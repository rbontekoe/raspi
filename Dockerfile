FROM resin/rpi-raspbian

RUN apt-get -q update && \  
    apt-get -qy install \
        python3 python3-pip \
        python3-dev gcc make \
	python3-flask \
	nano wget curl \
	rpi.gpio \
	sense-hat
	  
RUN pip3 install rpi.gpio wtforms flask-bootstrap flask-nav \
	pillow

COPY web.tar.gz .
RUN tar -zxvf web.tar.gz
