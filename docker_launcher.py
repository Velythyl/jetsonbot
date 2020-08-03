import argparse
import random
import signal
import subprocess
import sys
from time import sleep

# TODO split out the output of the dockers into separate log files, i guess?

def list_of_str(string):
    string = string.replace("[").replace("]")
    listed = string.split(",")
    return map(float, listed)


def signal_handler(sig, frame):
    handle_exit()

def cleanup_docker_name(string):
    return string.split(" ")[-1]

def handle_exit():
    for i, docker in enumerate(genned_names):
        docker_command = cleanup_docker_name(dockers_to_run[i])

        try:
            print(subprocess.check_output(("docker stop "+docker).split(" "),
                                          universal_newlines=True), end="")
            print(f"Successfully stopped '{docker_command}'")
        except Exception as e:
            print("Trying to kill instead")
            try:
                print(subprocess.check_output(("docker kill "+docker).split(" "),
                                              universal_newlines=True))
                print(f"Successfully killed '{docker_command}'")
            except Exception as e:
                print(f"You will have to kill '{docker}' yourself")

    for pipe in pipes:
        pipe.close()
    exit()

genned_names = []
def gen_name(docker):
    global genned_names

    name = cleanup_docker_name(docker).replace("/", "-").replace(":", "-")
    genned_names.append(name)
    return name




signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dockers", default=[], type=list_of_str)
parser = parser.parse_args()

dockers_to_run = [   "-v /var/run/docker.sock:/var/run/docker.sock -v /var/local:/var/local duckietown/dt-device-loader:daffy-arm32v7",
                     "velythyl/dt-duckiebot-interface:latest",
                     "duckietown/dt-car-interface:daffy-arm32v7",
                     "--gpus all duckietown/dt-core:daffy-arm32v7",
                     "duckietown/dt-rosbridge-websocket:daffy-arm32v7",
                     "duckietown/rpi-simple-server:master18"
                 ] + parser.dockers


print(f"Dockers to run, sequentially: {', '.join(map(cleanup_docker_name, dockers_to_run))}")

processes = []
pipes = []
for docker in dockers_to_run:
    command = f"docker run --net=host -v /home/jetsonbot/data:/data --privileged --device=/dev/vchiq:/dev/vchiq --name {gen_name(docker)} {docker}"

    pipes.append(open(cleanup_docker_name(docker).split("/")[-1]+".log", "w"))

    processes.append(subprocess.Popen(command.split(" "), universal_newlines=True, stdout=pipes[-1], stderr=pipes[-1]))

    print(f"Started '{cleanup_docker_name(docker)}'.")

    sleep(60)   # timing issues https://answers.ros.org/question/310848/run_id-on-parameter-server-does-not-match-declared-run_id/


def fake_func():
    while True:
        for i, process in enumerate(processes):
            if process.poll() is not None:
                print(
                    f"DOCKER LAUNCHER REPORT: process '{cleanup_docker_name(dockers_to_run[i])}' has died. \nExiting now.",
                    )
                return
        sleep(10)


fake_func()
handle_exit()
