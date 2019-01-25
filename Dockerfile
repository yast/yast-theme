FROM yastdevel/ruby
RUN zypper --non-interactive in --no-recommends \
    breeze5-icons
COPY . /usr/src/app
