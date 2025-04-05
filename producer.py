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
        'message': f'PRODUCER SERVICE TEN VERI'
    }
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        security_protocol='PLAINTEXT'
    )
    topic = "payment"
    producer.send(topic, value=message)
    producer.close()
