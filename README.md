# Python-Minify-CSS
Minifying CSS has never been faster or easier!

A Python-based tool to efficiently minify your CSS content. This utility streamlines your stylesheets by trimming unnecessary spaces, removing comments, and optimizing value representations for a more compact and web-optimized CSS file. Great for web developers aiming to improve site performance without manually sifting through lines of styling code!

Requirements
To successfully run and use the provided CSS Minifier script, ensure you meet the following prerequisites:

Python:
The script is written in Python, and you need to have Python installed on your machine. The code was tested with Python 3.9, but it should work with other 3.x versions. You can download and install Python from python.org.

Verify your Python installation by running the following command in your terminal or command prompt:

bash
Copy code
python --version
Read & Write Access:
Ensure you have read access to the source CSS file and write access to the destination where the minified CSS will be saved. If you're on a UNIX-like system, check and potentially modify file permissions if needed.
Script Dependencies:
Standard Library Dependencies: The script uses Python's built-in libraries:

re: This module provides support for regular expressions, which the script uses to minify the CSS.
tkinter and filedialog: These modules enable the script to provide a graphical file selection dialog.
Currently, you don't need to install additional Python packages from external sources as all required modules are part of the standard library. If in the future any other dependencies are added, it's recommended to create a virtual environment and install the required packages using pip.