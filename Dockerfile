
FROM rackspacedot/python37 

LABEL Name=calc Version=0.0.1
WORKDIR /app
ADD . /app

RUN pip install .
#CMD ["sub", "-n", "100", "20"]
#ENTRYPOINT [ "mycalc" ]