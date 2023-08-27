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
![image](https://github.com/vartikatrao/DynamicRoundRobin/assets/100116788/d2f2bed5-0680-4c3e-ade1-94e032889cfa)

## Results

Our algorithm outperforms traditional Round Robin in turnaround time, waiting time, and throughput. It reduces context switches, executes tasks before deadlines, and prioritizes time-sensitive tasks. Incorporating Priority Scheduling and Dynamic Time Quantum calculation improves efficiency and resource utilization.
<br> ![image](https://github.com/vartikatrao/DynamicRoundRobin/assets/100116788/59127475-350d-478f-a4f0-83d0ded5ad09)
![image](https://github.com/vartikatrao/DynamicRoundRobin/assets/100116788/57af1f86-3280-48ca-857e-667f943236b0)
![image](https://github.com/vartikatrao/DynamicRoundRobin/assets/100116788/d078e32e-ab0b-4a13-bd75-21eeaf34b67a)

![image](https://github.com/vartikatrao/DynamicRoundRobin/assets/100116788/19f84912-d6de-44f2-a64b-8d11733499d0)

## Simulation

We implemented the algorithm in Python, using Matplotlib for result visualization. Simulations involved generating processes with varying priorities, burst times, and deadlines. The algorithm's performance was measured using metrics like turnaround time and waiting time. Matplotlib aided in graphical analysis.

## Future Optimization and Enhancements

Further enhancements are possible. Dynamic time quantum could be adjusted adaptively based on system dynamics. Machine learning techniques could optimize priority factors in real-time. Continuous research can fine-tune the algorithm for improvements.

## Conclusion

The proposed algorithm effectively combines Round Robin, Priority Scheduling, and Dynamic Time Quantum. Through simulations, it surpasses traditional Round Robin, exhibiting reduced turnaround time, waiting time, and context switches. By prioritizing tasks and adhering to deadlines, this algorithm offers enhanced system performance and reliability.

