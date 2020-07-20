import psutil

for process in psutil.process_iter(['username', 'name', 'pid']):
    print(process.info)
