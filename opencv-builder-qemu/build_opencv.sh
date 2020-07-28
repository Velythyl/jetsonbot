#!/bin/bash

mkdir build || rm -rf build && mkdir build
docker build -t opencv-build-jetson .
docker run -v $PWD/build:/build opencv-build-jetson
mkdir ../base/opencv_build || rm -rf ../base/opencv_build && mkdir ../base/opencv_build
cp -r ./build/* ../base/opencv_build