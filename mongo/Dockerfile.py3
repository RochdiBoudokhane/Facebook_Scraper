FROM mongo:latest

#RUN mongo "mongodb://cluster0-shard-00-00.t3c6s.mongodb.net:27017,cluster0-shard-00-01.t3c6s.mongodb.net:27017,cluster0-shard-00-02.t3c6s.mongodb.net:27017/pap_database?replicaSet=atlas-z4q7ed-shard-0" --ssl --authenticationDatabase admin --username admin --password admin 

RUN apt-get update && apt-get -y install cron
# copy request_scrapy script into container
COPY mongo/request_mongodb /etc/cron.d/request_mongodb

# Give execution rights on the cron job
RUN chmod 0744 /etc/cron.d/request_mongodb  

# Apply cron job
RUN crontab /etc/cron.d/request_mongodb
 
# Create the log file to be able to run tail
RUN touch /var/log/cron_mongodb.log
 
# Run the command on container startup
ENTRYPOINT cron start && tail -f /var/log/cron_mongodb.log