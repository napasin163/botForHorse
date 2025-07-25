from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"🖱 คลิกที่ตำแหน่ง: x={x}, y={y}")

# สร้าง listener
with mouse.Listener(on_click=on_click) as listener:
    print("รอฟังคลิก... (กด Ctrl+C เพื่อหยุด)")
    listener.join()
