FROM python:3.10

WORKDIR /code

# Installing node and npm
RUN apt-get update && \
  apt-get install -y curl && \
  curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
  apt-get install -y nodejs && \
  apt-get install -y npm

# Install Google Chrome stable
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
  apt-get update && \
  apt-get install -y google-chrome-stable


RUN useradd -m -u 1000 user
USER user
  
# This env require for puppeteer to use chrome
ENV PUPPETEER_SKIP_DOWNLOAD=true \
  PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome

# setting correct working path
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# Copying everything from current dir to ~/app and setting user as owner
# This is nessecary to set owner as user
COPY --chown=user . $HOME/app

# Installing dependencies 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN npm install

CMD ["bash", "-c", "uvicorn app:app --host 0.0.0.0 --port 7860 & node index.js"]