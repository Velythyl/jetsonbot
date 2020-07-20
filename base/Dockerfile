FROM velythyl/opencv:latest

WORKDIR /project

RUN apt-get update && apt-get install -y ffmpeg mencoder && apt-get clean && \
    rm -r /var/lib/apt/lists/*

RUN pip3 install -U pip && pip3 install --upgrade pip setuptools wheel && rm -rf /root/.cache

RUN pip3 install numpy

COPY requirements.txt requirements-base.txt
RUN apt-get update && pip3 install -r requirements-base.txt && rm -rf /root/.cache

RUN pip3 freeze | tee /pip3-freeze.txt
RUN pip3 list | tee /pip3-list.txt

ENV DISABLE_CONTRACTS 1