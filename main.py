import pytesseract
from PIL import ImageGrab
import os
import platform
import subprocess
import pyperclip
import keyboard
import time

variable_name = "TESSERACT_PATH"

def setTesseractPath(variable_name):
    # Check if the environment variable exists
    if not os.environ.get(variable_name):
        print(f"Environment variable '{variable_name}' does not exist.")
        
        # Set default value for Tesseract path
        default_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        
        # Check the operating system
        system = platform.system()

        if system == "Windows":
            # Set the Tesseract path for Windows using setx
            os.environ[variable_name] = default_path
            # Construct the setx command
            try:
                os.system(f'setx {variable_name} "{default_path}"')
                print(f"Setting environment variable '{variable_name}' for Windows.")
            except subprocess.CalledProcessError as e:
                print(f"Error occurred: {e}")  
        
        elif system == "Linux" or system == "Darwin":  # Darwin is for macOS
            # Set the Tesseract path for Linux/macOS
            # Modify the ~/.bashrc or ~/.zshrc to include the variable
            home_dir = os.path.expanduser("~")
            shell_config_file = os.path.join(home_dir, '.bashrc' if system == 'Linux' else '.zshrc')
            
            with open(shell_config_file, 'a') as file:
                file.write(f'\nexport {variable_name}="{default_path}"\n')
            
            # You may also want to notify the user to reload the shell config
            print(f"Added Tesseract path to {shell_config_file}. Please reload your shell.")
        
        else:
            print(f"Unsupported system: {system}")
    else:
        print(f"Environment variable '{variable_name}' already exists with value: {os.environ[variable_name]}")

def transfer(file, tesseract_path):
    # Set the path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    # Perform OCR to extract text
    text = pytesseract.image_to_string(file)

    # Copy the extracted text to the clipboard
    pyperclip.copy(text)
    time.sleep(0.1)  # small delay to ensure clipboard is ready
    keyboard.press_and_release('ctrl+v')
    print("Text copied to clipboard and pasted.")

    # Print the extracted text
    # print(text)

def run():
    image = ImageGrab.grabclipboard()
    if image is None:
        print("No image found in clipboard.")
        return
    print("Image found in clipboard.")
        # Perform OCR on the screenshot
    try:
        transfer(image, os.environ[variable_name])
    except Exception as e:
        print("An error occurred during OCR, please add path to tesseract.exe in settings")

if __name__ == "__main__":
    setTesseractPath(variable_name)
    keyboard.add_hotkey('ctrl+shift+v', run)
    print("Running... Press Ctrl+Shift+V to paste the text. Press Shift+ESC to quit.")
    keyboard.wait('shift+esc')
    
