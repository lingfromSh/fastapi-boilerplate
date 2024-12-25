# use python:${PYTHON_VERSION}-slim as base image
ARG PYTHON_VERSION=3.12.8-slim
FROM python:${PYTHON_VERSION}

# if you are in China, set USE_CHINA_MIRROR to true and set CHINA_MIRROR_SOURCE to the nearest mirror
ARG USE_CHINA_MIRROR=true
ARG CHINA_MIRROR_SOURCE=mirrors.shanghaitech.edu.cn
COPY ./ci/china/auto-mirror.sh /opt/auto-mirror.sh
RUN if [ "${USE_CHINA_MIRROR}" = "true" ]; \
    then \
        apt-get -y update && apt-get -y install lsb-release ca-certificates && \
        bash /opt/auto-mirror.sh --protocol https --source ${CHINA_MIRROR_SOURCE} --clean-cache true --upgrade-software true --backup false --use-intranet-source false --ignore-backup-tips; \
        rm -rf /opt/auto-mirror.sh; \
    else \
        apt-get -y update && \
        rm -rf /opt/auto-mirror.sh; \
    fi

# set timezone
ARG TIMEZONE=Asia/Shanghai
RUN apt-get -y update && apt-get -y install tzdata && cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && echo ${TIMEZONE} > /etc/timezone

# install optional tools
ARG INSTALL_GIT="false"
ARG INSTALL_NETWORK_TOOLS="false"
ARG INSTALL_PING="false"
ARG INSTALL_DEBUG_TOOLS="false"
RUN if [ "${INSTALL_GIT}" = "true" ]; then apt-get -y update && apt-get -y install git; fi
RUN if [ "${INSTALL_NETWORK_TOOLS}" = "true" ]; then apt-get -y update && apt-get -y install curl wget; fi
RUN if [ "${INSTALL_PING}" = "true" ]; then apt-get -y update && apt-get -y install iputils; fi
RUN if [ "${INSTALL_DEBUG_TOOLS}" = "true" ]; then apt-get -y update && apt-get -y install htop iotop vim tmux; fi

# set workdir
ARG WORKDIR=/app
WORKDIR ${WORKDIR}

# set app port
ARG APP_PORT=8000
EXPOSE ${APP_PORT}

# you can add your own commands below
