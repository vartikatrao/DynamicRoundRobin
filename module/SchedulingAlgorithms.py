from ProcessState import ProcessState

class SchedulingAlgorithms:
    processes = []
    ready_queues = []
    remaining_process = 0
    completed_processes = []
    current_time = 0
    n = 0
    run_time = 0
    temp_process = None
    gantt_chart = []
    delay = 0

    def __init__(self, processes):
        self.processes = processes
        self.ready_queues = []
        self.completed_processes = []
        self.current_time = 0
        self.n = len(processes)
        self.remaining_process = self.n
        self.run_time = 0
        self.temp_process = None
        self.gantt_chart = []
        self.delay = 0
        self.processes.sort(key=lambda x: x.getArriveTime())

    # setter
    def addProcesses(self, process):
        if isinstance(process, list):
            for p in process:
                self.processes.append(p)
        elif isinstance(process, object):
            self.processes.append(process)

    # getter
    def getN(self):
        return self.n

    def getProcesses(self):
        return self.processes

    def getCompletedProcesses(self):
        if not self.completed_processes:
            return self.processes
        else:
            return self.completed_processes
    
    def getCurrentTime(self):
        return self.current_time

    def getGanttChart(self):
        return self.gantt_chart
    def setReadyQueues(self):
        # Add new processes to the ready queue
        for process in self.processes:
            if process.getArriveTime() > self.current_time:
                break

            if not process.getIsQueued() and not process.getIsCompleted() and process.getArriveTime() <= self.current_time:
                process.setState(ProcessState.READY)
                process.setIsQueued(True)
                self.ready_queues.append(process)
            
    def getRunningProcess(self):
        if self.ready_queues[0].getState() == ProcessState.READY:
            process = self.ready_queues.pop(0)
            process.setState(ProcessState.RUNNING)

            if process.getStartTime() is None:
                process.setStartTime(self.current_time)

            return process
        
        return None
    
    def setCompletedProcess(self, process):

        process.setFinishTime(self.current_time)

        process.setTurnaroundTime()

        process.setWaitingTime()

        process.setResponseTime()

        process.setState(ProcessState.EXIT)
        process.setIsCompleted(True)
        process.setIsQueued(False)

        self.completed_processes.append(process)
        self.processes.remove(process)

        self.remaining_process -= 1

    # check delay
    def checkDelay(self):
        if self.delay:
            self.gantt_chart.append(['##', self.delay]) 
            self.delay = 0

    def executeNonPreemptive(self, process):
        self.checkDelay()

        self.current_time += process.getBurstTime() 
        process.setBurstTimeRemaining(0) 

        if process.getBurstTimeRemaining() == 0:
            self.gantt_chart.append([process.getName(),
                                    process.getBurstTime()])
            self.setCompletedProcess(process)

    def executePreemptive(self, process):
        self.checkDelay()

        if process != self.temp_process:
            if self.temp_process and not self.temp_process.getIsCompleted():
                self.gantt_chart.append([self.temp_process.getName(), 
                                            self.run_time])
                self.run_time = 0
            self.temp_process = process
        self.run_time += 1

        self.current_time += 1
        process.setBurstTimeRemaining(process.getBurstTimeRemaining() - 1)

        if process.getBurstTimeRemaining() == 0:
            self.gantt_chart.append([process.getName(),
                                    self.run_time])
            self.temp_process = process
            self.run_time = 0

            self.setCompletedProcess(process)

        elif process.getState() == ProcessState.RUNNING:
            process.setState(ProcessState.READY)
            self.ready_queues.append(process)
