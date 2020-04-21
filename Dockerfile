FROM registry.opensuse.org/yast/sle-15/sp2/containers/yast-ruby
RUN zypper --non-interactive in --no-recommends \
    breeze5-icons
COPY . /usr/src/app
