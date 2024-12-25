variable "APP_VERSION" {
    default = "$APP_VERSION"
}

variable "APP_COMMIT" {
    default = "$APP_COMMIT"
}

variable "PYTHON_VERSION" {
    default = "$PYTHON_VERSION"
}

variable "APP_NAME" {
    default = "$APP_NAME"
}

variable "APP_PORT" {
    default = "$APP_PORT"
}

variable "TIMEZONE" {
    default = "$TIMEZONE"
}

variable "USE_CHINA_MIRROR" {
    default = "$USE_CHINA_MIRROR"
}

variable "CHINA_MIRROR_SOURCE" {
    default = "$CHINA_MIRROR_SOURCE"
}

variable "WORKDIR" {
    default = "$WORKDIR"
}

variable "INSTALL_GIT" {
    default = "$INSTALL_GIT"
}

variable "INSTALL_NETWORK_TOOLS" {
    default = "$INSTALL_NETWORK_TOOLS"
}

variable "INSTALL_PING" {
    default = "$INSTALL_PING"
}

variable "INSTALL_DEBUG_TOOLS" {
    default = "$INSTALL_DEBUG_TOOLS"
}

group "default" {
    targets = ["backend"]
}

target "backend" {
    dockerfile = "Dockerfile"
    platforms = ["linux/amd64", "linux/arm64", "linux/arm/v7"]

    labels = {
        "app.version" = "${APP_VERSION}",
        "app.name" = "${APP_NAME}",
        "app.commit" = "${APP_COMMIT}",
        "app.framework" = "fastapi",
        "app.language" = "python",
        "app.type" = "service",
        "app.port" = "${APP_PORT}",
    }

    args = {
        PYTHON_VERSION = "${PYTHON_VERSION}"
        TIMEZONE = "${TIMEZONE}"
        USE_CHINA_MIRROR = "${USE_CHINA_MIRROR}"
        CHINA_MIRROR_SOURCE = "${CHINA_MIRROR_SOURCE}"
        WORKDIR = "${WORKDIR}"
        INSTALL_GIT = "${INSTALL_GIT}"
        INSTALL_NETWORK_TOOLS = "${INSTALL_NETWORK_TOOLS}"
        INSTALL_PING = "${INSTALL_PING}"
        INSTALL_DEBUG_TOOLS = "${INSTALL_DEBUG_TOOLS}"
        APP_PORT = "${APP_PORT}"
    }

    tags = [
        "${APP_NAME}:${APP_VERSION}"
    ]

    context = "."
}
