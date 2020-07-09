import argparse
import signal
import subprocess
import sys
from time import sleep


def list_of_str(string):
    return map(float, string.replace("[").replace("]").split(","))


def signal_handler(sig, frame):
    handle_exit()


signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dockers", type=list_of_str)
parser = parser.parse_args()

dockers_to_run = [
                     "duckietown/dt-duckiebot-interface:daffy-arm32v7",
                     "duckietown/dt-car-interface:daffy-arm32v7",
                     "--gpus all duckietown/dt-core:daffy-arm32v7"
                 ] + parser.dockers


def cleanup_docker_name(string):
    return string.split(" ")[-1]


print(f"Dockers to run, sequentially: {', '.join(map(cleanup_docker_name, dockers_to_run))}")

processes = []
for docker in dockers_to_run:
    command = "docker run --net=host -v /home/jetsonbot/data:/data --privileged --device=/dev/vchiq:/dev/vchiq " + docker

    processes.append(subprocess.Popen(command.split(" "), universal_newlines=True))

    print(f"Started '{cleanup_docker_name(docker)}'.")


def handle_exit():
    for docker in dockers_to_run:
        try:
            print(subprocess.check_output(("docker kill " + cleanup_docker_name(docker)).split(" "),
                                          universal_newlines=True))
        except Exception as e:
            print(e)
    exit()


while True:
    for i, process in enumerate(processes):
        if process.poll() is not None:
            print(
                f"DOCKER LAUNCHER REPORT: process '{cleanup_docker_name(dockers_to_run[i])}' has died. \nExiting now.",
                file=sys.stderr)
            break
    sleep(10)
