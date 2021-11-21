import time
import datetime
class Clock():
    def __init__(self,hours,minutes,seconds,type = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.type = type
    def __str__(self):
        if self.type == 0:
            return '{:02}:{:02}:{:02}'.format(self.hours,self.minutes,self.seconds)
        if self.type == 1:
            hour12 = self.hours-12 if self.hours > 12 else self.hours
            hour12 = 12 if self.hours == 0 else hour12
            ampm = 'am' if  self.hours < 12 else 'pm'
            return '{:02}:{:02}:{:02} {}'.format(hour12,self.minutes,self.seconds,ampm)
    def tick(self):
        if self.seconds == 59:
            if self.hours == 23:
                if self.minutes == 59:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
            elif self.minutes == 59:
                self.hours += 1
                self.minutes = 0
                self.seconds = 0
            else:
                self.minutes += 1
                self.seconds = 0
        else: 
            self.seconds += 1


if __name__ == '__main__':
    #hours = int(input('What is the current hour: '))
    #minutes = int(input('What is the current minute: '))
    #seconds = int(input('What is the current second: '))
    #getting current time
    timenow = str(datetime.datetime.now()).split(' ')
    hours = int(timenow[1][0:2])
    minutes = int(timenow[1][3:5])
    seconds = int(timenow[1][6:8])
    clock1 = Clock(hours,minutes,seconds,1)

    while True:
        print(clock1)
        clock1.tick()
        time.sleep(1)
