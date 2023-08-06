# Meraki BSSID Dump

🔍 This project, **'Meraki BSSID Dump'**, is a Python script created to export BSSID (Basic Service Set Identifier) information from an organization's Meraki wireless networks. The primary use case is to retrieve BSSID details for manual import into e911 services location data. It provides network administrators with a simplified method to gather BSSID information, aiding in network troubleshooting and management.

CSV file example output:
<center>
| Device Name | BSSID              | SSID Name | Band  |
|-------------|--------------------|-----------|-------|
| Device1     | 00:11:22:33:44:55  | Network1  | 2.4GHz|
| Device1     | 66:77:88:99:AA:BB  | Network1  | 5GHz  |
| Device2     | CC:DD:EE:FF:00:11  | Network2  | 2.4GHz|
</center>
Please note that the actual values will depend on the data returned by the Meraki API.

## Technology Stack

🔧 The script is written in Python and utilizes the Meraki DashboardAPI to interact with the Meraki cloud. Python was chosen for its simplicity and the comprehensive support provided by Meraki's Python SDK.

## Status

✅ The current version of the script is stable (1.0), but updates and improvements may be implemented as needed.

## Use Cases

🎯 The script's primary use case is to export BSSID details for e911 services location data. However, it can also be beneficial for large enterprises such as colleges and hospitals. Here are a few additional use cases:

- **Colleges and Universities**: In a college or university environment, the script can help network administrators identify and manage BSSIDs across multiple campuses, buildings, and access points. This information can be useful for optimizing network performance, monitoring network utilization, and ensuring proper coverage across campus areas.

- **Hospitals and Healthcare Facilities**: For hospitals and healthcare facilities with complex network infrastructure, the script can assist in monitoring and managing BSSIDs. It allows network administrators to track the performance of wireless networks in different areas within the facility, ensuring critical connectivity for medical devices, patient monitoring systems, and staff communication.

- **Enterprise Networks**: In large enterprises with multiple branch offices and locations, the script can provide network administrators with a consolidated view of BSSID details across the organization.  

## Installation

To install and use the script:

1. Clone the [repo](https://github.com/shantarsecurity/meraki-bssid-dump) using the following command:

```bash
git clone https://github.com/shantarsecurity/meraki-bssid-dump.git
cd meraki-bssid-dump
```

2. Install the `meraki` package:

```bash
pip3 install meraki
```

## Configuration

Before running the script, make sure to replace `'Your Meraki API Key'` in the script with your actual Meraki Dashboard API key.

## Usage

To execute the script, use the following command:

```bash
python3 meraki-bssid-dump.py
```

The script will generate a `bssid.csv` file in the same directory, containing the fetched BSSID details.

## Known Issues

⚠️ Running the script on networks with a large number of devices may take some time due to the rate limit imposed by the Meraki API. It is advised to run the script during off-peak hours or schedule it accordingly.

## Future Improvements

🔮 Future versions of the script may include added features such as a progress display, filtering options, and customized output formats.

## Contributions

🤝 Thanks to Matt Giepert for the bulk of the starting code! Future contributions are welcome! If you have any ideas or improvements, feel free to fork the project and submit a pull request.

## License

📜 This project is licensed under the GPL-3.0 license. For more information, please refer to the [LICENSE](LICENSE) file.
