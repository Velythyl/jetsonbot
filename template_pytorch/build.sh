#!/bin/bash

mount --bind /usr/lib/aarch64-linux-gnu ./jetson_libs
docker build -t template-pytorch .
docker run --device=/dev/nvhost-ctrl --device=/dev/nvhost-ctrl-gpu --device=/dev/nvhost-prof-gpu --device=/dev/nvmap --device=/dev/nvhost-gpu --device=/dev/nvhost-as-gpu -v /usr/lib/aarch64-linux-gnu/tegra:/usr/lib/aarch64-linux-gnu/tegra template-pytorch
umount ./jetson_libs
# TODO docker commit