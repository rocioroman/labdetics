import RPi.GPIO as GPIO
import time
import serial

ser = serial.Serial('/dev/ttyACM0',9600, timeout = 1)
ser.reset_input_buffer()
GPIO.setmode(GPIO.BCM)


# LED
led_pin_red = 18 #Escribir el pin del LED
led_pin_yellow = 23
GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_yellow,GPIO.OUT)
limite_y = 3.0
limite_r = 5


while True:
    if ser.in_waiting > 0:
       analog = ser.readline().decode('utf-8').rstrip()
       if analog!="":
        print("Voltaje es",analog)
        convert = float(analog)
        if convert>limite_y:
           print("Amarillo")
           GPIO.output(led_pin_yellow, GPIO.LOW)
    time.sleep(0.2)
