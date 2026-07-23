import os 
import shutil

print("--- RUNNING LOCAL HARDWARE DIAGNOSTICS ---")

total, used, free = shutil.disk_usage("/")
free_gb = free // (2**30)
print(f"Available Disk space: {free_gb} GB")

process_count = len(os.popen("ps -ax").read().splitlines())
print(f"Active System Process: {process_count}")

if free_gb < 20:
    print("WARNING: system storage thresholds are completely healthy.")

else:
    print("STATUS: Storage thresholds are completely healthy.")

