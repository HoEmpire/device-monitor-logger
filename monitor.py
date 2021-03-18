import GPUtil
import time
import psutil
file = open("log.txt","w")

time.sleep(1)
while(1):
    cpu_info = psutil.cpu_percent()
    GPUs = GPUtil.getGPUs()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " gpu: " + str(int(GPUs[0].load*100)*1.0) + "%, cpu: " + str(cpu_info) + "%")
    file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " +str(int(GPUs[0].load*100)*1.0) + " "+ str(cpu_info)+"\n")
    time.sleep(1)
file.close() 
