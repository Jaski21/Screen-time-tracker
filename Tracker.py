import time
import pygetwindow as gw
from pynput import keyboard, mouse

last_input_time = time.time()
idle_threshold = 10
active_time = {}
current_app = None
last_key = None


def on_input(event=None):
    global last_input_time
    last_input_time = time.time()


def start_listeners():

    def on_key_press(key):
        global last_input_time, last_key
        last_input_time = time.time()
        last_key = key

    mouse.Listener(on_move=on_input, on_click=on_input, on_scroll=on_input).start()
    keyboard.Listener(on_press=on_key_press).start()


def get_active_window_title():
    try:
        win = gw.getActiveWindow()
        return win.title 
    except:
        return "Unknown"


def log_active_time(app_name):
    if app_name not in active_time:
        active_time[app_name] = 0
    active_time[app_name] += 1


def video_playing(window_title):
    keywords = ["YouTube", "Netflix", "Media Player", "Hotstar",]
    return any(keyword.lower() in window_title.lower() for keyword in keywords)


def summary():
    total = 0
    print("\n----------Screen Time----------\n")
    for app, seconds in active_time.items():
        minutes = seconds // 60
        sec = seconds % 60
        print(f"{app}: {minutes}m {sec}s")
        total += seconds
    print(f"\nTotal screen time = {total//60}m {total%60}s")


def main_loop():
    global current_app
    was_idle = False
    while True:
        now = time.time()

        active_window = get_active_window_title()
        if active_window == "Program Manager":
            active_window = "Desktop"

        if (last_key == keyboard.Key.esc and "visual studio" in active_window.lower()):
            print("\n[Exiting code]\n")
            summary()
            break

        idle = (now - last_input_time > idle_threshold) and not video_playing(active_window)
       
        if not idle:
            if was_idle:
                print("[Resumed tracking]")
            if active_window != current_app:
                current_app = active_window
                print(f"[Switched to] {current_app}")
            log_active_time(current_app)
            was_idle = False
        else:
            if not was_idle:
                print("[Idle] Not tracking...")
                was_idle = True

        time.sleep(1)


if __name__ == "__main__":
    print("\n----------Tracker----------\n")
    start_listeners()
    main_loop()