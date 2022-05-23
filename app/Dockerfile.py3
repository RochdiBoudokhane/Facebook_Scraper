FROM python:3.8

# os setup
RUN apt-get update && apt-get -y install   

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


COPY /requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt


RUN pip install facebook_scraper
RUN pip install pandas
RUN pip install pymongo


COPY app /usr/src/app


#CMD ['python', './main.py']


# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 8000

