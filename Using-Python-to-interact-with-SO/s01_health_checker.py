"""
Veficación del rendimiento del equipo
"""
import shutil
import psutil

def check_disk_usage(disk):
    '''Indica si el disco tiene más del 20% de almacenamiento libre'''
    d_usage = shutil.disk_usage(disk)
    free = d_usage.free / d_usage.total * 100
    return free > 20

def check_cpu_usage():
    '''Indica si se está utilizando menos del 75% del procesador'''
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")
