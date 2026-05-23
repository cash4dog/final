FROM python:3.11-slim

WORKDIR /app

COPY back_server.py .

EXPOSE 9900

CMD ["python", "-u", "back_server.py"]