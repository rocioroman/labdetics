from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
import serial

app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0',9600, timeout = 1)
ser.reset_input_buffer()
GPIO.setmode(GPIO.BCM)
pin_led = 18
pin_digital= 23
GPIO.setup(pin_digital,GPIO.IN)
GPIO.setup(pin_led,GPIO.OUT)
#GPIO.output(pin_led,GPIO.LOW)
#if ser.in_waiting > 0:
    #if analog!="":
    #	lectura = analog
    #convert = float(analog)
        


@app.route('/')
def index():
	lectura = ser.readline().decode('utf-8').rstrip()
	digital = GPIO.input(pin_digital)
	if digital == 1:
		digital_str = "Ruido detectado"
		GPIO.output(pin_led,GPIO.HIGH)
	else:
		digital_str = "No se detecta ruido" 
		GPIO.output(pin_led,GPIO.LOW)

	templateData = {
		'lectura' : lectura,
		'digital' : digital_str 
	}
	return render_template('index.html', **templateData)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
