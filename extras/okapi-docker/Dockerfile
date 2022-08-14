FROM alpine:latest

RUN apk --no-cache --update add openjdk11-jre bash bind-tools

WORKDIR /opt/okapi

ENV OKAPI_HOST='okapi'
ENV OKAPI_HTTP_PORT='9130'
ENV OKAPI_PORT_START='9131'
ENV OKAPI_PORT_END='9141'
ENV INITDB='false'
ENV PURGEDB='false'
ENV OKAPI_STORAGE='postgres'
ENV PG_HOST='pghost'
ENV PG_PORT='5432'
ENV PG_USERNAME='okapi'
ENV PG_PASSWORD='okapi25'
ENV PG_DATABASE='okapi'
ENV OKAPI_ROLE='dev'
ENV OKAPI_METRICS=0
ENV OKAPI_DEPLOY_WAIT_ITERATIONS='60'
ENV OKAPI_LOGLEVEL='INFO'
ENV OKAPI_KUBERNETES='false'

COPY okapi-core-fat.jar /opt/okapi/
COPY hazelcast.xml.tpl /opt/okapi/
COPY create_kube_config.sh /opt/okapi/
COPY startup.sh /opt/okapi/
COPY Dockerfile /opt/okapi/

CMD ["/opt/okapi/startup.sh"]
