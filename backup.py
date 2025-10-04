import shutil
import os
from datetime import datetime

# Paths
SOURCE_DIR = "/home/groot/ko/data"
BACKUP_DIR = "/home/groot/ko/backups"

# Create a timestamped backup folder
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
destination = os.path.join(BACKUP_DIR, f"backup_{timestamp}")

try:
    shutil.copytree(SOURCE_DIR, destination)
    print(f"[SUCCESS] Backup completed: {destination}")
except Exception as e:
    print(f"[ERROR] Backup failed: {e}")
