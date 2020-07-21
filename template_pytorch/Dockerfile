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

#RUN apt-get update && \
#    apt-get install python3-pip libopenblas-base libopenmpi-dev libjpeg-dev zlib1g-dev openmpi-bin openmpi-common -y && \
#    pip3 install Cython
#RUN wget https://nvidia.box.com/shared/static/3ibazbiwtkl181n95n9em3wtrca7tdzp.whl -O torch-1.5.0-cp37-cp37m-linux_aarch64.whl
#RUN wget https://github.com/pytorch/vision/archive/v0.6.0.zip -O torchvision.zip && unzip torchvision.zip

ENV DISABLE_CONTRACTS=1

ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/jetson_libs

RUN echo $LD_LIBRARY_PATH

#RUN python -c "import solution; import wrappers; import model"

# let's see what you've got there...
CMD python solution.py