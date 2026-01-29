# Import Resources
import meraki
import csv
import getpass
from tqdm import tqdm

# Function to prompt for the Meraki API Key
def get_api_key():
    try:
        user_api_key = getpass.getpass("Enter your Meraki API Key to continue: ", echo_char='*')
    except:
        raise Exception("Unable to prompt for API Key!\n\nYou might need to set your API Key statically in the script file.")
    else:
        return user_api_key

# Initialize the api_key variable as an empty string
api_key = ""

# Request Meraki API Key from the user by looping until a nominally viable entry is provided
while len(api_key) < 40:
    try:
        api_key = get_api_key()
    except:
        raise Exception("An error occurred in prompting for the API Key!\n\nStatic configuration might be necessary.")
    else:
        if len(api_key) >= 40:
            print("Thank you for providing your Meraki API Key!")
        else:
            print("Your Meraki API Key is required to continue!\nMerkai API Keys should be at least 40 characters long.\n")

# Manual / Static Meraki API Key Override
# If your runtime environment does not support getpass for some reason, you can uncomment this section and set your API Key permanently here.
# Be aware of the potential risks of storing your API key in a plaintext file like this.
# api_key = ''

# Create Meraki Dashboard object
try:
    dash = meraki.DashboardAPI(api_key, suppress_logging=True)
except:
    raise Exception("Unable to define the Meraki Dashboard API connection! Check api_key")

# Initialize counters to track parsing
netCount        = 0
devCount        = 0
bssidCount      = 0
totalNets       = 0
totalDevices    = 0
totalOrgs       = 0

# Get Meraki Organizations
print("Fetching Meraki Organizations...")
try:
    dashOrgs = dash.organizations.getOrganizations()
    # Returns a List object
except:
    raise Exception("Unable to get Meraki Organizations from the Meraki Dashboard API!")
else:
    totalOrgs = len(dashOrgs)
    # Initialize empty list to hold details for parsed networks
    allMatchedNetworks = []
    print(f"  Found {totalOrgs} Meraki Organizations!")
    # Parse Meraki Organization information
    if totalOrgs > 0:
        print("Searching organizations for networks with wireless products...")
        # Initialize empty dictionary to store Organization names as values for their IDs (as keys)
        orgDetails = {}
        for org in dashOrgs:
            # Normalize keys and values and store in orgDetails dictionary
            org_id = str(org.get("id", ""))
            org_name = str(org.get("name", ""))
            orgDetails[org_id] = org_name
            try:
                # Get network details for each organziation
                orgNetworks = dash.organizations.getOrganizationNetworks(org_id, productTypes=["wireless"], total_pages="all")
            except:
                print(f"[!!]An exception occurred when trying to retrieve networks for organization id: {org_id} (\"{org_name}\")")
            else:
                # Store data for networks
                allMatchedNetworks.extend(orgNetworks)
                orgNetworkCount = len(orgNetworks)
                print(f"  Organization ID: {org_id} named \"{org_name}\" has {orgNetworkCount} networks with wireless devices")
        totalNets = len(allMatchedNetworks)
        print(f"{totalNets} networks with wireless devices were found!")
    else:
        print(f"No organizations were found using the provided Meraki Dashboard API key")

if totalNets > 0:
    print("Collecting wireless device details...")
    # Initialize empty list to store discovered BSSID data
    discoveredBSSIDs = []
    # Loop through networks to collect device information
    for net in tqdm(allMatchedNetworks, desc="Network", unit="network", miniters=1, position=1, bar_format="{desc} {n_fmt}/{total_fmt} {percentage:.0f}% {bar}Elapsed: {elapsed} ETA: {remaining}"):
        netCount = netCount + 1
        netId = str(net.get("id"))
        netName = str(net.get("name"))
        orgId = str(net.get("organizationId"))
        orgName = str(orgDetails.get(orgId, ""))
        tqdm.write(f"  Organization: {orgId} \"{orgName}\"")
        tqdm.write(f"    Processing network {netCount}/{totalNets} ID: {netId} Name: {netName}")
        try:
            netDevices = dash.organizations.getOrganizationDevices(organizationId=orgId, networkIds=[netId], productTypes="wireless", perPage=5000, total_pages="all")
        except:
            print(f"[!!] An excption occurred in processing network ID {netId}")
        else:
            devCount = len(netDevices)
            tqdm.write(f"      {devCount} wireless devices found!")
            currentNetDevCount = 0
            for netDevice in tqdm(netDevices, desc="Network Device", unit="device", miniters=1, position=0, leave=False, bar_format="{desc} {n_fmt}/{total_fmt} {percentage:.0f}% {bar}"):
                currentNetDevCount      = currentNetDevCount + 1
                totalDevices            = totalDevices + 1
                tqdm.write(f"        Processing wireless device {currentNetDevCount}/{devCount}:")
                currentNetDevModel      = str(netDevice['model'])
                currentNetDevSerial     = str(netDevice['serial'])
                currentNetDevMacAddress = str(netDevice.get('mac', ""))
                currentNetDevLanIp      = str(netDevice.get('lanIp', ""))
                currentNetDevName = str(netDevice['name']) if netDevice['name'] is not None else currentNetDevSerial
                currentNetDevAddress = str(netDevice.get('address', ''))
                currentNetDevLatitude = str(netDevice.get('lat', ''))
                currentNetDevLongitude = str(netDevice.get('lng', ''))
                currentNetDevFloorPlanId = str(netDevice.get('floorPlanId', ''))
                currentNetDevNotes = str(netDevice.get('notes', ''))
                tqdm.write(f"          Model:         {currentNetDevModel}")
                tqdm.write(f"          Serial:        {currentNetDevSerial}")
                tqdm.write(f"          Base MAC:      {currentNetDevMacAddress}")
                tqdm.write(f"          LAN IP:        {currentNetDevLanIp}")
                tqdm.write(f"          Name:          {currentNetDevName}")
                tqdm.write(f"          Location:      {currentNetDevAddress}")
                tqdm.write(f"          Longitude:     {currentNetDevLongitude}")
                tqdm.write(f"          Latitude:      {currentNetDevLatitude}")
                tqdm.write(f"          Floor Plan ID: {currentNetDevFloorPlanId}")
                tqdm.write(f"          Notes:         {currentNetDevNotes}")
                try:
                    # get BSSID List
                    status = dash.wireless.getDeviceWirelessStatus(netDevice['serial'])
                except:
                    print(f"[!!] An exception occurred in processing BSSIDs for {currentNetDevSerial}")
                else:
                    # Loop through all basic service sets
                    for set in status['basicServiceSets']:
                        # Only report on enabled BSSIDs
                        if set.get('enabled'):
                            bssidCount = bssidCount +1
                            deviceBssid = str(set['bssid'])
                            deviceSsid = str(set['ssidName'])
                            bssidBand = str(set['band'])
                            tqdm.write(f"      Processing BSSID: {deviceBssid}")
                            tqdm.write(f"        BSSID: {deviceBssid}")
                            tqdm.write(f"        SSID:  {deviceSsid}")
                            tqdm.write(f"        Band:  {bssidBand}")
                            # Construct dictionary for current output
                            currentBSSIDoutput = {
                                "netId"             :   netId,
                                "netName"           :   netName,
                                "deviceModel"       :   currentNetDevModel,
                                "deviceSerial"      :   currentNetDevSerial,
                                "deviceMacAddress"  :   currentNetDevMacAddress,
                                "deviceLanIp"       :   currentNetDevLanIp,
                                "deviceName"        :   currentNetDevName,
                                "deviceAddress"     :   currentNetDevAddress,
                                "deviceLongitude"   :   currentNetDevLongitude,
                                "deviceLatitude"    :   currentNetDevLatitude,
                                "deviceFloorPlanId" :   currentNetDevFloorPlanId,
                                "deviceNotes"       :   currentNetDevNotes,
                                "deviceBssid"       :   deviceBssid,
                                "deviceSsid"        :   deviceSsid,
                                "bssidBand"         :   bssidBand
                                }
                            # Append current dictionary to output list
                            discoveredBSSIDs.append(currentBSSIDoutput)
    print("Processing completed!")
    print(f"  Evaluated {totalDevices} devices in {netCount} networks.")
    print(f"  Found {bssidCount} BSSIDs enabled on {totalDevices} wireless access points.")
    # Define the field names (keys of the dictionaries) that will become the header row
    fieldnames = ["netId", "netName", "deviceModel", "deviceSerial", "deviceMacAddress", "deviceLanIp", "deviceName", "deviceAddress", "deviceLongitude", "deviceLatitude", "deviceFloorPlanId", "deviceNotes", "deviceBssid", "deviceSsid", "bssidBand"]
    print(f"Writing {len(discoveredBSSIDs)} BSSIDs to Meraki-BSSIDs.csv")
    try:
        with open('Meraki-BSSIDs.csv', 'w', encoding="utf-8", newline='') as csvfile:
            # Create a DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write header row to CSV
            writer.writeheader()
            # Write data to CSV
            writer.writerows(discoveredBSSIDs)
        print("Finished writing to Meraki-BSSIDs.csv!")
    except IOError as e:
        print(f"I/O error: {e}")
else:
    print("No wireless devices to evaluate!")