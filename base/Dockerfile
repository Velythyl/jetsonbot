FROM nvcr.io/nvidia/l4t-base:r32.3.1

WORKDIR /project

RUN apt-get update && apt-get install -y ffmpeg mencoder python3.6 git && apt-get clean && \
    rm -r /var/lib/apt/lists/*


RUN pip3 install -U pip && rm -rf /root/.cache

RUN git clone https://github.com/Velythyl/jetsonbot && cd

COPY requirements.txt requirements-base.txt
RUN pip3 install -r requirements-base.txt && rm -rf /root/.cache

RUN pip3 freeze | tee /pip3-freeze.txt
RUN pip3 list | tee /pip3-list.txt

ENV DISABLE_CONTRACTS 1