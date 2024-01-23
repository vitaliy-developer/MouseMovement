import pyautogui
import time

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Set the size of the square and its offset
square_size = 50
offset = 10

# Remember the initial cursor position
start_x, start_y = pyautogui.position()

# Calculate the coordinates of the square's vertices
top_left = (start_x - offset, start_y - offset)
bottom_left = (start_x - offset, start_y + square_size + offset)
top_right = (start_x + square_size + offset, start_y - offset)
bottom_right = (start_x + square_size + offset, start_y + square_size + offset)

try:
    while True:
        # Move the mouse cursor
        pyautogui.moveTo(top_right[0], top_right[1], duration=0.25)
        pyautogui.moveTo(bottom_right[0], bottom_right[1], duration=0.25)
        pyautogui.moveTo(bottom_left[0], bottom_left[1], duration=0.25)
        pyautogui.moveTo(top_left[0], top_left[1], duration=0.25)

        # Pause execution for 5 minutes (300 seconds)
        time.sleep(300)

except KeyboardInterrupt:
    pass
finally:
    # Return the cursor to the initial position after execution
    pyautogui.moveTo(start_x, start_y, duration=0.25)
