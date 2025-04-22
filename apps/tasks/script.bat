@echo off
echo Task executed at: %DATE% %TIME% >> C:\Users\dhruv\Videos\Video_Extractor_Python_Files\ppt_creator\apps\logs\log_file.txt
rem Simulate a task running (use timeout instead of sleep)
timeout /t 5
echo Task completed at: %DATE% %TIME% >> C:\path\to\log_file.txt
