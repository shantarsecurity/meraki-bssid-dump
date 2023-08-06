import meraki

# Your Meraki API key
api_key = 'Your Meraki API Key'

#create dashboard object
dash = meraki.DashboardAPI(api_key, suppress_logging=True)

#loop through orgs
for org in dash.organizations.getOrganizations():
    print(f"Processing organization: {org['id']}...")
    #loop through nets
    for net in dash.organizations.getOrganizationNetworks(org['id']):
        print(f"  Processing network: {net['id']}...")
        #loop through devices
        for device in dash.networks.getNetworkDevices(net['id']):
            #check if device is an AP
            if 'MR' in device.get('model', '') or 'CW' in device.get('model', ''):
                print(f"    Processing AP device: {device['serial']}...")
                #get BSSID list
                status = dash.wireless.getDeviceWirelessStatus(device['serial'])
                #loop through all sets
                for set in status['basicServiceSets']:
                    #only report on enabled
                    if set.get('enabled'):
                        print(f"      Processing BSSID: {set['bssid']}...")
                        list = [device.get('name', 'None'), set.get('bssid', 'None'), set.get('ssidName', 'None'), set.get('band', 'None')]
                        with open('bssid.csv', 'a') as file:
                            file.write(f"{','.join(list)}\n") 
print("Processing completed.")
