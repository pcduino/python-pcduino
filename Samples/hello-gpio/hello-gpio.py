from flask import Flask, render_template
import datetime  
import gpio

app = Flask(__name__)

channel = { 0:'gpio0', 1:'gpio1', 2:'gpio2', 3:'gpio3', 4:'gpio4', 
			5:'gpio5', 6:'gpio6', 7:'gpio7', 8:'gpio8', 9:'gpio9', 
			10:'gpio10', 11:'gpio11', 12:'gpio12', 13:'gpio13'
		     }
  
@app.route("/")
def hello():

	now = datetime.datetime.now()
	timeString = now.strftime("%Y/%m/%d  %H:%M:%S")
	templateData = {
			'title':'HELLO!',
			'time':timeString
			}
	return render_template('main.html',**templateData)

@app.route("/readpin/<pin>")
def readPin(pin):
		
		gpio.pinMode(channel[int(pin)],gpio.INPUT)
		value  = " "

		if  (gpio.digitalRead(channel[int(pin)]) == gpio.HIGH)  :
			value = "Read GPIO" + pin + " is high !"
		else :
			value = "Read GPIO" + pin +" is low !"
		templateData = {
					'title' : 'Status of GPIO' + pin ,
					'value' : value
							}
		return render_template('pin.html',**templateData)

if __name__ == "__main__" :
	app.run (host='0.0.0.0',port=80,debug=True)  