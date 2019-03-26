FROM yastdevel/ruby:sle15-sp1
RUN zypper --non-interactive in --no-recommends \
    breeze5-icons
COPY . /usr/src/app
