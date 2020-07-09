echo -e "#! /bin/bash\n\ngst-launch-1.0 -v nvarguscamerasrc ! 'video/x-raw(memory:NVMM), format=NV12, width=1920, height=1080, framerate=30/1' ! nvvidconv ! 'video/x-raw, width=640, height=480, format=I420, framerate=30/1' ! videoconvert ! identity drop-allocation=1 ! 'video/x-raw, width=640, height=480, format=RGB, framerate=30/1' ! v4l2sink device=/dev/video2" > gstpipeline.sh 

chmod 777 gstpipeline.sh

sudo -i

echo -e "[Unit]\nDescription=GST Pipeline\nAfter=network.target\nStartLimitIntervalSec=0\n[Service]\nType=simple\nRestart=always\nRestartSec=1\nUser=$USER\nExecStart=/usr/bin/env /home/jetsonbot/gstpipeline.sh\n[Install]\nWantedBy=multi-user.target" > /etc/systemd/system/gstpipeline.service

exit

systemctl start gstpipeline

systemctl enable gstpipeline
