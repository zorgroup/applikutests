# Use Python 3.11.10 as the base image
FROM python:3.11.10-bullseye

# Use Bash as the default shell
SHELL ["/bin/bash", "-c"]

# Set environment variables
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 0

# Install basic utilities and libraries
RUN apt-get update && apt-get install -y \
    wget \
    nano \
    python3-pip \
    gettext \
    chrpath \
    libssl-dev \
    libxft-dev \
    libfreetype6 \
    libfreetype6-dev \
    libfontconfig1 \
    libfontconfig1-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip && pip install --upgrade setuptools

# Set the working directory inside the container
WORKDIR /code/

# Copy the requirements file and install dependencies
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the entire current directory to the container
COPY ./ /code/

# Add a non-root user for security
RUN useradd -ms /bin/bash code
USER code

# Set the command to run the Python script
CMD ["python", "app.py"]
