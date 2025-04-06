from kafka import KafkaProducer
import json
import time
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def base(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/send")
async def send_text(request: Request):
    message = {
        "id": 1,
        'message': f'PRODUCER SERVICE TEN payment topic verisi'
    }

    message2 = {
        "id": 0,
        'message': f'PRODUCER SERVICE TEN test-topic verisi'
    }

    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        security_protocol='PLAINTEXT'
    )
    topic = "payment"
    topic2 = "test-topic"
    producer.send(topic2, value=message2)  # test-topic'in 0. partitionuna gönder
    # producer.send(topic2, value=message2, partition=1)  # test-topic'in 1. partitionuna gönder
    # producer.send(topic, value=message)
    producer.close()
