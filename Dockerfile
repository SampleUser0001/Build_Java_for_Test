# 任意のイメージを取得
FROM python:latest

# タイムゾーン設定
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# aws-cliインストール
RUN apt-get update && apt-get install -y less curl unzip sudo

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN sudo ./aws/install

RUN python -m pip install --upgrade pip
RUN pip install python-dotenv boto3

WORKDIR /opt/app

COPY app /opt/app

RUN chmod 755 /opt/app/start.sh

RUN python --version

# ENTRYPOINT [ "/opt/app/start.sh" ]
