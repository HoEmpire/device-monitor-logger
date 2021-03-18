import matplotlib.pyplot as plt
file = open("log.txt","r")
time = []
gpu = []
cpu = []
t_now = 0
oneline = file.readline().split()
start_time = input("input start time:")
end_time = input("input start time:")
while(oneline[1]!=start_time):
    oneline = file.readline().split()
while(len(oneline)!=0 and oneline[1]!=end_time):
    time.append(t_now)
    gpu.append(float(oneline[2]))
    cpu.append(float(oneline[3]))
    oneline = file.readline().split()
    t_now+=1
plt.plot(time,cpu,'r')
plt.plot(time,gpu,'b')
plt.xlabel('time / sec')
plt.ylabel('Util / %')
plt.legend(['cpu','gpu'])
plt.show()
