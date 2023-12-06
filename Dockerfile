FROM python:3.11

CMD mkdir /spam-sms
COPY . /spam-sms
WORKDIR /spam-sms

EXPOSE 8501

RUN pip3 install -r requirements.txt

CMD  ["streamlit", "run","app.py"]

