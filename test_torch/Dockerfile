FROM nvcr.io/nvidia/l4t-base:r32.3.1

RUN apt-get update && apt-get install python3-pip libopenblas-base libopenmpi-dev libjpeg-dev zlib1g-dev openmpi-bin openmpi-common -y
RUN wget https://nvidia.box.com/shared/static/ncgzus5o23uck9i5oth2n8n06k340l6k.whl -O torch-1.4.0-cp36-cp36m-linux_aarch64.whl
RUN pip3 install Cython && pip3 install numpy
RUN pip3 install torch-1.4.0-cp36-cp36m-linux_aarch64.whl
