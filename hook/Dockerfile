FROM alpine:edge
LABEL maintainer="clemenko@gmail.com"
RUN apk -U upgrade && apk add --no-cache curl py2-pip  &&\
    pip install --no-cache-dir --upgrade pip requests &&\
    pip install --no-cache-dir flask &&\
    rm -rf /var/cache/apk/*
WORKDIR /code
ADD . /code
EXPOSE 5000
HEALTHCHECK CMD curl -f http://localhost:5000/healthz || exit 1
CMD ["python", "hook.py"]
