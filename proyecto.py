import RPi.GPIO as GPIO
import time
import serial

ser = serial.Serial('/dev/ttyUSB0',9600, timeout = 1)

GPIO.setmode(GPIO.BCM)

# Distance Sensor
digital_pin =  17 #Escribir el pin del echo
GPIO.setup(digital_pin, GPIO.IN)
time.sleep(1)

# LED
led_pin = 23 #Escribir el pin del LED
GPIO.setup(led_pin, GPIO.OUT)

limite = 500

while True:
    if ser.in_waiting > 0:
        analog = ser.readline().decode('utf-8').rstrip()
        print(analog)
    # ver que tipo de salida da analog para dps compararlo con el limite
    # LED
    if analog<limite:
        GPIO.output(led_pin, False)
    else:
        GPIO.output(led_pin, True)
    time.sleep(0.2)