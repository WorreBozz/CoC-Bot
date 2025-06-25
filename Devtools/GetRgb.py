import pyautogui
import keyboard  # Make sure to install this: pip install keyboard
import time

print("Press 'C' to check the pixel under your mouse.")
print("Press 'Esc' to exit.")

while True:
    if keyboard.is_pressed('c'):
        x, y = pyautogui.position()
        rgb = pyautogui.pixel(x, y)
        print(f"Pixel at ({x}, {y}) = {rgb}")
        time.sleep(0.3)  # Prevent double-trigger

    if keyboard.is_pressed('esc'):
        print("Exiting.")
        break
