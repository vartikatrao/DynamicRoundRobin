from ProcessState import ProcessState
from SchedulingAlgorithms import SchedulingAlgorithms

# RR (Round Robin)
class RR(SchedulingAlgorithms):
    quantum = 0
    context_switch_count=-1
    def __init__(self, processes, quantum):
        super().__init__(processes)
        self.quantum = quantum

    def execute(self, process):

        # If the process has finished, terminate it
        if process.getBurstTimeRemaining() <= self.quantum:

            self.gantt_chart.append([process.getName(), 
                                    process.getBurstTimeRemaining()]) 
            self.current_time += process.getBurstTimeRemaining()
            self.setCompletedProcess(process)

        # If the process is still running, put it back in the ready queue
        elif process.getState() == ProcessState.RUNNING:

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
            
            process = self.getRunningProcess()
            self.context_switch_count+=1
            self.execute(process)

