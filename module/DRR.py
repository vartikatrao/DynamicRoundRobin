from ProcessState import ProcessState
from SchedulingAlgorithms import SchedulingAlgorithms

# Dynamic Round Robin
class DRR(SchedulingAlgorithms):
    quantum = 0

    def __init__(self, processes):
        super().__init__(processes)
        self.ready_queues.sort(key=lambda x: (x.getPriority(), x.getDeadline()))

        self.quantum = (max(process.getBurstTimeRemaining() for process in processes) + 
                        min(process.getBurstTimeRemaining() for process in processes)) // 2

    def execute(self, process):

        # If the process is still running, put it back in the ready queue
        if process.getState() == ProcessState.RUNNING:

            if (process.getBurstTimeRemaining()<1.5*self.quantum):
                self.gantt_chart.append([process.getName(),process.getBurstTimeRemaining()])
                self.current_time += process.getBurstTimeRemaining()
                self.setCompletedProcess(process)

                
            else:
                process.setBurstTimeRemaining(process.getBurstTimeRemaining() - self.quantum)
                self.gantt_chart.append([process.getName(), 
                                        self.quantum]) 
                # Execute the process
                self.current_time += self.quantum

                if self.remaining_process != 0:
                    self.setReadyQueues()

                process.setState(ProcessState.READY)
                self.ready_queues.append(process)

    def run(self):
        self.setReadyQueues()

        while self.remaining_process:

            if not self.ready_queues:
                self.setReadyQueues()

                if not self.ready_queues:
                    self.current_time += 1
                    self.delay += 1
                    continue
            self.ready_queues.sort(key=lambda x: (x.getPriority(), x.getDeadline()))

            process = self.getRunningProcess()
            self.execute(process)
            
            for p in self.ready_queues: 
                if (self.remaining_process): 
                    if (process==p): continue
                    else: 
                        p.setPriority(p.getPriority()-self.quantum)

            # calculate new quantum value after every quantum of execution
            if (self.remaining_process):
                self.quantum = (max(process.getBurstTimeRemaining() for process in self.ready_queues) + 
                                    min(process.getBurstTimeRemaining() for process in self.ready_queues)) // 2
            

