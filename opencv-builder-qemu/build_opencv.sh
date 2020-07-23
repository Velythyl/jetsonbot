#!/bin/bash

mkdir build || rm -rf build && mkdir build
docker build -t opencv-build-jetson .
docker run -v $PWD/build:/build opencv-build-jetson