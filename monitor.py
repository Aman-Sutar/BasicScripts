import psutil

# Thresholds
CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 90

# CPU
cpu = psutil.cpu_percent(interval=1)
if cpu > CPU_LIMIT:
    print(f"[WARNING] CPU usage high: {cpu}%")
else:
    print(f"CPU usage OK: {cpu}%")

# Memory
memory = psutil.virtual_memory().percent
if memory > MEMORY_LIMIT:
    print(f"[WARNING] Memory usage high: {memory}%")
else:
    print(f"Memory usage OK: {memory}%")

# Disk
disk = psutil.disk_usage('/').percent
if disk > DISK_LIMIT:
    print(f"[WARNING] Disk usage high: {disk}%")
else:
    print(f"Disk usage OK: {disk}%")

# Top 5 processes by CPU
print("\nTop 5 processes by CPU usage:")
for proc in sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)[:5]:
    print(f"PID: {proc.info['pid']} | Name: {proc.info['name']} | CPU: {proc.info['cpu_percent']}%")
