FROM python:latest
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]
