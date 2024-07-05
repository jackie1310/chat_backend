FROM python:3.12-slim

WORKDIR /app

COPY . /app

# RUN apt-get update && apt-get install -y build-essential
# RUN apt-get update && apt-get install -y build-essential
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt-get update && apt-get install -y gcc python3-dev
RUN apt-get update && apt-get install -y libglib2.0-0





RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./main.py