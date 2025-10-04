# 🛡️ Linux System Utilities – System Monitor & Backup Scripts

This repository contains two lightweight Python scripts developed to fulfill specific Linux system administration tasks:

1. **System Health Monitoring Script**  
2. **Automated Directory Backup Script**

---

## 📌 Problem Statements

### 1. System Health Monitoring

Monitor and report on:

- CPU usage  
- Memory usage  
- Disk space usage  
- Top 5 CPU-consuming processes  

Alerts are printed to the console if any usage crosses defined thresholds.

### 2. Automated Backup

Creates a timestamped backup of a specified local directory using Python’s `shutil` module. It logs the success or failure of the operation to the console.

---

## 📂 File Structure
```
.  
├── monitor.py         – System Health Monitoring Script  
├── backup.py          – Automated Backup Script  
└── README.md          – Project README
```
---

## 🛠️ Requirements

- Python 3.x  
- [psutil](https://pypi.org/project/psutil/) library (used in `monitor.py`)

### Install required package:
```
pip install psutil
```
---

## 🚀 How to Use

### 🧠 System Health Monitoring

**File:** `monitor.py`  
Run:

python3 monitor.py

This script checks:

- CPU usage (threshold: 80%)  
- Memory usage (threshold: 80%)  
- Disk usage (threshold: 90%)  
- Top 5 CPU-consuming processes

**Sample Output:**
```
CPU usage OK: 23.4%  
Memory usage OK: 57.1%  
Disk usage OK: 69.2%

Top 5 processes by CPU usage:  
PID: 1234 | Name: chrome | CPU: 45.0%  
PID: 5678 | Name: python3 | CPU: 20.0%  
...
```

---

### 💾 Directory Backup

**File:** `backup.py`  
Run:

python3 backup.py

This script:

- Copies the contents of `/home/user/test/data`  
- Saves the backup to `/home/user/test/backups/backup_<timestamp>`  
- Prints success or error messages

**Sample Output:**

[SUCCESS] Backup completed: /home/user/test/backups/backup_20251004_214530

> You can modify `SOURCE_DIR` and `BACKUP_DIR` in the script as needed.

---


