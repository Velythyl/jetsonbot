FROM arm64v8/python:3.7
WORKDIR /project

RUN apt-get update && apt-get install -y ffmpeg mencoder && apt-get clean && \
    rm -r /var/lib/apt/lists/*


RUN pip install -U pip && rm -rf /root/.cache

RUN apt-get install python-opencv

COPY requirements.txt requirements-base.txt
RUN pip install -r requirements-base.txt && rm -rf /root/.cache

RUN pip freeze | tee /pip-freeze.txt
RUN pip list | tee /pip-list.txt

ENV DISABLE_CONTRACTS 1