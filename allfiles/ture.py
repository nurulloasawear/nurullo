import RPi.GPIO as GPIO
import time

# GPIO pinlarini sozlash
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
    while True:
        # GPIO pinini yuqori holatga o'tkazish (energiyani uzatish)
        GPIO.output(18, GPIO.HIGH)
        print("Signal yuborildi")
        time.sleep(1)  # 1 soniya davomida signal yuborish

        # GPIO pinini past holatga o'tkazish (energiyani uzatishni to'xtatish)
        GPIO.output(18, GPIO.LOW)
        print("Signal to'xtatildi")
        time.sleep(1)  # 1 soniya davomida signalni to'xtatish

except KeyboardInterrupt:
    print("Dastur to'xtatildi")

finally:
    GPIO.cleanup()
