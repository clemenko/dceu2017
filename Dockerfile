FROM alpine:3.2
LABEL maintainer="clemenko@gmail.com"
RUN apk -U upgrade && apk add --no-cache py-pip &&\
    pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir flask  &&\
    rm -rf /var/cache/apk/*
WORKDIR /code
ADD . /code
EXPOSE 5000
CMD ["python", "app.py"]
