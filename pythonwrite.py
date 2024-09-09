import pyautogui
import time

def click_at_position(x, y):
    pyautogui.moveTo(x, y, duration=1)  # Move mouse to (x, y) with 1 second delay
    pyautogui.click()  # Perform a left-click

def type_script(script_text):
    # Split the script into lines and type each line with a newline
    for line in script_text.splitlines(True):
        pyautogui.write(line, interval=0.05)  # Adjust interval for typing speed
        pyautogui.press('enter')  # Simulate pressing Enter to move to the next line

if __name__ == "__main__":
    x = 500  # Replace with the x-coordinate
    y = 300  # Replace with the y-coordinate

    # Insert your code here
    script_text = '''
def greet(name):
    return f"Hello, {name}!"

name = "Alice"
print(greet(name))
'''

    # Adding a delay to switch to the desired window before the script runs
    print("Switch to the window where you want to click and type...")
    time.sleep(5)  # Give yourself 5 seconds to switch windows

    # Click at the specified position
    click_at_position(x, y)

    # Type the provided script with correct formatting
    type_script(script_text)

    print("Script typed successfully!")
