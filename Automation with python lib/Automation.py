import psutil, datetime, time , schedule , openpyxl, os

pid = (int(input("Enter the PID of the process you want to monitor: ")))

def warning():
    cpuUsage = psutil.cpu_percent(interval=1, percpu=True)
    for i in cpuUsage:
      if i > 50:
        print("WARNING: CPU usage is over 50%")
        print("CPU usage is: ", i)
        print("Time: ", datetime.datetime.now())
        print("\n")
      memusage = psutil.virtual_memory()
      if memusage.percent > 50:
        print("WARNING: Memory usage is over 50%")
        print("Memory usage is: ", memusage.percent)
        print("Time: ", datetime.datetime.now())
        print("\n")
      diskusage = psutil.disk_usage('/')
      if diskusage.percent > 50:
        print("WARNING: Disk usage is over 50%")
        print("Disk usage is: ", diskusage.percent)
        print("Time: ", datetime.datetime.now())
        print("\n")

def monitor():
  p = psutil.Process(pid)
  cpu = p.cpu_percent(interval=1)/psutil.cpu_count()

  mem = p.memory_full_info().rss/(1024*1024)
  memory = p.memory_percent()

  # path will be a CSV file 
  path = os.path.join(os.getcwd(), "monitor.csv")
  # if the file does not exist, create it, otherwise append to it
  if not os.path.exists(path):
    with open(path, "w") as f:
      f.write("Time, CPU Usage, Memory Usage\n")
  with open(path, "a") as f:
    f.write(str(datetime.datetime.now()) + "," + str(cpu) + "," + str(mem) + "\n")

schedule.every(1).seconds.do(monitor) # updated every 1 second
schedule.every(5).seconds.do(warning) #Warning is checked every 5 seconds

while True:
  schedule.run_pending()
  time.sleep(1)