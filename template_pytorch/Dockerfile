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

WORKDIR /workspace

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

#ADD jetson_libs /jetson_libs
#RUN cp -r /jetson_libs/. /usr/lib/aarch64-linux-gnu/

# we make the workspace our working directory
WORKDIR /workspace

ENV DISABLE_CONTRACTS=1
#ENV LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/lib:/jetson_libs:/usr/lib/aarch64-linux-gnu:/usr/lib/aarch64-linux-gnu/openmpi/
#RUN python -c "import solution; import wrappers; import model"

# let's see what you've got there...
CMD python3 solution.py