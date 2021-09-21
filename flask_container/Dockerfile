#use python container image
FROM python
#set working directory to /app
WORKDIR /app
#copy currnet dirctory contents to container at /app
ADD . /app
#install depedencies
RUN pip install -r requirements.txt
#run command to start uwsgi

CMD ["uwsgi", "app.ini"]