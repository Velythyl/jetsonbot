FROM arm64v8/python:3.7

WORKDIR /project

RUN apt-get update && apt-get clean && \
    rm -r /var/lib/apt/lists/*

RUN pip3 install -U pip && rm -rf /root/.cache

RUN pip3 install numpy neon

# OPENCV
RUN apt-get update && apt-get install \
    python3-dev python3-pip python3-numpy build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev \
    libavformat-dev libswscale-dev  libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev \
    protobuf-compiler libgflags-dev libgoogle-glog-dev libblas-dev libhdf5-serial-dev liblmdb-dev libleveldb-dev \
    liblapack-dev libsnappy-dev libprotobuf-dev libopenblas-dev libgtk2.0-dev libboost-dev libboost-all-dev \
    libeigen3-dev libatlas-base-dev libne10-10 libne10-dev -y --no-install-recommends && \
    apt-get install libneon27-dev -y --no-install-recommends && \
    apt-get install libneon27-gnutls-dev -y --no-install-recommends

RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.2.zip && \
    unzip opencv.zip && \
    wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/4.1.2.zip && \
    unzip opencv_contrib.zip && \
    mkdir ./opencv-4.1.2/build && \
    cd ./opencv-4.1.2/build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D ENABLE_NEON=ON -D ENABLE_TBB=ON -D ENABLE_IPP=ON -D ENABLE_VFVP3=ON -D \
    WITH_OPENMP=ON -D WITH_CSTRIPES=ON -D WITH_OPENCL=ON -D CMAKE_INSTALL_PREFIX=/usr/local -D \
    OPENCV_EXTRA_MODULES_PATH=./../../opencv_contrib-4.1.2/modules/ .. && \
    make && \
    make install && \
    cd ../.. && \
    rm -rf opencv-4.1.2 && rm -rf opencv_contrib-4.1.2

ENV DISABLE_CONTRACTS 1