import numpy as np
import matplotlib.pyplot as plt
import glob
import time
import sys
sys.path.append("module")

barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))

RR_list=[]
DRR_list=[]
 
from Process import Process
from display import print_in_table, print_off_table, printGanttChart
from DRR import DRR
from RR import RR

def printInfo(processes, context_switch_count, ganttChart=None):
    print_in_table(processes)
    avg_metrics=print_off_table(processes,context_switch_count)

    if ganttChart:
        printGanttChart(ganttChart)
    return avg_metrics
# MAIN PROGRAM 
txt_files = glob.glob("test-case/*.txt")

schedulingAlgorithms = ["DRR (Dynamic Round Robin)",
                        "RR (Round Robin)"
                        ]

# Display
print()
print('-' * 35 + " Simulation Scheduling Algorithm " + '-' * 35, end="\n\n")

# SIMULATION
while True:
    
    print("Select input type:")
    print("1. Manual")
    print("2. Import test case")
    print("0. Exit")
    print('=' * 30)
    print("Enter number:")
    choice = int(input("-> "))
    print('-' * 10, end="\n\n")

    processes = []
    if choice == 1:
        # manual input
        n = int(input("Enter how many process: "))
        for i in range(n):
            arrive_time = int(input("Enter Arrive Time: "))
            burst_time = int(input("Enter Burst Time : "))
            deadline=int(input("Enter Deadline Time : "))
            processes.append(Process("P"+str(i), arrive_time, burst_time, deadline))

    elif choice == 2:
        """ data.txt
        2
        P0 3 5 2
        P1 0 4 3
        3
        """

        print("Select file .txt:")
        for i, file in enumerate(txt_files):
            print(f"{i+1}. {file}")
        print('=' * 30)
        print("Warning! Make sure the data is in the correct format.")
        print("Enter number:")
        choice = int(input("-> "))
        print('-' * 10, end="\n\n")

        if choice <= len(txt_files):
            filename = txt_files[choice-1]
        else:
            print("[!]> Invalid choice <[!]", end="\n\n")
            continue

        # import test case (read)
        with open(filename, 'r') as f:
            data = f.readlines()

        for line in data:
                    # Skip empty or whitespace-only lines
                    if not line.strip():
                        continue

                    values = line.strip().split()
                    if len(values) == 4:
                        name, arrival_time, burst_time, deadline = values
                        processes.append(Process(name, int(arrival_time), int(burst_time), int(deadline)))
                    else:
                        pass

        
        n = len(processes) 

    elif choice == 0:
        break

    else:
        print("[!]> Invalid choice <[!]", end="\n\n")
        continue

    if processes:

        print("Input Process:")
        print_in_table(processes)
        # process RR (Round Robin) 
        print('-' * 35 + " RR (Round Robin) " + '-' * 35)

        set_quantum = input("Set quantum: ")
        
        if set_quantum:
            quantum = int(set_quantum)
        else:
             print("Quantum not set")
             sys.exit(0)
        rr = RR(processes, quantum)
        rr.run()
        processes = rr.getCompletedProcesses()


        # display information
        RR_list=printInfo(processes,rr.getContextSwitchCount(), rr.getGanttChart())
        for process in processes:
                process.reset()

        print(30*'-')
        drr=DRR(processes)
        drr.run()
        processes=drr.getCompletedProcesses()
        print('-' * 35 + " DRR (Dynamic Round Robin) " + '-' * 35)
        DRR_list=printInfo(processes, drr.getContextSwitchCount(), drr.getGanttChart())

        br1 = np.arange(len(RR_list))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        # Make the plot
        plt.bar(br1, RR_list, color ='c', width = barWidth,
                edgecolor ='grey', label ='RR')
        plt.bar(br2, DRR_list, color ='black', width = barWidth,
                edgecolor ='grey', label ='DRR')
        plt.xlabel('Metrics', fontweight ='bold', fontsize = 15)
        plt.ylabel('Time', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(RR_list))],
                ['Turn Around Time', 'Waiting Time', 'Context Switches'])
        plt.legend()
        plt.show()






