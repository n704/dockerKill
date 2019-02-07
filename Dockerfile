FROM ubuntu:16.04
# Install Python.
RUN \
  apt-get update && \
  apt-get install -y python python-dev && \
  rm -rf /var/lib/apt/lists/*
COPY entrypoint.sh /
COPY app.py /
CMD ["./entrypoint.sh"]