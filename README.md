# jetsonbot
Fixing/cleaning/reproducing the Duckieracer PDF - util scripts and stuff

# Cant run agents??

This says the docker compose yamls are https://docs.duckietown.org/daffy/opmanual_duckiebot/out/setup_troubleshooting_docker.html 
basic, health, others, and core. Health doesn't matter here. So we gotta launch the other three.

We can find them here https://github.com/duckietown/duckietown-shell-commands/tree/daffy/init_sd_card/stacks

## Basic

only has portainer + dt-device-loader. Portainer is already ok. Let's add dt-device-loader to the docker launcher

# dts duckiebot evaluate

When done in a repo where the dockerfile is non trivial, it seems like the messages from dts write at the same stream as the docker's build script.
This makes it so it's very hard to see the progress of the build phase, leading one to belive the build phase aborted or is stuck etc.

I recommend either removing all dts messages until the build is done, or the operator can simply do a `dts challenges submit`, and use the image ID
created by that with `dts duckiebot evaluate --image <image>`. That way, one knows for sure the build succeeded or failed, and that the cause of error
isn't because the JN is too foreign to dts.

# CUDA inside the docker

https://github.com/Technica-Corporation/Tegra-Docker

Basically, by simply plugging all the files needed for CUDA into the docker, since the host is also aarch65, everything works fine!

NOTE: this is just in case we need it, because I found something much better https://github.com/NVIDIA/nvidia-docker/wiki/NVIDIA-Container-Runtime-on-Jetson

# Turns out that doing this ourselves is way too hard and unmaintainable

We'll have to flip the current scheme on its head: instead of doing the base, then the lib (torch/TF), then the submission,
we'll have to do lib, base, submission.

By simply using NVIDIA's lib images, we're saving ourselves a LOT of headaches https://ngc.nvidia.com/catalog/containers/nvidia:l4t-pytorch

https://github.com/NVIDIA/nvidia-docker/wiki/NVIDIA-Container-Runtime-on-Jetson

However, we could simply pull the `ml` image, meaning that we wouldn't have to maintain two templates. However, it'd also mean larger image sizes

NOTE: nope, the non-base images are of a JN version higher than ours. This is kind of undocumented, but this means they're completely incompatible. The build
goes well, but when we launch the dockers, it just fails.

# Syslog

/var/log/syslog grew to be VERY large in size over time. Mine was 8GB at some point, and I had trouble prototyping dockers because of a lack of space.

Doing a daily `sudo cat /dev/null > /var/log/syslog`, even though it's normally bad practice, might be useful here.

Also, /var/lib/docker/overlay2 grows to be very large. Doing a rm -rf and then restarting the entier docker stack might be pertinent.

# The current way of doing the dockers:

1. Start `FROM` nvidia's l4t-base's version mentionned in here https://github.com/NVIDIA/nvidia-docker/wiki/NVIDIA-Container-Runtime-on-Jetson
2. Build our own base upon it
3. Build torch on that
4. Compile on a qemu-enabled laptop with a dts challenges submit
5. Using the docker tag from step 4, run duckiebot evaluate natively