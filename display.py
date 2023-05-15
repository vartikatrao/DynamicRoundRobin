from Table import Table

def print_in_table(processes):
    if processes[0].getStartTime():
        processes = sorted(processes, key=lambda p: p.getStartTime())
    # else:

    #     processes = sorted(processes, key=lambda p: p.getArriveTime())

    # set data to list of dictionary
    dictProcesses = []
    for process in processes:
        dictProcesses.append(process.getDict())

    # create and display process with table
    table = Table()
    table.addData(dictProcesses)
    table.display()

def print_off_table(processes, context_switch_count):
    n = len(processes)

    total_time = 0
    for process in processes:
        if total_time < process.getFinishTime():
            total_time = process.getFinishTime()

    #  troughput
    total_time+=context_switch_count
    throughput = total_time / n
    # Calculate average metrics
    avg_start_time = sum(p.getStartTime() for p in processes) / n
    avg_turnaround_time = sum(p.getTurnaroundTime() for p in processes) / n
    avg_waiting_time = sum(p.getWaitingTime() for p in processes) / n
    avg_response_time = sum(p.getResponseTime() for p in processes) / n
    
    avg_metrics=[avg_turnaround_time,avg_waiting_time,context_switch_count]
    # output
    print("Average Start Time        : {:.2f}".format(avg_start_time))
    print("Average Turnaround Time   : {:.2f}".format(avg_turnaround_time))
    print("Average Waiting Time      : {:.2f}".format(avg_waiting_time))
    print("Average Response Time     : {:.2f}".format(avg_response_time))
    print("No. of Context Switches   : ",context_switch_count)
    print("Assuming that each context switch takes 1s")
    print("Total time taken          : {:.2f} seconds".format(total_time))
    print()
    
    return avg_metrics

    # # gantt chart
    # gantt_chart()

# print gantt chart
def printGanttChart(ganttChart):
    
    if ganttChart is None:
        print("Gantt chart is empty")
        return

    print("Gantt Chart:")

    # create border horizontal
    border = ' '
    for process in ganttChart:
        border += '__' * process[1] + ' '

    # create process label
    label = '|'
    for process in ganttChart:
        space = '_' * (process[1]-1)
        label += space + process[0] + space + '|'

    # display
    print(border)
    print(label)

    time = 0
    # create list to store intervals for each process
    print(time, end="")
    for process in ganttChart:
        print('  ' * (process[1]), end='')
        time += process[1]

        if time > 9:
            print("\b", end="")
            
        print(time, end="")

    print()

"""
Gantt chart
 ____ __ ____ ____ ____ ____ ____ ____ ____ __ __ ____ __
|_P1_|P2|_P1_|_P0_|_P4_|_P3_|_P0_|_P5_|_P4_|P3|P0|_P4_|P4|
0    2  3    5    7    9   11   13   15   17 18 19   21 22

"""