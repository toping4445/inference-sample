FROM python:3.7-slim
MAINTAINER Youngkyu OH <toping4445@gmail.com>
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

COPY . /rms-fastapi-uvicorn
WORKDIR /rms-fastapi-uvicorn
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]
