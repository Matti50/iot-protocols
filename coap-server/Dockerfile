FROM python:3.9-bullseye
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD coap-server.py /
EXPOSE 5683
CMD ["python", "./coap-server.py"]
