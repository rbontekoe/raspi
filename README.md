# raspi
Tryout git, raspberry, docker, sense-hat and flask.

I have a RaspberryPi 3 with Docker installed and a container. The container has Flask running en the website displays the air pressure. My objective is to learn Git.

Instruction
1. Install Docker on Raspberry Pi 3
2. Download Dockerfile and web.tar.gz
3. Build Docker image: docker build -t rbontekoe/myflaskapp:1.0 .
4. Create container: docker run --privileged -it -p 5005:80 rbontekoe/robflask:1.0
5. Start app: python3 web/app.py
6. Load web app in browser: http://raspi2:5005/ - I use my Chromebook to access my Raspberry Pi 3 remote via ssh. 

Reference
Get started with docker: http://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/
