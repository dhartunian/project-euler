import numpy as np


class EulerDate:

    yeardict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    leapyeardict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self,day, month, year, dow):
        self.day = day
        self.month = month
        self.year = year
        self.dow = dow

    def isleapyear(self):
        if self.year % 100 == 0:
            return self.year % 400 == 0
        else:
            return self.year % 4 == 0

    def nextday(self):
        if self.isleapyear():
            ydict = self.leapyeardict
        else:
            ydict = self.yeardict
        if self.day == ydict[self.month]:
            if self.month == 12:
                self.year = self.year + 1
                self.month = 1
                self.day = 1
            else:
                self.month = self.month + 1 
                self.day = 1
        else:
            self.day = self.day + 1
        self.dow = (self.dow + 1) % 7

    def __str__(self):
        return '{}/{}/{}'.format(self.day, self.month, self.year)

my_date = EulerDate(1,1,1900,1)
counter = 0
while my_date.year < 2001:
    my_date.nextday()
    if my_date.dow == 0 and my_date.day == 1:
        counter = counter + 1
        print str(my_date)

