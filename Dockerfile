#FROM python:3
#USER root
#LABEL maintainer="maria.morozov@gmail.com"
#RUN mkdir /hm1
#
#RUN chmod -R 755 /hm1
#COPY * /hm1/
#RUN pip install -r /hm1/requirements.txt
#
#WORKDIR "/hm1"
#EXPOSE 5000
#ADD main.py /
##CMD [ "python3", "./main.py" ]
##ENTRYPOINT [ "/usr/local/bin/python3", "/hm1/main.py" ]
#ENV FLASK_APP=main.py
#ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
#

FROM python:3.7

RUN mkdir /hm1
WORKDIR /hm1
ADD . /hm1/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/hm1/main.py"]
