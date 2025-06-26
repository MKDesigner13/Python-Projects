"""
The class will be called Timer. 
Its constructor accepts three arguments representing hours (a value from range [0..23]), minutes (from range [0..59]) and seconds (from range [0..59]).
"""

class Timer:
    def __init__(self, hr, minute, sec):
        self.__hr = hr
        self.__minute = minute
        self.__sec = sec

    def __str__(self):
        #Set timer string in 00:00:00 format
        self.__timerStr = "{:02}".format(self.__hr) + ":" + "{:02}".format(self.__minute) + ":" + "{:02}".format(self.__sec)
        return self.__timerStr

    def next_second(self):
        #Add second
        self.__sec += 1
        
        #Check if total seconds is over 59, if so set seconds to 0 and add 1 to total minutes
        if self.__sec > 59:
            self.__sec -= 60
            self.__minute += 1

            #Check if total minutes is over 59, if so set minutes to 0 and add 1 to total hours
            if self.__minute > 59:
                self.__minute -= 60
                self.__hr += 1

    def prev_second(self):
        #Subtract second
        self.__sec -= 1

        #Check if total seconds is under 0, if so set seconds to 59 and subtract 1 from total minutes
        if self.__sec < 0:
            self.__sec += 60
            self.__minute -= 1

            #Check if total minutes is under 0, if so set minutes to 59 and subtract 1 from total hours
            if self.__minute < 0:
                self.__minute += 60
                self.__hr -= 1



timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
