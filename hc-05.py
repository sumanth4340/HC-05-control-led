
import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO
import serial
from time import sleep
led2="P9_30"
led1="P9_15"
led="P9_12"
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
UART.setup("UART4")
hc = serial.Serial('/dev/ttyO4',9600)
hc.close()
while(1):
        hc.open()
        data=hc.readline()
        print data
        value=round(int(data)*2.5)
        print value
        if value==3.0:
                GPIO.output(led1,GPIO.LOW)
                GPIO.output(led2,GPIO.LOW)
                GPIO.output(led,GPIO.HIGH)
        elif value==0.0:
                GPIO.output(led2,GPIO.LOW)
                GPIO.output(led,GPIO.LOW)
                GPIO.output(led1,GPIO.HIGH)
        elif value==5.0:
                GPIO.output(led,GPIO.LOW)
                GPIO.output(led1,GPIO.LOW)
                GPIO.output(led2,GPIO.HIGH)


        elif value==8.0:
                for i in range(0,10):
                        GPIO.output(led1,GPIO.HIGH)
                        sleep(.1)
                        GPIO.output(led1,GPIO.LOW)
                        sleep(.1)
                        GPIO.output(led,GPIO.HIGH)
                        sleep(.1)
                        GPIO.output(led,GPIO.LOW)
                        sleep(.1)
                        GPIO.output(led2,GPIO.HIGH)
                        sleep(.1)
                        GPIO.output(led2,GPIO.LOW)
                        sleep(.1)
        elif value==10.0:
                for i in range(0,10):
                         GPIO.output(led,GPIO.HIGH)
                        GPIO.output(led2,GPIO.HIGH)
                        GPIO.output(led1,GPIO.LOW)
                        sleep(.1)
                        GPIO.output(led,GPIO.LOW)
                        GPIO.output(led2,GPIO.LOW)
                        GPIO.output(led1,GPIO.HIGH)
                        sleep(.1)
        elif value==13.0:
                for i in range(0,10):
                        GPIO.output(led,GPIO.HIGH)
                        GPIO.output(led1,GPIO.HIGH)
                        GPIO.output(led2,GPIO.HIGH)

GPIO.cleanup()

