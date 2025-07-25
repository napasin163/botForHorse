import pyautogui
import time

print("เลื่อนเมาส์ไปตำแหน่งที่ต้องการดูพิกัด (Ctrl+C เพื่อหยุด)")
while True:
    x, y = pyautogui.position()
    print(f"ตำแหน่ง: {x}, {y}")
    time.sleep(0.5)
ababababab