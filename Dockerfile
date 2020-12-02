FROM python:3.8
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt-get -y install sudo
RUN sudo apt-get update && apt-get install -y cowsay fortunes
ENV PATH $PATH:/usr/games
RUN echo $PATH

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install requests requests_oauthlib
RUN pip install pandas
RUN pip install IPython
RUN pip install twitter
RUN pip install tweepy
RUN pip install snscrape