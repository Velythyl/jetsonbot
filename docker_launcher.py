import subprocess
import sys
from time import sleep

dockers_to_run = ["duckietown/dt-duckiebot-interface:daffy-arm32v7", "duckietown/dt-car-interface:daffy-arm32v7", "--gpus all duckietown/dt-core:daffy-arm32v7"]

processes = []
for docker in dockers_to_run:
    command = "docker run --net=host -v /home/jetsonbot/data:/data --privileged --device=/dev/vchiq:/dev/vchiq "+docker

    processes.append(subprocess.Popen(command.split(" "), universal_newlines=True))

while True:
    for i, process in enumerate(processes):
        if process.poll() is None:
            print(f"DOCKER LAUNCHER REPORT: process '{' '.join(dockers_to_run[i].split(' ')[1:])}' has died. ", file=sys.stderr)
    sleep(10)
