# Definition of Submission container

FROM velythyl/base:latest

# DO NOT MODIFY: your submission won't run if you do
RUN apt-get update -y && apt-get install -y --no-install-recommends \
         gcc \
         libc-dev\
         git \
         bzip2 \
         python-tk && \
     rm -rf /var/lib/apt/lists/*

# let's create our workspace, we don't want to clutter the container
RUN rm -rf /workspace; mkdir /workspace

# here, we install the requirements, some requirements come by default
# you can add more if you need to in requirements.txt
COPY requirements.txt /workspace
RUN pip3 install -r /workspace/requirements.txt

# let's copy all our solution files to our workspace
# if you have more file use the COPY command to move them to the workspace
COPY solution.py /workspace
COPY models /workspace/models
COPY model.py /workspace
COPY wrappers.py /workspace

# we make the workspace our working directory
WORKDIR /workspace

ENV DEBIAN_FRONTEND=noninteractive


#
# install prerequisites (many of these are for numpy)
#
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            python3-pip \
		  python3-dev \
		  libopenblas-dev \
		  libopenmpi \
            openmpi-bin \
            openmpi-common \
		  gfortran \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install setuptools Cython wheel
RUN pip3 install numpy --verbose

#
# PyTorch (for JetPack 4.4 DP)
#
#  PyTorch v1.2.0 https://nvidia.box.com/shared/static/lufbgr3xu2uha40cs9ryq1zn4kxsnogl.whl (torch-1.2.0-cp36-cp36m-linux_aarch64.whl)
#  PyTorch v1.3.0 https://nvidia.box.com/shared/static/017sci9z4a0xhtwrb4ps52frdfti9iw0.whl (torch-1.3.0-cp36-cp36m-linux_aarch64.whl)
#  PyTorch v1.4.0 https://nvidia.box.com/shared/static/c3d7vm4gcs9m728j6o5vjay2jdedqb55.whl (torch-1.4.0-cp36-cp36m-linux_aarch64.whl)
#  PyTorch v1.5.0 https://nvidia.box.com/shared/static/3ibazbiwtkl181n95n9em3wtrca7tdzp.whl (torch-1.5.0-cp36-cp36m-linux_aarch64.whl)
#
ARG PYTORCH_URL=https://nvidia.box.com/shared/static/lufbgr3xu2uha40cs9ryq1zn4kxsnogl.whl
ARG PYTORCH_WHL=torch-1.2.0-cp36-cp36m-linux_aarch64.whl

RUN wget --quiet --show-progress --progress=bar:force:noscroll --no-check-certificate ${PYTORCH_URL} -O ${PYTORCH_WHL} && \
    pip3 install ${PYTORCH_WHL} --verbose && \
    rm ${PYTORCH_WHL}


#
# torchvision 0.4
#
ARG TORCHVISION_VERSION=v0.4.0
ARG PILLOW_VERSION=pillow<7
ARG TORCH_CUDA_ARCH_LIST="5.3;6.2;7.2"

RUN printenv && echo "torchvision version = $TORCHVISION_VERSION" && echo "pillow version = $PILLOW_VERSION" && echo "TORCH_CUDA_ARCH_LIST = $TORCH_CUDA_ARCH_LIST"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  git \
		  build-essential \
            libjpeg-dev \
		  zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone -b ${TORCHVISION_VERSION} https://github.com/pytorch/vision torchvision && \
    cd torchvision && \
    python3 setup.py install && \
    cd ../ && \
    rm -rf torchvision && \
    pip3 install "${PILLOW_VERSION}"


#
# torchaudio
#
ARG TORCHAUDIO_VERSION

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
		  sox \
		  libsox-dev \
		  libsox-fmt-all \
    && rm -rf /var/lib/apt/lists/*

RUN git clone -b ${TORCHAUDIO_VERSION} https://github.com/pytorch/audio torchaudio && \
    cd torchaudio && \
    python3 setup.py install && \
    cd ../ && \
    rm -rf torchaudio


#
# PyCUDA
#
ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"
RUN echo "$PATH" && echo "$LD_LIBRARY_PATH"

RUN pip3 install pycuda --verbose

RUN exaq

# Torch & torchvision: https://forums.developer.nvidia.com/t/pytorch-for-jetson-nano-version-1-5-0-now-available/72048
RUN apt-get update && apt-get install python3-pip libopenblas-base libopenmpi-dev libjpeg-dev zlib1g-dev openmpi-bin -y
RUN wget https://nvidia.box.com/shared/static/yr6sjswn25z7oankw8zy1roow9cy5ur1.whl -O torch-1.6.0-cp37-cp37m-linux_aarch64.whl
RUN pip3 install Cython
RUN pip3 install torch-1.6.0-cp37-cp37m-linux_aarch64.whl
RUN git clone --branch release/0.7 https://github.com/pytorch/vision torchvision
WORKDIR torchvision
RUN find / lib | grep libmpi
RUN ln -s /usr/lib/aarch64-linux-gnu/libmpi_cxx.so.40 /usr/lib/aarch64-linux-gnu/libmpi_cxx.so.20 && \
    ln -s /usr/lib/aarch64-linux-gnu/libmpi.so.40 /usr/lib/aarch64-linux-gnu/libmpi.so.20
RUN python3 setup.py install
WORKDIR /workspace



ENV DISABLE_CONTRACTS=1

RUN python -c "import solution; import wrappers; import model"

# let's see what you've got there...
CMD python solution.py