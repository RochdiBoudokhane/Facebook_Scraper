FROM python:3.8

# os setup
RUN apt-get update && apt-get -y install   

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app



#RUN mkdir /usr/src/app
#WORKDIR /usr/src/app
#RUN apk update
#COPY ./requirements.txt .
#RUN pip install -r requirements.txt

COPY /requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt


#RUN ln -s /usr/bin/python3 /usr/bin/python

#RUN apt-get install -y python3-pip
RUN pip install facebook_scraper
RUN pip install pandas
RUN pip install pymongo
#RUN pip3 install fastapi
#RUN pip3 install pydantic
#RUN pip3 install uvicorn

COPY app /usr/src/app

# install requirements
#COPY ./requirements.txt /usr/src/app/
#RUN pip3 install --no-cache-dir -r requirements.txt

#CMD ['python', './main.py']


# 
#CMD ['python', '-m', 'uvicorn', 'main:app', '--reload']
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 8000

#ENV PYTHONUNBUFFERED 1
