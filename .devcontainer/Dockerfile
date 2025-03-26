FROM ubuntu:22.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
    cmake \
    libgl1-mesa-glx \
    libopenblas-dev \
    libopengl0 \
    libsuitesparse-dev \
    pkg-config \
    python3 \
    python3-pip \
    swig \
    wget
RUN pip3 install meson ninja

WORKDIR /tmp
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
RUN bash Miniconda3-latest-Linux-aarch64.sh -b -p /opt/conda
RUN rm Miniconda3-latest-Linux-aarch64.sh
ENV PATH="/opt/conda/bin:$PATH"

RUN conda config --add channels conda-forge && \
    conda config --set channel_priority strict

RUN conda install -y jupyter
RUN conda install -y -c conda-forge ocp
RUN conda install -y -c conda-forge cadquery
RUN conda install -y -c conda-forge pyopengl
RUN conda install conda-forge::sqlite conda-forge:libsqlite
RUN pip3 install "ezdxf>=1.3.0"

ENV LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH

#conda install conda-forge::libsqlite --force-reinstall
# conda install conda-forge::sqlite --force-reinstall