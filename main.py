import glob
import time
import sys
sys.path.append("module")

# import model
from Process import Process
from display import print_in_table, print_off_table, printGanttChart
from DRR import DRR
from RR import RR

def printInfo(processes, ganttChart=None):
    print_in_table(processes)
    print_off_table(processes)

    if ganttChart:
        printGanttChart(ganttChart)

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

        for line in data[0:-1]:
            values = line.strip().split()
            if len(values) == 4:
                name, arrival_time, burst_time, deadline = values
                processes.append(Process(name, int(arrival_time), int(burst_time), int(deadline)))
            
            else:
                pass

        quantum = int(data[-1].strip()) 
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
        rr = RR(processes, quantum)
        rr.run()
        processes = rr.getCompletedProcesses()


        # display information
        printInfo(processes, rr.getGanttChart())
        for process in processes:
                process.reset()

        print(30*'-')
        drr=DRR(processes)
        drr.run()
        processes=drr.getCompletedProcesses()
        print('-' * 35 + " DRR (Dynamic Round Robin) " + '-' * 35)
        printInfo(processes, drr.getGanttChart())



