FROM python:3.9.2

ENV BINARY_PATH=/usr/bin/google-chrome
ENV DRIVER_PATH=/usr/local/bin/chromedriver
ENV DISPLAY=:99
ENV PYTHONUNBUFFERED=1

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - 
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get -y update && \
    apt-get install -y google-chrome-stable

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY app /app
WORKDIR /app

RUN useradd alice
USER alice

CMD ["python", "main.py"]
