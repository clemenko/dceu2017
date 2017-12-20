from jenkins:alpine
MAINTAINER clemenko@docker.com
USER root
RUN apk -U --no-cache add docker
