# Meraki BSSID List

This project, "Meraki BSSID Dump", creates a simple, yet powerful, Python script that generates a list of enabled BSSIDs across an organization's Meraki wireless networks. By executing a few simple commands, network administrators can retrieve detailed BSSID information from their wireless networks, thus facilitating more effective network management and troubleshooting.

## Technology Stack

The script is written in Python, and interacts with the Meraki cloud via the Meraki DashboardAPI. Python was chosen for its syntactical simplicity, and the comprehensive support provided by Meraki's Python SDK.

## Status

The current script version is a stable release (1.0), however, updates and improvements are expected as and when necessary.

## Use Case

The script's primary use case is to retrieve BSSID details from an organization, network, and device registered under Meraki. Essentially, it offers network administrators a simplified data gathering process, otherwise a convoluted task that requires significantly more time and effort.

## Installation

Follow the steps below for installation and setup:

1. Clone the repo using the following link:

```bash
git clone https://github.com/shantarsecurity/meraki-bssid-dump.git
cd meraki-bssid-dump
```

2. Install the `meraki` package:

```bash
pip install meraki
```

## Configuration

Ensure to replace `'Your Meraki API Key'` in the script with your actual Meraki Dashboard API key.

## Usage

To run the script, use the following command:

```bash
python3 meraki-bssid-dump.py
```

Upon successful execution, the script creates a `bssid.csv` file in the directory where the script was run. This file contains the fetched BSSID details.

## Known Issues

Should your network host a large number of devices, the script may execute for a while, given each device requires an API request. This delay is due to the rate limit imposed on the Meraki API and is a known issue. Therefore, it's advised to run the script during off-peak times or a period with less network traffic.

## Future Improvements

Future versions could potentially include a progress display, specific fetch options for organizations/networks/devices, and additional filters or formatters for the output data.

## Contributions

Community contributions are always welcome! Please fork the project and submit your pull requests!

## License

This project is licensed under the GPL-3.0 license. For additional details, refer to the [LICENSE](LICENSE) file.
