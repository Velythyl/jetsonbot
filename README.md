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

# Building for arm64v8

For me, `dts devel build -a arm64v8` didn't work. It exited with exit code 125 (and, weirdly, told me that docker tag had to be lowercase; but changing the name of the repo everywhere I could see didn't matter. I think it bases itself off of git?)

It also said my arg `ARCH=<...>` wasn't consumed. Meaning, the docker isn't compatible at all with building for another arch.

The two files 

So we'll be enabling building for `arm64` ourselves: 

```
export DOCKER_CLI_EXPERIMENTAL=enabled
docker buildx version # should return a correct version; verifies that buildx is enabled

```

# CUDA inside the docker

https://github.com/Technica-Corporation/Tegra-Docker

Basically, by simply plugging all the files needed for CUDA into the docker, since the host is also aarch65, everything works fine!

# Pytorch inside the docker

Well. This is awkward. We can't use CUDA inside a docker because we're on ARM64, so we're hacking it up at runtime. But to install torchvision, we need CUDA at install time.

We're doing the following: create the docker image with a `docker build`. Then, make the docker run a script that installs torch during a `docker run`.

Then, use `docker commit`. Tada! Torch installed.

# Turns out that doing this ourselves is way too hard and unmaintainable

We'll have to flip the current scheme on its head: instead of doing the base, then the lib (torch/TF), then the submission,
we'll have to do lib, base, submission.

By simply using NVIDIA's lib images, we're saving ourselves a LOT of headaches https://ngc.nvidia.com/catalog/containers/nvidia:l4t-pytorch

https://github.com/NVIDIA/nvidia-docker/wiki/NVIDIA-Container-Runtime-on-Jetson

However, we could simply pull the `ml` image, meaning that we wouldn't have to maintain two templates. However, it'd also mean larger image sizes