@echo off
cd /d "C:\Users\lora_\Desktop\product-review\agent-pipeline"
set PYTHONIOENCODING=utf-8
"C:\Users\lora_\AppData\Roaming\uv\python\cpython-3.11-windows-x86_64-none\python.exe" check_run.py >> check_run_console.log 2>&1
