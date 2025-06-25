import pyautogui
import keyboard

positions = []

def add_to_list(event):
    if event.name == 'y':
        pos = pyautogui.position()
        positions.append(pos)
        print(f"Added position: {pos}")

print("Press 'Y' to record mouse position. Press ESC to quit.")

keyboard.on_press(add_to_list)
keyboard.wait("esc")

print("\nFinal positions recorded:")
for i, pos in enumerate(positions, 1):
    print(f"{i}: {pos}")
