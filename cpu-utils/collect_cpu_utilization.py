import subprocess
import sys
import socket
import os,time,sys,signal

hostname = socket.gethostname()

def collect_system_info():
    print("OS INFO")
    kernal_version=subprocess.check_output('uname -r',shell=True)
    linux_version=subprocess.check_output('cat /etc/redhad-release',shell=True)

    print(f'kernal_version = {kernal_version.decode()}')
    print(f'linux_version = {linux_version.decode()}')

def collect_cpu_info():
    print("CPU INFO")
    cpu_core=subprocess.check_output("lscpu |grep 'core(s) per socket' |awk '{print $4}'",shell=True)
    cpu_speed=subprocess.check_output("lscpu |grep 'CPU MHz' |awk '{print $3}'",shell=True)
    cpu_count=subprocess.check_output("lscpu |grep 'Socket' |awk '{print $2}'",shell=True)
    cpu_model=subprocess.check_output("lscpu |grep 'Model Name' |cut -d ':' -f2 |sed 's/^[ \t]*//'",shell=True)

    print(f'CPU_CORES = {cpu_core.decode()}')
    print(f'CPU_SPEED = {cpu_speed.decode()}')
    print(f'CPU_COUNT = {cpu_count.decode()}')
    print(f'CPU_MODEL = {cpu_model.decode()}')


def collect_cpu_stats():
    print(f'Checking CPU and Memory Utilization on {hostname}')
    for _ in range(3):
        cpu_memory=subprocess.check_output("cat /proc/meminfo | grep Mem",shell=True)
        cpu_memory_perct=int(float(subprocess.check_output("free -m |grep Mem | awk '{ print ($3/$2)*100; }'",shell=True)))
        cpu_utilization=int(float(subprocess.check_output("top -bn2 | grep '%Cpu' | tail -n 1 | awk '{print 100 - $8}'",shell=True)))
        
        if cpu_memory_perct > 15 or cpu_utilization > 15: #currnet threshold set to 75%
            print(f'Waiting for 1 minute and then rechecking... (MEMORY and CPU UTILIZATION on {hostname})')
            time.sleep(60)
        else:
            break

    print(f'CPU_MEMORY:\{cpu_memory.decode()}')
    print(f'CPU_MEMORY_USED = {cpu_memory_perct}%')
    print(f'CPU_UTILIZATION = {cpu_utilization}%')

    if cpu_memory_perct > 75: #currnet threshold set to 75%
        print("Alert # MEMORY UTILIZATION ALERT FOR THE SERVER : "+hostname)
    
    if cpu_utilization > 75: #currnet threshold set to 75%
        print("Alert!! CPU UTILIZAITON ALERT FOR THE SERVER"+hostname)
        
        
    


def cpu_stats():
    
    cpu_utilization=int(float(subprocess.check_output("top -bn2 | grep '%Cpu' | tail -n 1 | awk '{print 100 - $8}'",shell=True)))

    print(f'CPU_UTILIZATION = {cpu_utilization}%')

    if cpu_utilization > 15: #currnet threshold set to 75%
        print("WARNING!! CPUT UTILIZAITON ALERT FOR THE SERVER"+hostname)

def main():
    collect_cpu_info()
    collect_cpu_stats()

if __name__ =='__main__':
    main()