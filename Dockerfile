FROM python:alpine

ARG NODE_HOST
ARG PORT

COPY src /src/

RUN apk add --no-cache python3-dev libffi-dev gcc musl-dev make
RUN pip install -r src/requirements.txt
RUN export NODE_HOST=NODE_HOST
RUN export PORT=PORT

ENTRYPOINT ["python", "/src/app.py"]
