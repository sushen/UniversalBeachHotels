import time

import pyautogui


class WakeMonitor:
    def wake(self):
        pyautogui.moveRel(100, 100)
        pyautogui.moveRel(-100, -100)


if __name__ == "__main__":
    for i in range(10000):
        print(f"Looping {i+1} for waking.")
        WakeMonitor().wake()
        time.sleep(1)
