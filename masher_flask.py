#!/usr/bin/python
# 1) If temp hits target, turn off
# 2) If temp less than target, turn on
# 3) While loop to allow for warmup
# 4) Set a length of time to run at real temp (timedelta)

import time
import datetime
import yagmail
from temp_reader import readTempOnce
from outlet_control import turnOutletOn, turnOutletOff
from flask import Flask
from flask import render_template

app = Flask(__name__)

targetTemp = 150
allowedHighDifference = 3
allowedLowDifference = 1
timeLengthInMinutes = 30

onCode = '21811'
offCode = '21820'

@app.route('/')
def main():
    startTemp = readTempOnce()
    startTime = datetime.datetime.now()
    warmup()
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=timeLengthInMinutes)
    warmup()
    temp = readTempOnce()
    print 'temp is ' + str(temp)
    return render_template('temp.html', temp=temp)
    while datetime.datetime.now() < endTime:
        warmup()
    print str (timeLengthInMinutes) + ' minutes are up!'
    print 'We started at ' + str(startTime) + ' at ' + str(startTemp) + ' degrees.'

def warmup():
    print 'warming up...'
    temp = readTempOnce()
    if temp > targetTemp + allowedHighDifference:
        yagmail.SMTP('john@stotlers.com').send('john@stotlers.com', '[ALERT]The temp is too high!', 'The temp is currently ' + str(temp))
    print 'temp is ' + str(temp)
    while temp < targetTemp:
        turnOutletOn(onCode)
        temp = readTempOnce()
        print 'temp is ' + str(temp)
    print 'all warmed up.'
    turnOutletOff(offCode)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)