import Jetson.GPIO as GPIO
import time

# ========================
# CONFIGURABLE PARAMETERS
# ========================
FAN_PIN = 7              # GPIO pin using BOARD numbering
TEMP_THRESHOLD = 35.0    # [C] - temperature to turn on fan
SLEEP_INTERVAL = 10       # seconds between checks
# ========================

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(FAN_PIN, GPIO.OUT)

def get_cpu_temp():
    try:
        with open("/sys/devices/virtual/thermal/thermal_zone1/temp", "r") as f:
            temp_str = f.readline()
        return float(temp_str) / 1000.0
    except:
        return None

try:
    while True:
        temp = get_cpu_temp()
        if temp is not None:
            GPIO.output(FAN_PIN, GPIO.HIGH if temp > TEMP_THRESHOLD else GPIO.LOW)
        time.sleep(SLEEP_INTERVAL)

finally:
    GPIO.output(FAN_PIN, GPIO.LOW)
    GPIO.cleanup()

