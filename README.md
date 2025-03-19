# Password Generator

A simple GUI-based password generator built with Python and Tkinter. This tool allows users to create random passwords with customizable character compositions, including uppercase letters, lowercase letters, digits, and symbols.

## Features
- Choose the number of uppercase letters, lowercase letters, digits, and symbols.
- Generate a secure random password.
- Copy the generated password to the clipboard.
- Light/Dark theme toggle.

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/Gabrielazmbr/RandomPasswordGenerator.git
cd RandomPasswordGenerator
```

### 2. Install Dependencies (If applicable)
Ensure you have Python installed (version 3.6 or later). The required dependencies are minimal:

```sh
pip install -r requirements.txt
```

### 3. Install Tkinter (if not already installed)
#### For Linux (Debian-based)
```sh
sudo apt-get install python3-tk
```
#### For macOS and Windows
Tkinter comes pre-installed with Python, but if needed, reinstall Python from [python.org](https://www.python.org/downloads/).

## Usage
Run the script using Python:
```sh
python password_generator.py
```

Adjust the sliders to customize your password, then click **"Generate"**. You can copy the password to your clipboard using the **"Copy"** button.

## File Structure
```
password-generator/
│── azure.tcl               # Theme file
│── theme/                  # Folder containing dark.tcl and light.tcl
│── password_generator.py   # Main script
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
```

## Requirements

Python 3.6 or later

Libraries: Tkinter

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements.

## Author
Developed by Gabrielazmbr

