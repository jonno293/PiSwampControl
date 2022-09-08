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

def updateConfig(): #config.csv contains temp schedule and other settings
    configData = pd.read_csv('config.csv',index_col=0,skiprows=25,header=None,usecols=[0,1],names=['name','setting'])
    scheduleData = pd.read_csv('config.csv',index_col=0,nrows=24,header=0)
    print(configData)
    # print(scheduleData)


def overrideTemp(newTemp,overrideTime):
    global SetTemp
    overrideExpire = time.time()+overrideTime*3600
    setTemp = newTemp

updateConfig()

#while True:

    # sleep(30)
