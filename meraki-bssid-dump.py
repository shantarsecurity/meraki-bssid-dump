# Import Resources
import meraki
import csv
import re

# Your Meraki API key
api_key = 'Your Meraki API Key'

#create dashboard object
dash = meraki.DashboardAPI(api_key, suppress_logging=True)

# Initialize output files and write headers (this will erase existing file contents to ensure clean output for each run)
bssidFileHeaders = ["Network ID", "Network Name", "Device Model", "Device Serial", "Device Base MAC", "LAN IP", "Display Name", "Location Address", "Longitude", "Latitude", "Floor Plan ID", "Notes", "BSSID", "SSID", "Band"]
with open('Meraki-BSSIDs.csv', 'w', encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(bssidFileHeaders)

skippedFileHeaders = ["Network ID", "Network Name", "Device Model", "Device Serial", "Display Name", "Location Address"]
with open('Meraki-SkippedDevices.csv', 'w', encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(skippedFileHeaders)

# Initialize counters to track parsing
orgCount = 0
netCount = 0
devCount = 0
matchCount = 0
bssidCount = 0
skipCount = 0

#loop through orgs
for org in dash.organizations.getOrganizations():
    orgCount = orgCount + 1
    print(f"Processing organization #{orgCount}: {org['id']}...")
    #loop through nets
    for net in dash.organizations.getOrganizationNetworks(org['id']):
        netCount = netCount + 1
        netId = str(net['id'])
        netName = str(net['name'])
        print(f"  Processing network #{netCount}:")
        print(f"  ID:   {netId}")
        print(f"  Name: {netName}")
        #loop through devices
        for device in dash.networks.getNetworkDevices(net['id']):
            devCount = devCount + 1
            deviceModel = str(device['model'])
            deviceSerial = str(device['serial']) if device['serial'] is not None else 'Serial Not Found'
            deviceMacAddress = str(device.get('mac', ''))
            deviceLanIp = str(device.get('lanIp', ''))
            deviceName = str(device['name']) if device['name'] is not None else deviceSerial
            deviceAddress = str(device.get('address', ''))
            deviceLatitude = str(device.get('lat', ''))
            deviceLongitude = str(device.get('lng', ''))
            deviceFloorPlanId = str(device.get('floorPlanId', ''))
            deviceNotes = str(device.get('notes', ''))

            #check if device is an AP
            #use regex matching to check start of string
            if re.match(r"MR",device.get('model', '')) or re.match(r"CW",device.get('model', '')):
                matchCount = matchCount + 1
                print(f"    Processing AP {matchCount}:")
                print(f"      Model:         {deviceModel}")
                print(f"      Serial:        {deviceSerial}")
                print(f"      Base MAC:      {deviceMacAddress}")
                print(f"      LAN IP:        {deviceLanIp}")
                print(f"      Name:          {deviceName}")
                print(f"      Location:      {deviceAddress}")
                print(f"      Longitude:     {deviceLongitude}")
                print(f"      Latitude:      {deviceLatitude}")
                print(f"      Floor Plan ID: {deviceFloorPlanId}")
                print(f"      Notes:         {deviceNotes}")
                #get BSSID list
                status = dash.wireless.getDeviceWirelessStatus(device['serial'])
                #loop through all sets
                for set in status['basicServiceSets']:
                    #only report on enabled
                    if set.get('enabled'):
                        bssidCount = bssidCount + 1
                        deviceBssid = str(set['bssid'])
                        deviceSsid = str(set['ssidName'])
                        bssidBand = str(set['band'])
                        print(f"      Processing BSSID: {deviceBssid}")
                        print(f"        BSSID: {deviceBssid}")
                        print(f"        SSID:  {deviceSsid}")
                        print(f"        Band:  {bssidBand}")
                        list = [netId, netName, deviceModel, deviceSerial, deviceMacAddress, deviceLanIp, deviceName, deviceAddress, deviceLongitude, deviceLatitude, deviceFloorPlanId, deviceNotes, deviceBssid, deviceSsid, bssidBand]
                        print("      Writing BSSID Info to file:")
                        for index, item in enumerate(list):
                            print(f"        {index}: {item}")
                        with open('Meraki-BSSIDs.csv', 'a', encoding="utf-8", newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(list)
            else:
                skipCount = skipCount +1
                print(f"    Skipping {device['serial']} because model is {device['model']}...")
                print(f"        Serial: {deviceSerial}")
                print(f"        Name:   {deviceName}")
                print(f"        Model:  {deviceModel}")
                list = [netId, netName, deviceModel, deviceSerial, deviceName, deviceAddress]
                print("     Writing Skipped Device Info to file:")
                for index, item in enumerate(list):
                    print(f"      {index}: {item}")
                with open('Meraki-SkippedDevices.csv', 'a', encoding="utf-8", newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(list)
print("Processing completed!")
print(f"  Evaluated {devCount} devices in {netCount} networks.")
print(f"  Found {bssidCount} BSSIDs enabled on {matchCount} wireless access points.")
print(f"  Skipped {skipCount} devices.")