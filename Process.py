from ProcessState import ProcessState

# create Process class for store data simulation
class Process:
    __name = ""
    __burst_time = None
    __arrive_time = None
    __deadline = None
    __priority = None
    __state = None
    __start_time = None
    __finish_time = None
    __turnaround_time = None
    __waiting_time = None
    __response_time = None
    __burst_time_remaining = None
    __isQueued = False
    __isCompleted = False

    # constructor
    def __init__(self, name, arrive_time, burst_time, deadline=None):
        self.__name = name
        self.__burst_time = burst_time
        self.__arrive_time = arrive_time
        self.__deadline=deadline
        self.__priority = deadline-burst_time
        self.__state = ProcessState.NEW
        self.__start_time = None
        self.__finish_time = None
        self.__turnaround_time = None
        self.__waiting_time = None
        self.__response_time = None
        self.__burst_time_remaining = burst_time
        self.__isQueued = False
        self.__isCompleted = False

    # resetting before going to next algo
    def reset(self):
        self.__state = ProcessState.NEW
        self.__start_time = None
        self.__finish_time = None
        self.__turnaround_time = None
        self.__waiting_time = None
        self.__response_time = None
        self.__burst_time_remaining = self.__burst_time
        self.__deadline=None
        self.__isQueued = False
        self.__isCompleted = False

    # setter 
    def setName(self, name):
        self.__name = name

    def setArriveTime(self, arrive_time):
        self.__arrive_time = arrive_time

    def setBurstTime(self, burst_time):
        self.__burst_time = burst_time
    
    def setDeadline(self, deadline):
        self.__deadline=deadline

    def setPriority(self, priority):
        self.__priority = priority

    def setState(self, state):
        self.__state = state

    # getter
    def getName(self):
        return self.__name

    def getArriveTime(self):
        return self.__arrive_time
    
    def getBurstTime(self):
        return self.__burst_time
    
    def getDeadline(self): 
        return self.__deadline
    
    def getPriority(self):
        return self.__priority
    
    def getState(self):
        return self.__state
    
    def getStateValue(self):
        return self.__state.value
    
    # setter
    def setStartTime(self, start_time):
        self.__start_time = start_time

    def getStartTime(self):
        return self.__start_time
        
    # setter 
    def setFinishTime(self, finish_time):
        self.__finish_time = finish_time

    def getFinishTime(self):
        return self.__finish_time
        
    # setter 
    def setTurnaroundTime(self, time=None):
        if time is None:
            self.__turnaround_time = self.__finish_time - self.__arrive_time
        else:
            self.__turnaround_time = time
    

    def getTurnaroundTime(self):
        return self.__turnaround_time
    
    # setter 
    def setWaitingTime(self, time=None):
        if time is None:
            self.__waiting_time = self.__turnaround_time - self.__burst_time
        else:
            self.__waiting_time = time
    
    def getWaitingTime(self):
        return self.__waiting_time
    
    # setter 
    def setBurstTimeRemaining(self, time):
        self.__burst_time_remaining = time

    def getBurstTimeRemaining(self):
        return self.__burst_time_remaining

    def setResponseTime(self, time=None):
        if time is None:
            self.__response_time = self.__start_time - self.__arrive_time
        else:
            self.__response_time = time

    def getResponseTime(self):
        return self.__response_time
    
    # setter 
    def setIsQueued(self, isQueued):
        self.__isQueued = isQueued

    def getIsQueued(self):
        return self.__isQueued
    
    # setter 
    def setIsCompleted(self, isCompleted):
        self.__isCompleted = isCompleted

    def getIsCompleted(self):
        return self.__isCompleted

  
    def getDict(self):
        dict = {
            'Name': self.__name,
            'Arrive_T': self.__arrive_time,
            'Burst_T': self.__burst_time,
            'Deadline': self.__deadline,
            'Start_T': self.__start_time,
            'Finish_T': self.__finish_time,
            'Turnaround_T': self.__turnaround_time,
            'Waiting_T': self.__waiting_time,
            'Response_T': self.__response_time
        }

        keys_to_remove = [k for k, v in dict.items() if v is None]
        for key in keys_to_remove:
            dict.pop(key)

        return dict