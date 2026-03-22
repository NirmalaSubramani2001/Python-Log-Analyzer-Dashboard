FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

VOLUME ["/app/logs"]

EXPOSE 5000

CMD ["python", "app.py"]
