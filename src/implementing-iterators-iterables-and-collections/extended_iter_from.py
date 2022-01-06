"""Extended iter usage"""


"""
read lines in file until END is present
"""
import time
with open("end_terminated_file.txt", "rt") as f:
    lines = iter(lambda: f.readline().strip(), "END")
    readings = [int(line) for line in lines]
    print(readings)

"""
Timestamp iterator (never stops as datetime never evaluates to None)
"""
import datetime
timestamps = iter(datetime.datetime.now, None)
print(next(timestamps))
time.sleep(2)
print(next(timestamps))
time.sleep(1)

# just test how datetime can be used
print(datetime.datetime.now)
time.sleep(1)
print(datetime.datetime.now())

"""
Realtime data iterator (reading disk space with time)
"""
from pathlib import Path
cwd = Path.cwd()
print(cwd)

from shutil import disk_usage

def free_space():
    return disk_usage(cwd).free

free_space_readings = iter(free_space, None)
import time
# values from two iterators - free_disk_readings and previously created
# timestamps
GB = float(float(1024) ** 3) # 1,073,741,824
for timestamp, free_bytes in zip(timestamps, free_space_readings):
    print(timestamp, '{0:.2f} GB'.format(free_bytes / GB))
    time.sleep(1.0)