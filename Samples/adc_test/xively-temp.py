# part of the python code is copied from page 82 of Getting Started with BeagleBone, by Matt Richardson
# Jingfeng Liu
# LinkSprite.com/pcDuino.com

from adc import analog_read
import time
import datetime
import xively
from requests import HTTPError

api =xively.XivelyAPIClient("APIKEY")
feed=api.feeds.get(FEEDID)


def delay(ms):
    time.sleep(1.0*ms/1000)

def setup():
		print "read channel ADC0 value ,the V-REF = 3.3V"
		delay(3000)

def loop():

    while True:
        value = analog_read(5)
	temp = value*(3.3/4096*100)
        print ("value =  %4d"%value)
	print ("temperature =  %4.3f  V" %temp)
	
        now=datetime.datetime.utcnow()
        feed.datastreams=[ xively.Datastream(id='office_temp', current_value=temp, at=now)
        ]

        try:
              feed.update()
              print "Value pushed to Xively: " +  str(temp)
        except HTTPError as e:
                         print "Error connecting to Xively: " + str (e)

        time.sleep(20) 

def main():
    setup()
    loop()

main()
