import GPUtil
import time
import psutil

file = open("log.txt", "w")

time.sleep(1)
# read_mb_pre = psutil.disk_io_counters().read_bytes / 1024 / 1024
# read_mb_pre = psutil.disk_io_counters().read_time
write_mb_pre = psutil.disk_io_counters().write_bytes / 1024 / 1024

while (1):
    time_pre = time.time()
    cpu_info = psutil.cpu_percent()
    GPUs = GPUtil.getGPUs()
    # read_mb_cur = psutil.disk_io_counters().read_bytes / 1024 / 1024
    read_mb_cur = psutil.disk_io_counters().read_time
    write_mb_cur = psutil.disk_io_counters().write_bytes / 1024 / 1024
    print(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " gpu: " +
        str(int(GPUs[0].load * 100) * 1.0) + "%, cpu: " + str(cpu_info) +
        "%, GPU mem: " + str(round(GPUs[0].memoryUtil * 11, 1)) + "GB, RAM: " +
        str(round(psutil.virtual_memory().percent * 64 / 100, 1)) +
        "GB, write speed: " +
        # str(round(read_mb_cur - read_mb_pre, 1)) + "mb/s, write speed: " +
        str(round(write_mb_cur - write_mb_pre, 1)) + "mb/s")
    file.write(
        time.strftime("%Y-%m-%d:%H.%M.%S", time.localtime()) + " " +
        str(int(GPUs[0].load * 100) * 1.0) + " " + str(cpu_info) + " " +
        str(round(GPUs[0].memoryUtil * 11, 1)) + " " +
        str(round(psutil.virtual_memory().percent * 64 /100, 1)) + " " +
        # str(round(read_mb_cur - read_mb_pre, 1)) + " " +
        str(round(write_mb_cur - write_mb_pre, 1)) + "\n")
    # read_mb_pre = read_mb_cur
    write_mb_pre = write_mb_cur
    time.sleep(time_pre+1-time.time())
file.close()
