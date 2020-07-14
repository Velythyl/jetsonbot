FROM arm64v8/python:3
WORKDIR /project

RUN apt-get update && apt-get install -y ffmpeg mencoder && apt-get clean && \
    rm -r /var/lib/apt/lists/*


RUN pip install -U pip && rm -rf /root/.cache

# OPENCV
#RUN apt-get install python3-dev python3-pip python3-numpy
#RUN apt-get install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev  libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev protobuf-compiler libgflags-dev libgoogle-glog-dev libblas-dev libhdf5-serial-dev liblmdb-dev libleveldb-dev liblapack-dev libsnappy-dev libprotobuf-dev libopenblas-dev libgtk2.0-dev libboost-dev libboost-all-dev libeigen3-dev libatlas-base-dev libne10-10 libne10-dev
#RUN pip3 install neon
#RUN apt-get install libneon27-dev
#RUN apt-get install libneon27-gnutls-dev
#RUN wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.4.0.zip
#RUN unzip opencv-3.4.0.zip
#RUN wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.4.0.zip
#RUN unzip opencv_contrib-3.4.0.zip
#RUN cd opencv-3.4.0
#RUN mkdir build
#RUN cd build
#RUN cmake -D CMAKE_BUILD_TYPE=RELEASE -D ENABLE_NEON=ON -D ENABLE_TBB=ON -D ENABLE_IPP=ON -D ENABLE_VFVP3=ON -D WITH_OPENMP=ON -D WITH_CSTRIPES=ON -D WITH_OPENCL=ON -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=/root/$(whoami)/opencv_contrib-3.4.0/modules/ ..
#RUN make
#RUN make install
#RUN cd .. && cd ..

RUN pip install --upgrade pip && pip install wheel
RUN pip install opencv-python-aarch64

COPY requirements.txt requirements-base.txt
RUN pip install -r requirements-base.txt && rm -rf /root/.cache

RUN pip freeze | tee /pip-freeze.txt
RUN pip list | tee /pip-list.txt

ENV DISABLE_CONTRACTS 1