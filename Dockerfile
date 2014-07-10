FROM ubuntu:14.04
MAINTAINER jderuere <deruere.julien@gmail.com>

# Update OS
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y upgrade

# Install dependencies
RUN apt-get install make python-setuptools -y
RUN easy_install pip
RUN pip install pelican Markdown ghp-import shovel
RUN pip install --upgrade pelican Markdown ghp-import shovel

# Install script to ensures that newly created files are 775 by default
#ADD docker-umask-wrapper.sh /bin/docker-umask-wrapper.sh
#RUN chmod u+x /bin/docker-umask-wrapper.sh

WORKDIR /srv/pelican-website

# Expose default Pelican port
EXPOSE 8000

# Run Pelican
CMD make devserver
