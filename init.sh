#!/bin/bash
until apt-get update; do sleep 2; done

function start_msg() {
    echo "$1 has started!"
}

function end_msg() {
    echo "$1 has ended successfully"
}

function setup_cameras() {
mkdir data && cd data
mkdir config && cd config
mkdir calibrations && cd calibrations
mkdir camera_extrinsic && cd camera_extrinsic && echo "homography: [-4.89775e-05, -0.0002150858, -0.1818273, 0.00099274, 1.202336e-06, -0.3280241, -0.0004281805, -0.007185673, 1]" > default.yaml
cd -
mkdir camera_intrinsic && cd camera_intrinsic && echo "image_width: 640
image_height: 480
camera_name: /porsche911/rosberrypi_cam
camera_matrix:
  rows: 3
  cols: 3
  data: [307.7379294605756, 0, 329.692367951685, 0, 314.9827773443905, 244.4605588877848, 0, 0, 1]
distortion_model: plumb_bob
distortion_coefficients:
  rows: 1
  cols: 5
  data: [-0.2565888993516047, 0.04481160508242147, -0.00505275149956019, 0.001308569367976665, 0]
rectification_matrix:
  rows: 3
  cols: 3
  data: [1, 0, 0, 0, 1, 0, 0, 0, 1]
projection_matrix:
  rows: 3
  cols: 4
  data: [210.1107940673828, 0, 327.2577820024981, 0, 0, 253.8408660888672, 239.9969353923052, 0, 0, 0, 1, 0]" > default.yaml
cd -
mkdir kinematics && cd kinematics && echo "baseline: 0.1
gain: 1.0
k: 27.0
limit: 1.0
radius: 0.0318
trim: 0.0" > default.yaml
echo "${FUNCNAME[0]} has run successfully"
true
}

#setup_cameras

function install_deps() {
apt install python3-pip -y
apt install python-pip -y
pip3 install cython
echo "${FUNCNAME[0]} has run successfully"
true
}

#install_deps

function docker_stuff() {
groupadd docker && usermod -aG docker $(logname) && newgrp docker
docker pull portainer/portainer
docker volume create portainer_data
docker run -d -p 9000:9000 -p 8000:8000 --name portainer --restart always -v/var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
mkdir -p /etc/systemd/system/docker.service.d
echo "[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H unix:// -H tcp://0.0.0.0:2375" > /etc/systemd/system/docker.service.d/options.conf
systemctl daemon-reload
systemctl restart docker
echo "${FUNCNAME[0]} has run successfully"
true
}

: '
#docker_stuff
start_msg "PIPELINE SETUP"
cd /usr/src/linux-headers-4.9.140-tegra-ubuntu18.04_aarch64/kernel-4.9
mkdir v4l2loopback
git clone https://github.com/umlaeute/v4l2loopback.git v4l2loopback
cd v4l2loopback
make
make install
depmod -a
apt-get install -y v4l2loopback-dkms v4l2loopback-utils
modprobe v4l2loopback devices=1 video_nr=2 exclusive_caps=1
echo options v4l2loopback devices=1 video_nr=2 exclusive_caps=1 > /etc/modprobe.d/v4l2loopback.conf
echo v4l2loopback > /etc/modules
update-initramfs -u
end_msg "PIPELINE SETUP"
'

#start_msg "PIPELINE SERVICE SETUP"
#echo -e "#! /bin/bash\n\ngst-launch-1.0 -v nvarguscamerasrc ! 'video/x-raw(memory:NVMM), format=NV12, width=1920, height=1080, framerate=30/1' ! nvvidconv ! 'video/x-raw, width=640, height=480, format=I420, framerate=30/1' ! videoconvert ! identity drop-allocation=1 ! 'video/x-raw, width=640, height=480, format=RGB, framerate=30/1' ! v4l2sink device=/dev/video2" > gstpipeline.sh
#chmod 777 gstpipeline.sh
#sudo -i echo -e "[Unit]\nDescription=GST Pipeline\nAfter=network.target\nStartLimitIntervalSec=0\n[Service]\nType=simple\nRestart=always\nRestartSec=1\nUser=$USER\nExecStart=/usr/bin/env /home/jetsonbot/gstpipeline.sh\n[Install]\nWantedBy=multi-user.target" > /etc/systemd/system/gstpipeline.service
#echo "Created service file. Restarting systemcl."
#systemctl start gstpipeline
#systemctl enable gstpipeline
#systemctl daemon-reload
#end_msg "PIPELINE SERVICE SETUP"

start_msg "DOCKER IMAGES SETUP"
apt install -y git git-lfs
pip3 install --no-cache-dir -U duckietown-shell
git clone https://github.com/carmen-sc/dt-duckiebot-interface.git
cd dt-duckiebot-interface
dts devel build -f
end_msg "DOCKER IMAGES SETUP"
