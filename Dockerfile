FROM python:3.10.4-slim-buster
WORKDIR /app
RUN apt-get update && apt -y install git curl python3-pip
COPY . .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD flask run -h 0.0.0.0 -p 8000 & python3 -m session
