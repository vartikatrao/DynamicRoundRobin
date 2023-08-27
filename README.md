# Dynamic Round Robin with Priority Scheduling - A Novel CPU Scheduling Algorithm 

**Abstract:**
CPU scheduling algorithms play a vital role in optimizing system efficiency. Effective scheduling algorithms are crucial components of an operating system, ensuring stability and optimal performance. The Round Robin (RR) algorithm, though widely used, has limitations like high turnaround time, waiting time, and context switches. It lacks priority handling and deadline awareness, impacting time-sensitive tasks. To address these issues, we propose a novel CPU scheduling algorithm, combining RR, Priority Scheduling, and Dynamic Time Quantum. This algorithm aims to enhance RR's efficiency, prioritize time-sensitive tasks, and improve system performance.

**Keywords:** Round Robin, Dynamic Priority, Deadline, Dynamic Time Quantum, Waiting Time, Turn Around Time.

## Introduction

The CPU scheduling algorithm is a critical component of an operating system that manages CPU time allocation to processes. Efficient scheduling ensures optimal resource utilization and timely execution of processes. Turnaround time and waiting time are key metrics to evaluate scheduling effectiveness. Our project introduces a new scheduling algorithm, merging Round Robin and Priority Scheduling.

## Proposed Algorithm

1. Calculate priority: Priority = Deadline - Burst Time
2. Sort processes in the ready queue by priority and deadline.
3. Calculate quantum as the average of max and min remaining burst times.
4. While processes remain:
    a. Select highest-priority process.
    b. Execute process for quantum or till completion.
    c. If process completes, set state as EXIT.
    d. If remaining burst < ½ quantum, complete and set state as EXIT. Else, move to ready queue.
    e. Decrement priority of other processes.
    f. Calculate new quantum based on max and min burst times.

## Results

Our algorithm outperforms traditional Round Robin in turnaround time, waiting time, and throughput. It reduces context switches, executes tasks before deadlines, and prioritizes time-sensitive tasks. Incorporating Priority Scheduling and Dynamic Time Quantum calculation improves efficiency and resource utilization.

## Simulation

We implemented the algorithm in Python, using Matplotlib for result visualization. Simulations involved generating processes with varying priorities, burst times, and deadlines. The algorithm's performance was measured using metrics like turnaround time and waiting time. Matplotlib aided in graphical analysis.

## Future Optimization and Enhancements

Further enhancements are possible. Dynamic time quantum could be adjusted adaptively based on system dynamics. Machine learning techniques could optimize priority factors in real-time. Continuous research can fine-tune the algorithm for improvements.

## Conclusion

The proposed algorithm effectively combines Round Robin, Priority Scheduling, and Dynamic Time Quantum. Through simulations, it surpasses traditional Round Robin, exhibiting reduced turnaround time, waiting time, and context switches. By prioritizing tasks and adhering to deadlines, this algorithm offers enhanced system performance and reliability.

