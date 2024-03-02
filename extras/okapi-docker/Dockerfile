FROM openjdk:19-alpine

ARG version

WORKDIR /opt/okapi

RUN apk --no-cache --update add bash bind-tools git maven
RUN git clone -b "v${version}" --recursive https://github.com/folio-org/okapi.git
RUN cd okapi; mvn clean install -DskipTests
RUN cp okapi/okapi-core/target/okapi-core-fat.jar .
RUN rm -rf okapi /root/.m2
RUN apk del git maven


ENV OKAPI_HOST='okapi'
ENV OKAPI_HTTP_PORT='9130'
ENV OKAPI_PORT_START='9131'
ENV OKAPI_PORT_END='9141'
ENV INITDB='false'
ENV PURGEDB='false'
ENV OKAPI_STORAGE='postgres'
ENV PG_HOST='postgres'
ENV PG_PORT='5432'
ENV PG_USERNAME='okapi'
ENV PG_PASSWORD='okapi25'
ENV PG_DATABASE='okapi'
ENV OKAPI_ROLE='dev'
ENV OKAPI_METRICS=0
ENV OKAPI_DEPLOY_WAIT_ITERATIONS='60'
ENV OKAPI_LOGLEVEL='INFO'
ENV OKAPI_KUBERNETES='false'

COPY hazelcast.xml.tpl /opt/okapi/
COPY create_kube_config.sh /opt/okapi/
COPY startup.sh /opt/okapi/
COPY Dockerfile /opt/okapi/

CMD ["/opt/okapi/startup.sh"]
