FROM python:3.7-alpine

# copy the files over
COPY /www/flag.txt /home/flag.txt
COPY /www/app.py /home/app.py
COPY /www/models.py /home/models.py
COPY /www/templates/* /home/templates/
COPY /www/requirements.txt /home/requirements.txt

WORKDIR /home

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]