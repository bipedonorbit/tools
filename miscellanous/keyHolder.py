import pyautogui
import time
import threading

def hold_alt():
    duration = 30
    pyautogui.keyDown('alt')
    for remaining_time in range(duration, 0, -1):
        print(f"Time left: {remaining_time} seconds")
        time.sleep(1)
    pyautogui.keyUp('alt')  # Release the Alt key

# Start the Alt holding thread
alt_thread = threading.Thread(target=hold_alt)
alt_thread.start()

# Wait for the Alt holding thread to finish (wait for 30 seconds)
alt_thread.join()

print("Alt key held for 30 seconds and released.")
