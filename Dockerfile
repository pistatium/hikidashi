FROM python:3.6-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
      libpq-dev \
      gcc \
      make \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

COPY requirements.txt /opt/hikidashi/
WORKDIR  /opt/hikidashi

RUN pip install -r requirements.txt

COPY src /opt/hikidashi/src
COPY setup.py /opt/hikidashi/

RUN ["/bin/bash", "-c", "pip install -e . && pip install .[server]"]

ENV AWS_DEFAULT_REGION=ap-northeast-1

EXPOSE 8000

CMD ["/bin/bash", "-c", "uwsgi --http 0.0.0.0:8000 -L -w hikidashi.wsgi:app --enable-threads"]
