# ProSoft

ProSoft is a simple Python program designed to automatically clear temporary files and free up system space on Windows. This utility helps maintain your system by removing unnecessary files that accumulate over time, potentially improving system performance.

## Features

- Clears temporary files from the system's temporary directory.
- Clears temporary files from the Windows-specific temporary directory.
- Logs actions performed during the cleanup process for easy monitoring.

## Requirements

- Python 3.x
- Windows operating system

## Installation

1. Clone the repository or download the `prosoft.py` file.
2. Ensure Python is installed on your system and added to your PATH.

## Usage

1. Open a command prompt or terminal.
2. Navigate to the directory where `prosoft.py` is located.
3. Run the program using the command:

   ```bash
   python prosoft.py
   ```

## Logging

ProSoft logs its actions, including any errors encountered during the cleanup process. Logs are printed to the console for easy access.

## Disclaimer

ProSoft is designed to perform safe operations by removing only files in the temporary directories. However, always ensure that important data is backed up before running cleanup operations. The authors are not responsible for any accidental data loss.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.