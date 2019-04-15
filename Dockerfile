
FROM rackspacedot/python37 as build 

LABEL Name=calc Version=0.0.1
WORKDIR /app
ADD . /app

RUN pip install .
RUN pyinstaller src/calc/cli.py

FROM ubuntu 
RUN mkdir -p /app/cli
COPY --from=build /app/dist/cli/ /app/cli

CMD ["sub", "-n", "100", "20"]
ENTRYPOINT [ "/app/cli/cli" ]