from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
import serial

app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0',9600, timeout = 1)
ser.reset_input_buffer()


#if ser.in_waiting > 0:
    #if analog!="":
    #	lectura = analog
    #convert = float(analog)
        


@app.route('/')
def index():
	lectura = ser.readline().decode('utf-8').rstrip()
	print(lectura)
	templateData = {
		'lectura' : lectura
	}
	return render_template('index.html', **templateData)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
