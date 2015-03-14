from flask import Flask, render_template
from adc import analog_read
import datetime  

app = Flask(__name__)

#temperature = 2
#brightness = 3
#humidity =4

@app.route('/')
def now_time():
		now = datetime.datetime.now()
		timeString = now.strftime("%Y/%m/%d  %H:%M:%S")
		return  "Time :%s " % timeString

@app.route('/temperature')
def temp():
		temp = analog_read(2)
		return  "Temperature :%d " % temp

@app.route('/brightness')
def brig():
		brig = analog_read(3)
		return  "Brightness : %d " % brig

@app.route('/humidity')
def humi():
		humi = analog_read(4)
		return  "humi : %d " % humi

if __name__ == "__main__" :
	app.run (host='0.0.0.0',port=80,debug=True)  