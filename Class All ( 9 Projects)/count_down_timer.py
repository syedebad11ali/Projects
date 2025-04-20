import winsound
import keyboard as k
import time as t
try:
    user=int(input("How many seconds do you want to count down from: "))
    while user <= 0:
        print("Please enter a number greater than 0.")
        user=int(input("How many seconds do you want to count down from: "))

    while user > 0:
        minutes = user // 60
        seconds = user % 60
        print(f"Countdown: {minutes:02d}:{seconds:02d}")
        if k.is_pressed("p"):
             print("⏸ Paused. Press 'r' to resume")
        while not k.is_pressed("r"):
             t.sleep(0.1)
        print("Resumed")
        t.sleep(1)
        user=user-1
except ValueError as e:
    print(f"Error:{e}")
for _ in range(3):
        winsound.Beep(1000, 500)
        t.sleep(0.3)

input("Press Enter to exit...")
print(" Time is UP!!")