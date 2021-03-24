import sys
import matplotlib.pyplot as plt
import numpy as np
report_file = open("report.txt", "r")
file = open(sys.argv[1],"r")
figure_count = 0



oneline = file.readline().split()
report_line = report_file.readline().split()

while(len(report_line)!=0):
    time = []
    gpu = []
    cpu = []
    gpum = []
    ram = []
    ws = []
    t_now = 0
    start_time = report_line[0]
    end_time = report_line[2]    

    while(oneline[0]!=start_time):
        oneline = file.readline().split()
    while(len(oneline)!=0 and oneline[0]!=end_time):
        time.append(t_now)
        gpu.append(float(oneline[1]))
        cpu.append(float(oneline[2]))
        gpum.append(float(oneline[3]))
        ram.append(float(oneline[4]))
        ws.append(float(oneline[5]))
    
        oneline = file.readline().split()
        t_now+=1
    plt.figure(figure_count)
    plt.plot(time,cpu,'r')
    plt.plot(time,gpu,'b')
    plt.xlabel('time / sec')
    plt.ylabel('Util / %')
    plt.legend(['CPU','GPU'])
    plt.title(report_line[3].replace("-"," "))
    figure_count += 1

    plt.figure(figure_count)
    plt.plot(time,ram,'r')
    plt.plot(time,gpum,'b')
    plt.xlabel('time / sec')
    plt.ylabel('Used / GB')
    plt.legend(['RAM','GPU memory'])
    plt.title(report_line[3].replace("-"," "))
    figure_count += 1

    plt.figure(figure_count)
    plt.plot(time,ws,'b')
    plt.xlabel('time / sec')
    plt.ylabel('Speed / MB/sec')
    plt.legend(['Disk Writing Speed'])
    plt.title(report_line[3].replace("-"," "))
    figure_count += 1

    if(len(cpu)!=0 and len(gpu)!=0):
        cpu_array = np.array(cpu)
        gpu_array = np.array(gpu)
        print("average cpu: %.1f" % cpu_array.mean())
        print("average gpu: %.1f" % gpu_array.mean())
        print("max cpu: %.1f" % cpu_array.max())
        print("max gpu: %.1f" % gpu_array.max())
        print(" \n")
    
    report_line = report_file.readline().split()
    if(figure_count % 3 == 0):
        plt.show()

file.close()
report_file.close()
plt.show()
