# Power Measurement Code Snippet Repo

This repository contains various code snippets and tools related to power measurement and monitoring. The main goal is to retrieve power values using both Redfish and IPMI interfaces and compare them over time. This repository is intended for data center operators, system administrators, and developers interested in hardware monitoring and power consumption analytics.

## Overview

In this repository you will find:
- **redfish_ipmi_power_comparison.py**: A Python script that retrieves power measurements from a server's BMC using both Redfish and IPMI protocols and logs the data into a CSV file for later analysis.

### Features

- **Dual-Protocol Monitoring**: Simultaneously measure power consumption using both the modern Redfish API and the legacy IPMI protocol.
- **CSV Logging**: Continuously logs power data into a CSV file so that you can easily import it into Excel or other graphing tools for analysis.
- **Comparison and Analysis**: Provides a framework to compare the power consumption values from both interfaces.

## Prerequisites

- **Python 3.9**
- Required Python libraries:
  - `pyghmi` (for IPMI and Redfish interactions)
  - Standard libraries: `csv`, `time`, `datetime`
- Access to a server or hardware with a BMC that supports both Redfish and IPMI.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests with improvements, bug fixes, or additional code snippets related to power monitoring and measurement.

## License
This project is licensed under the Apache License. See the LICENSE file for details.

## Disclaimer
This repository is provided "as-is" without any warranties. Use it at your own risk, and please ensure that you comply with your hardware vendor's guidelines when accessing management interfaces like IPMI and Redfish.

