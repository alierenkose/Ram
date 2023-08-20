## @alierenkose


import os

def get_system_info():
    meminfo = {}
    with os.popen('wmic os get FreePhysicalMemory,TotalVisibleMemorySize /value') as regdata:
        for line in regdata:
            line = line.strip()
            if 'FreePhysicalMemory' in line:
                meminfo['FreePhysicalMemory'] = int(line.split('=')[-1])
            elif 'TotalVisibleMemorySize' in line:
                meminfo['TotalPhysicalMemory'] = int(line.split('=')[-1])
    return meminfo

system_info = get_system_info()

total_memory = system_info['TotalPhysicalMemory'] / 1024 / 1024
free_memory = system_info['FreePhysicalMemory'] / 1024 / 1024
used_memory = total_memory - free_memory
used_percent = used_memory / total_memory * 100

print('Total Memory: {} GB'.format(total_memory))
print('Free Memory: {} GB'.format(free_memory))
print('Used Memory: {} GB ({:.2f}%)'.format(used_memory, used_percent))

# https://github.com/alierenkose
## @alierenkose
### Amateur Pythonista
