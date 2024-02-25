 
import serial
import time
import RPi.GPIO as GPIO
 
ser = serial.Serial('/dev/ttyACM0', 9600)
 
 ser.flushInput()
  while True:
   try:
        
        lineBytes = ser.readline()
 
        line = lineBytes.decode('utf-8')
       
       
        pieces =line.split("\t")
        #print(pieces)
        humidity = pieces[0]
        temperature = pieces[1]
 
        #print(type(humidity))
        #print(pieces[0])
        #print(pieces[1])
        #print(temprature)
 
        pieces2 = temperature.split(":")
        pieces1 = humidity.split(":")
 
        humidity_c = float(pieces1[1])
        temp_c = float(pieces2[1])
 
        #print(pieces1[1])
        #print(type(pieces[1]))
        #print(type(humidity_c))
        print("my temprature is" , temp_c)
        print("my humidity is" , humidity_c)
       
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        tempHI = 40
        tempLOW = 30
        humiHI = 40
        humiLOW = 30
        if (temp_c) > tempHI:
            GPIO.output(21, GPIO.HIGH) #turn GPIO pin 21 on
        elif (temp_c) < tempHI:
            GPIO.output(21, GPIO.LOW)
        time.sleep(1)
       
        if (temp_c) < tempLOW:
            GPIO.output(16, GPIO.HIGH)
        elif (temp_c) > tempLOW:
            GPIO.output(16, GPIO.LOW)
        time.sleep(1)
       
       
        
        if (humidity_c) > humiHI:
            GPIO.output(26, GPIO.HIGH) #turn GPIO pin 21 on
        elif (humidity_c) < humiHI:
            GPIO.output(26, GPIO.LOW)
        time.sleep(1)
        if (humidity_c) < humiLOW:
            GPIO.output(20, GPIO.HIGH) #Turn GPIO pin 21 off
        elif (humidity_c) > humiLOW:
            GPIO.output(20,GPIO.LOW)
        time.sleep(1)
 
    except KeyboardInterrupt:
        break # stop the while loop