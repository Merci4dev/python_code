import psutil
import time
import multiprocessing

class SystemInfo:
    def __init__(self):
        self.num_cpus = multiprocessing.cpu_count()
        self.memory_available = psutil.virtual_memory().available
        self.processes = psutil.cpu_percent(percpu=True)
    
    def get_num_cpus(self):
        return self.num_cpus
    
    def get_memory_available(self):
        return self.memory_available
    
    def get_network_interfaces(self):
        return psutil.net_if_addrs()
    
    def get_cpu_time(self):
        return psutil.cpu_times()
    
    def get_network_connections(self):
        return psutil.net_connections()
    
    def get_process_ids(self):
        return psutil.pids()
    
    def get_task_creation_speed(self):
        # Perform a sample task and measure the time
        start_time = time.time()

        # Realiza una tarea de ejemplo aquí, por ejemplo, un bucle simple
        for _ in range(10000):
            pass
        # Perform your task here
        end_time = time.time()
        
        # Calculate the task creation speed
        task_creation_speed = 1 / (end_time - start_time) 
        return task_creation_speed
    

# =============================================
# system_info = SystemInfo()
# num_cpus = system_info.get_num_cpus()
# memory_available = system_info.get_memory_available()
# network_interfaces = system_info.get_network_interfaces()
# cpu_time = system_info.get_cpu_time()
# network_connections = system_info.get_network_connections()
# process_ids = system_info.get_process_ids()
# task_creation_speed = system_info.get_task_creation_speed()

# print(num_cpus)
# print(memory_available)
# print(network_interfaces)
# print(cpu_time)
# print(network_connections)
# print(process_ids)
# print("Task Spead per seg:", task_creation_speed)