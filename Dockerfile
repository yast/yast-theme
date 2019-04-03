FROM registry.opensuse.org/yast/head/containers/yast-ruby:latest
RUN zypper --non-interactive in --no-recommends \
    breeze5-icons
COPY . /usr/src/app
