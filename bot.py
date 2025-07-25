import pyautogui
import time
import keyboard
import inspect

while True:
    print("⏳ เริ่มภายใน 3 วินาที... (กด Left Ctrl เพื่อหยุด, กด X เพื่อรีเซ็ตเมื่อจบ)")
    time.sleep(3)

    def log_action(msg):
        frame = inspect.currentframe().f_back
        lineno = frame.f_lineno
        print(f"[Line {lineno}] {msg}")

    def click(x, y, delay=1):
        if keyboard.is_pressed('left ctrl'):
            print("🛑 หยุดโดยผู้ใช้ (Left Ctrl)")
            exit()
        pyautogui.moveTo(x, y)
        pyautogui.click()
        log_action(f"คลิกที่ตำแหน่ง x={x}, y={y}")
        time.sleep(delay)

    def type_text(text, delay=1):
        if keyboard.is_pressed('left ctrl'):
            print("🛑 หยุดโดยผู้ใช้ (Left Ctrl)")
            exit()
        pyautogui.write(text)
        log_action(f"พิมพ์ข้อความ: \"{text}\"")
        time.sleep(delay)

    print("⏳ เริ่มภายใน 3 วินาที... (กด Left Ctrl เพื่อหยุด)")
    time.sleep(3)

    # --- ลบผู้ใช้ ---
    click(1535, 835)
    click(781, 626)
    click(903, 585)
    click(903, 585)
    time.sleep(2)
    click(795, 588)
    time.sleep(1)

    # --- โหลดหน้าใหม่ ---
    print("🕐 กำลังรอโหลด 10 วินาที...")
    for i in range(10):
        if keyboard.is_pressed('left ctrl'):
            print("🛑 หยุดโดยผู้ใช้ (Left Ctrl)")
            exit()
        log_action(f"รอโหลด... {i+1}/10 วิ")
        time.sleep(1)

    # --- ล็อกอินและตั้งค่า ---
    click(795, 588)
    click(971, 395)
    click(969, 494)
    click(906, 645)
    click(933, 471)
    click(905, 648)
    click(906, 587)
    click(808, 469)
    type_text("200202")
    click(911, 585)
    log_action("⏳ รอโหลดหลัง login เพิ่มเติม 5 วิ...")
    time.sleep(5)
    click(907, 592)
    click(838, 415)
    time.sleep(1)
    type_text("a")
    click(809, 599)
    time.sleep(1)
    click(809, 599)

    print("🔁 กด next รัว 3 วิ...")
    end = time.time() + 16
    while time.time() < end:
        click(744, 853, delay=0.1)

    print("🚀 เริ่ม spam ตำแหน่ง (670, 637) เป็นเวลา 5 วินาที...")
    end = time.time() + 3
    while time.time() < end:
        if keyboard.is_pressed('left ctrl'):
            print("🛑 หยุดโดยผู้ใช้ (Left Ctrl)")
            exit()
        pyautogui.click(670, 637)
        time.sleep(0.1)
    log_action("✅ จบ spam")

    # --- ดำเนินการต่อ ---
    click(575, 834)  # collect
    time.sleep(1)    # wait 1 sec
    click(555, 834)     # collect again
    time.sleep(1)  
    click(358, 831)  # close
    time.sleep(1)  
    click(667, 858)  # scout
    time.sleep(1)  
    click(709, 547)  # move
    click(614, 717)  # 10 rolls
    click(572, 591)  # confirm

    # --- ลูป 8 ครั้ง ---
    for i in range(9):
        log_action(f"🔁 เริ่ม Loop #{i+1}")

        # → ก่อนย้ายไปตำแหน่งใหม่ รอ 1 วิ
        time.sleep(0.5)

        # 🔄 Spam (744, 853) 3 วิ
        end = time.time() + 3.5
        while time.time() < end:
            if keyboard.is_pressed('left ctrl'):
                print("🛑 หยุดโดยผู้ใช้ (Left Ctrl)")
                exit()
            pyautogui.click(744, 853)
            time.sleep(0.1)

        log_action("✅ กดรัว (744, 853) เสร็จแล้ว")
        time.sleep(0.5)

        # → ก่อนย้าย
        time.sleep(0.5)

        # ✅ คลิก (564, 845) ครั้งเดียว
        if keyboard.is_pressed('left ctrl'):
            print("🛑 หยุดโดยผู้ใช้ (Left Ctrl)")
            exit()
        pyautogui.click(564, 845)
        log_action("✅ คลิก (564, 845) ครั้งเดียว")
        time.sleep(0.5)

        # → ก่อนย้าย
        time.sleep(1)

        # ✅ คลิก (565, 590) ครั้งเดียว
        if keyboard.is_pressed('left ctrl'):
            print("🛑 หยุดโดยผู้ใช้ (Left Ctrl)")
            exit()
        pyautogui.click(565, 590)
        log_action("✅ คลิก (565, 590) ครั้งเดียว")
        time.sleep(0.5)

    click(744, 853)



    print("✅ จบโปรแกรมเรียบร้อย")

    print("✅ จบโปรแกรมเรียบร้อย")
    log_action("💤 รอการกดปุ่ม 'x' เพื่อเริ่มโปรแกรมใหม่...")

    # -------- [ โหมดรอ Restart ] --------
    while True:
        if keyboard.is_pressed('left ctrl'):
            print("🛑 หยุดโดยผู้ใช้ (Left Ctrl)")
            exit()

        if keyboard.is_pressed('x'):
            print("🔁 กำลังรีสตาร์ทโปรแกรม...")
            time.sleep(1)
            break  # ออกจาก while รอ → กลับไปเริ่มรอบใหม่
        time.sleep(0.2)  # ไม่โหลด CPU
