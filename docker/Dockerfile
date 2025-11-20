# Start from official Ubuntu 22.04 Docker image
FROM pytorch/pytorch:latest

# Install
# OpenCV python needs libgl1-mesa-glx libglib2.0-0 libsm6 libxext6
RUN apt-get update && apt-get install -y \
    git \
    nano \
    bash-completion \
    python3-argcomplete \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install -U \
    numpy==1.26.4 \
    opencv-python==4.10.0.84 \
    scikit-image==0.24.0 \
    pytorch-model-summary==0.1.2 \
    vit-pytorch==1.8.8 \
    pandas==2.2.3 \
    matplotlib==3.9.2 \
    seaborn==0.13.2 \
    hyperopt \
    pybullet \
    tensorboard \
    opensimplex

WORKDIR /workspace

RUN git clone --recurse-submodules --shallow-submodules https://github.com/mbrummelhuis/ats-meta.git && \
    cd ats-meta && git submodule update --init --recursive
WORKDIR /workspace/ats-meta

# Install the packages
RUN pip3 install -e tactile_data \
    && pip3 install -e tactile_data_shear \
    && pip3 install -e tactile_servo_control \
    && pip3 install -e tactile_image_processing \
    && pip3 install -e tactile_learning \
    && pip3 install -e tactile_sim
RUN ls -a /workspace/ats-meta/tactile_servo_control/tactile_servo_control/learning

# Entrypoint
RUN echo "Hello"
COPY docker/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

# CMD is executed and replaced to any arguments passed
# CMD ["python3 tactile_servo_control/tactile_servo_control/learning/launch_hyper_training.py"]