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

# This is a weird arm64 container; installing the torch and torchvision throught requirements.txt doesn't work.
# We're also doing this install in a single layer to reduce image size. Excuse the messy code.
ENV FORCE_CUDA=1
RUN apt-get update && \
    apt-get install python3-pip libopenblas-base libopenmpi-dev libjpeg-dev zlib1g-dev openmpi-bin openmpi-common -y && \
    wget https://nvidia.box.com/shared/static/ncgzus5o23uck9i5oth2n8n06k340l6k.whl -O torch-1.4.0-cp36-cp36m-linux_aarch64.whl && \
    pip3 install Cython && pip3 install numpy && \
    pip3 install torch-1.4.0-cp36-cp36m-linux_aarch64.whl && \
    wget https://github.com/pytorch/vision/archive/v0.5.0.zip -O torchvision.zip && \
    unzip torchvision.zip && \
    cd vision-0.5.0 && \
    python3 setup.py install && \
    cd .. && \
    rm -rf torchvision.zip && rm -rf torch-1.4.0-cp36-cp36m-linux_aarch64.whl && rm -rf vision-0.5.0

RUN pip3 install Cython
RUN pip3 install torch-1.5.0-cp37-cp37m-linux_aarch64.whl

# let's copy all our solution files to our workspace
# if you have more file use the COPY command to move them to the workspace
COPY solution.py /workspace
COPY models /workspace/models
COPY model.py /workspace
COPY wrappers.py /workspace

# we make the workspace our working directory
WORKDIR /workspace

ENV DISABLE_CONTRACTS=1

RUN python3 -c "import solution; import wrappers; import model"

# let's see what you've got there...
CMD python3 solution.py