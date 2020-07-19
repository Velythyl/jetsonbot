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

# Torch & torchvision: https://forums.developer.nvidia.com/t/pytorch-for-jetson-nano-version-1-5-0-now-available/72048
RUN apt-get update && apt-get install python3-pip libopenblas-base libopenmpi-dev libjpeg-dev zlib1g-dev openmpi-bin -y
RUN wget https://nvidia.box.com/shared/static/yr6sjswn25z7oankw8zy1roow9cy5ur1.whl -O torch-1.6.0-cp37-cp37m-linux_aarch64.whl
RUN pip3 install Cython
RUN pip3 install torch-1.6.0-cp37-cp37m-linux_aarch64.whl
RUN git clone --branch release/0.7 https://github.com/pytorch/vision torchvision
WORKDIR torchvision
RUN apt-get update && apt-get install libopenmpi-dev openmpi-bin -y && python3 setup.py install
WORKDIR /workspace



ENV DISABLE_CONTRACTS=1

RUN python -c "import solution; import wrappers; import model"

# let's see what you've got there...
CMD python solution.py