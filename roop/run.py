#!/usr/bin/env python3

from roop import core

# customise
import subprocess

if __name__ == '__main__':
    print('ok')
    core.run()
    # Execute the command to close the command prompt replace face
    close_cmd = "taskkill /f /im cmd.exe"
    subprocess.run(close_cmd, shell=True)
    