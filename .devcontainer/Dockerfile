# Path: .devcontainer/Dockerfile
ARG VARIANT="3.0"
FROM mcr.microsoft.com/vscode/devcontainers/ruby:0-${VARIANT}

# [Optional] Uncomment this section to install additional packages.
ARG RUBY_VERSION=3.2.2
FROM ruby:$RUBY_VERSION-slim
ARG INSTALL_ZSH="true"
ARG UPGRADE_PACKAGES="true"
COPY library-scripts/*.sh /tmp/library-scripts/
COPY Gemfile Gemfile
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${UPGRADE_PACKAGES}" \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts/
RUN apt update \
    && apt install -y build-essential git locales nodejs

RUN NOKOGIRI_USE_SYSTEM_LIBRARIES=true bundle install

RUN \
  echo "en_US UTF-8" > /etc/locale.gen && \
  locale-gen en-US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
