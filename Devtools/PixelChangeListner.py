import pyautogui
import time
import datetime

def watch_pixel_change(pos, check_interval=0.2):
    print(f"Watching pixel at {pos} for color changes...")
    last_color = pyautogui.pixel(*pos)
    print(f"Initial color: {last_color}")

    try:
        while True:
            current_color = pyautogui.pixel(*pos)
            if current_color != last_color:
                now = datetime.datetime.now()
                print(f"[{now.strftime('%H:%M:%S.%f')[:-3]}] Color changed: {last_color} -> {current_color}")
                last_color = current_color
            time.sleep(check_interval)
    except KeyboardInterrupt:
        print("Stopped watching.")

if __name__ == "__main__":
    pos = (951, 896)  # Change this to your pixel of interest
    watch_pixel_change(pos)
