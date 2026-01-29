[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/shantarsecurity/meraki-bssid-dump)
[![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/devenv/?id=devenv-vscode-base&GITHUB_SOURCE_REPO=https://github.com/shantarsecurity/meraki-bssid-dump)
# Meraki BSSID Dump

🔍 This project, **'Meraki BSSID Dump'**, is a Python script that exports BSSID (Basic Service Set Identifier) information for an organization's Meraki wireless networks.

## Use Cases

🎯 The script's primary use case is to export BSSID details for import into geolocation services (e.g., e911 services).\
\
🏢 This is often necessary for large organizations like, Colleges and Universities, Hospitals and Healthcare Facilities, and Private Enterprise Networks.

## Technology Stack

🔧 The script is written in Python and utilizes the [Meraki Dashboard API Python Library](https://github.com/meraki/dashboard-api-python/tree/main) to interact with the [Meraki Dashboard API](https://developer.cisco.com/meraki/api-v1/).

🐍 Python was chosen for its simplicity and the comprehensive support provided by Meraki's Python SDK. 

### Dependencies

<details>

| **Module** | **Documentation** | **Notes** |
|------------|-------------------|-----------|
| `meraki`   | [Meraki](https://github.com/meraki/dashboard-api-python/tree/main) | This is the official Dashboard API library (SDK) for Python. |
| `csv`      | [CSV](https://docs.python.org/3/library/csv.html) | This is a built-in, [Standard Library](https://docs.python.org/3/library/index.html) module. |
| `getpass`  | [getpass](https://docs.python.org/3/library/getpass.html) | This is a built-in, [Standard Library](https://docs.python.org/3/library/index.html) module. |
| `tqdm`     | [tqdm](https://github.com/tqdm/tqdm) | This is a mature, stable, efficient, and widely-supported library that provides progress-bar functionality. |

</details>

## Status

✅ The current version of the script is stable (1.0), but updates and improvements may be implemented as needed.

## Installation

To install the script:

1. Clone the [repo](https://github.com/shantarsecurity/meraki-bssid-dump) using the following command:

```bash
git clone https://github.com/shantarsecurity/meraki-bssid-dump.git
cd meraki-bssid-dump
```

2. Install the [Meraki Dashboard API Python Library](https://github.com/meraki/dashboard-api-python/tree/main):

```bash
pip3 install --upgrade meraki
```

3. Install the [tqdm library](https://github.com/tqdm/tqdm):

```bash
pip3 install --upgrade tqdm
```

## Usage

To execute the script, use the following command:

```bash
python3 meraki-bssid-dump.py
```

## Input

🗝️ You will be prompted to provide a valid [API Key](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/How-Tos/Cisco_Meraki_Dashboard_API#Generate_an_API_Key) for your Meraki account. This is ***required*** in order to access the Meraki Dashboard API. You can read more about generating and managing API keys for the Meraki Dashboard API in the [Cisco Meraki Dashboard Administration documentation](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/How-Tos/Cisco_Meraki_Dashboard_API).

## Output

💾 The script will generate a `Meraki-BSSIDs.csv` file in the same directory, containing the fetched BSSID details.\
⚠️ This file will be overwritten with each execution.

<details>

<summary>Sample CSV File Output</summary>

### Sample CSV File Output

| Network ID | Network Name | Device Model | Device Serial  | Device Base MAC   | LAN IP          | Display Name | Location Address   | Longitude | Latitude | Floor Plan ID | Notes     | BSSID              | SSID      | Band  |
|------------|--------------|--------------|----------------|-------------------|-----------------|--------------|--------------------|-----------|----------|---------------|-----------|--------------------|-----------|-------|
| A_12345678 | MyNetwork1   | CW1234L      | A12B-CD34-E56F | a1:b2:c3:d4:e5:f6 | 123.456.789.101 | Device1      | 123 A Street NW    | -45.678   |  90.123  | None          |           | 00:11:22:33:44:55  | Network1  | 2.4GHz|
| A_12345678 | MyNetwork1   | MR99         | GH78-I9J0-1K2L | 1a:2b:3c:4d:5e:6f | 121.314.151.617 | Device1      | 456 D Aveneue SE   | -90.123   | -45.678  | None          |           | 66:77:88:99:AA:BB  | Network1  | 5GHz  |
| A_12345678 | MyNetwork1   | MR01         | 3M45-O6N8-9Q09 | ab:12:cd:34:ef:56 | 181.920.212.223 | Device2      | 789 13th Blvd      |  45.678   | -90.123  | None          |           | CC:DD:EE:FF:00:11  | Network2  | 2.4GHz|

</details>

## Precautions

⏱️ Running the script for Meraki organizations or networks with a large number of devices will take some time due to the strict rate limits imposed by the Meraki API. It is advised to run the script during off-peak hours or schedule it accordingly. For reference, in testing it has taken 25-30 minutes to process 9,447 BSSIDs on 1,230 devices across 615 networks.

## Limitations

<details>

<summary>Interactive API Key Prompt</summary>

In rare cases, due to limitations in the `getpass` module, the interactive prompt for the Meraki API Key might not work correctly. If you are affected by this, there is commented code you can edit to set your Meraki API Key statically. If you need to apply this override, also comment-out the preceeding while loop that handles the interactive prompt. See the [getpass documentation](https://docs.python.org/3/library/getpass.html) for details on its limitations. 

`getpass` is part of the official [Python Standard Library](https://docs.python.org/3/library/index.html).\
***It should be extremely unusual for these limitations to impact interactive users.***

</details>

## Future Improvements

🔮 Future versions of the script might include added features such as:
- [x] Progress Display
- [ ] Filtering Options
- [ ] Customized Output Formats
- [ ] Interactive Output File Overwrite Hanlding

## Contributions

🤝 Thanks to Matt Giepert for the bulk of the starting code! Future contributions are welcome! If you have any ideas or improvements, feel free to fork the project and submit a pull request.

## Additional Reading

<details>

<summary>Calculating Cisco Meraki BSSID MAC Addresses</summary>

### Calculating Cisco Meraki BSSID MAC Addresses

The document "[Calculating Cisco Meraki BSSID MAC Addresses](https://documentation.meraki.com/MR/Wi-Fi_Basics_and_Best_Practices/Calculating_Cisco_Meraki_BSSID_MAC_Addresses)" offers a comprehensive guide on how BSSID MAC addresses are computed for Cisco Meraki access points. Each SSID is represented by a unique BSSID, which helps clients identify the associated access point. The BSSID addresses are derived from the wired MAC address, with calculations based on the MAC OUI. Different MAC OUIs for various access point models determine the adjustments for 2.4 GHz and 5 GHz bands. The BSSID values are assigned to each radio and SSID, with up to 15 possible BSSID combinations per radio.

👉 This script does not perform these calculations. It retrieves the BSSIDs from the Meraki Dashboard API.
</details>

## License

📜 This project is licensed under the GPL-3.0 license. For more information, please refer to the [LICENSE](LICENSE) file.
