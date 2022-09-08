import RPi.GPIO as GPIO

from time import sleep
import time
import csv
import pandas as pd
import DHT11
import masterstat

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

switches = []
fanHi = 0.005
fanLo = 0.005
purgePump = 0.005
pump = 0.005
temp = 75
overrideTime = 2.5 #hours
setTemp = 75

def updateConfig():
    configData = pd.read_csv('config.csv',index_col=0,skiprows=25,header=None,usecols=[0,1],names=['name','setting'])
    scheduleData = pd.read_csv('config.csv',index_col=0,nrows=24,header=0)
    print(configData)
    # print(scheduleData)

    totalOn = sum(switches)
    remainingTime = 0.887-totalOn*0.005
    for x in range(3):
        GPIO.output(8,1)
        sleep(0.031)
        GPIO.output(8,0)
        sleep(0.002)
        GPIO.output(8,1)
        sleep(0.011)
        GPIO.output(8,0)
        sleep(0.002)
        GPIO.output(8,1)
        sleep(0.011)
        GPIO.output(8,0)
        sleep(0.002)
        GPIO.output(8,1)
        sleep(0.011)
        GPIO.output(8,0)
        sleep(0.002)
        GPIO.output(8,1)
        sleep(0.011)
        GPIO.output(8,0)
        sleep(0.002)
        GPIO.output(8,1)
        sleep(fanHi+0.005*switches[1])
        GPIO.output(8,0)
        sleep(0.002)
        GPIO.output(8,1)
        sleep(fanLo+0.005*switches[2])
        GPIO.output(8,0)
        sleep(0.002)
        GPIO.output(8,1)
        sleep(purgePump+0.005*switches[3])
        GPIO.output(8,0)
        sleep(0.002)
        GPIO.output(8,1)
        sleep(pump+0.005*switches[4])
        GPIO.output(8,0)
        sleep(remainingTime)

def overrideTemp(newTemp,overrideTime):
    global SetTemp
    overrideExpire = time.time()+overrideTime*3600
    setTemp = newTemp

updateConfig()

#while True:

    # sleep(30)