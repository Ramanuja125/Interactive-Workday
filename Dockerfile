FROM ubuntu:22.04

# Set non-interactive mode to suppress apt prompts
ENV DEBIAN_FRONTEND=noninteractive

# Create a working directory
WORKDIR /cse572

# Install tools, Percona Server with RocksDB, and Python3 with pip
RUN apt update && apt install -y git-all \
    curl gnupg2 lsb-release software-properties-common python3 python3-pip nano vim && \
    curl -O https://repo.percona.com/apt/percona-release_latest.generic_all.deb && \
    apt install -y ./percona-release_latest.generic_all.deb && \
    percona-release enable-only ps-84-lts release && \
    percona-release enable tools release && \
    apt update && \
    apt install -y percona-server-server percona-server-rocksdb && \
    apt clean

# Remove existing contents of /cse572 if any
RUN rm -rf /cse572/*

# Copy requirements.txt from the main branch repository
RUN git clone --branch main <you personal access token here>/Ramanuja125/CSE572_project.git /cse572

# Install Python libraries listed in the requirements.txt file
RUN pip3 install --no-cache-dir -r /cse572/requirements.txt

# Set permissions for the /cse572 directory
RUN chmod -R 777 /cse572/*

# Expose MySQL port
EXPOSE 3306

# Configure MySQL to run as root and allow MyRocks plugin
CMD ["mysqld_safe", "--user=root", "--plugin-load-add=ha_rocksdb.so"]

RUN python3 download_LLM.py

#CMD ["python3", "RAG.py"]
