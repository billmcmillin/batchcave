FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN echo "deb http://download.mono-project.com/repo/debian jessie main" | tee /etc/apt/sources.list.d/mono-official.list
RUN apt-get update
RUN cat /etc/*-release
RUN apt-get install mono-complete -y
RUN apt remove firefox
RUN apt-get install firefox-esr xvfb -y
RUN pip install selenium pyvirtualdisplay
#ADD xvfb.init /etc/init.d/xvfb
#RUN chmod +x /etc/init.d/xvfb
#RUN update-rc.d xvfb defaults
#CMD (service xvfb start; export DISPLAY=10;)
COPY . /code/
RUN cp geckodriver /usr/local/bin/
