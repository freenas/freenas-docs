#Download base image debian buster
FROM debian:buster
 
# Install nginx, and supervisord from debian repository
RUN apt-get update && apt-get install -y sphinx-common \
	sphinx-intl \
	make \
	texlive \
	texlive-xetex \
	texlive-formats-extra \
	texlive-latex-base \
	latexmk \
	dblatex \
	fonts-materialdesignicons-webfont \ 
	fonts-open-sans \
	fonts-freefont-ttf \
	fonts-freefont-otf

# Put things in right locations for Linux
RUN rm -rf /var/lib/apt/lists/*
 
# Configure Services and Port
COPY docker/build.sh /build.sh
CMD ["/build.sh"]
 
#EXPOSE 80 443
