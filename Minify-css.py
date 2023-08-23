"""
CSS Minifier

Description:
    A simple Python script to minify CSS files. The script provides a GUI to select the target CSS file, then creates a minified version of it in the same directory with a "_minified.css" suffix.

Author:
    Johann Coetzee

Creation Date:
    August 23, 2023

License:
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.

Version:
    1.0.0
"""
import re
import tkinter as tk
from tkinter import filedialog

def minify_css(css_content):
    """
    Function to minify given CSS content.
    
    Parameters:
    - css_content (str): Original CSS content to be minified.
    
    Returns:
    - str: Minified CSS content.
    """

    # Remove comments: Matches anything between /* and */ and removes it.
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    
    # Remove whitespaces around punctuation: Matches spaces around {}, :, ;, and , and replaces them with the punctuation without spaces.
    css_content = re.sub(r'\s*([{}:;,])\s*', r'\1', css_content)
    
    # Remove last semicolon in a block: Matches ;} and replaces it with just }.
    css_content = re.sub(r';}', r'}', css_content)

    # Nested function to handle replacement of units with just 0.
    def replace_unit_with_zero(match):
        """
        Function to replace units (px, em, %, etc) that follow a 0 with just 0.
        
        Parameters:
        - match (re.Match object): Match object containing the matched pattern.
        
        Returns:
        - str: Replacement string.
        """
        return match.group(1) + '0'

    # Use the above function to replace 0 followed by a unit with just 0.
    css_content = re.sub(r'(:|\s)0(px|em|%|in|cm|mm|pc|pt|ex)', replace_unit_with_zero, css_content)
    
    # Replace multiple spaces with one: Matches one or more spaces and replaces them with a single space.
    css_content = re.sub(r'\s+', ' ', css_content).strip()

    # Return the minified content.
    return css_content


def select_file():
    """
    Function to open a file explorer and return the selected file path.

    Returns:
    - str: Path to the selected file.
    """
    root = tk.Tk()  # instantiate main window
    root.withdraw()  # hide main window
    file_path = filedialog.askopenfilename(title="Select a CSS file", filetypes=(("CSS files", "*.css"), ("All files", "*.*")))
    return file_path

if __name__ == "__main__":
    input_file = select_file()  # Open file explorer and get the selected file path
    
    if not input_file:  # Check if a file was actually selected
        print("No file selected. Exiting...")
        exit()

    # Open the selected CSS file and read its content.
    with open(input_file, 'r') as f:
        content = f.read()
        
    # Minify the content using the minify_css function.
    minified_content = minify_css(content)

    # Here, we're saving the minified content in the same directory as the input but with a "_minified" suffix.
    output_file = input_file.rsplit('.', 1)[0] + '_minified.css'
    with open(output_file, 'w') as f:
        f.write(minified_content)

    # Print a success message.
    print(f"CSS Minified Successfully! Saved as {output_file}")
