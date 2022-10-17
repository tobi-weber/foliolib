#!/bin/bash

JAVA=`which java`
VERSION=`$JAVA --version`


OKAPI_URL="http://$OKAPI_HOST:$OKAPI_HTTP_PORT"
OKAPI_CLUSTERHOST=$(hostname -i)
OKAPI_NODENAME=$(hostname)
OKAPI_JAR=/opt/okapi/okapi-core-fat.jar
HAZELCAST_FILE="/opt/okapi/hazelcast.xml"
HAZELCAST_FILE_TPL="/opt/okapi/hazelcast.xml.tpl"
HAZELCAST_PORT="5701"
HAZELCAST_VERTX_PORT="5702"
HAZELCAST_IP=$(hostname -i)
VERTX_CACHE_DIR_BASE="/tmp/vertx-cache-okapi"
OKAPI_JAVA_OPTS=" -Djava.awt.headless=true"


cp -f $HAZELCAST_FILE_TPL $HAZELCAST_FILE


# Purge postgres db
if [ "$PURGEDB" == "true" ]; then
    echo "Purge db on $PG_HOST"
    $JAVA \
    -Dstorage=$OKAPI_STORAGE \
    -Dpostgres_host=$PG_HOST \
    -Dpostgres_port=$PG_PORT \
    -Dpostgres_username=$PG_USERNAME \
    -Dpostgres_password=$PG_PASSWORD \
    -Dpostgres_database=$PG_DATABASE \
    -jar $OKAPI_JAR \
    purgedatabase

    echo "Done"
fi


# Init postgres db
if [ "$INITDB" == "true" ]; then
    echo "Init db on $PG_HOST"
    $JAVA \
    -Dstorage=$OKAPI_STORAGE \
    -Dpostgres_host=$PG_HOST \
    -Dpostgres_port=$PG_PORT \
    -Dpostgres_username=$PG_USERNAME \
    -Dpostgres_password=$PG_PASSWORD \
    -Dpostgres_database=$PG_DATABASE \
    -jar $OKAPI_JAR \
    initdatabase

    echo "Done"
fi


# Setup okapi storage
if [ "$OKAPI_STORAGE" == "postgres" ]; then
    OKAPI_JAVA_OPTS+=" -Dstorage=postgres"
    OKAPI_JAVA_OPTS+=" -Dpostgres_host=$PG_HOST"
    OKAPI_JAVA_OPTS+=" -Dpostgres_port=$PG_PORT"
    OKAPI_JAVA_OPTS+=" -Dpostgres_username=$PG_USERNAME"
    OKAPI_JAVA_OPTS+=" -Dpostgres_password=$PG_PASSWORD"
    OKAPI_JAVA_OPTS+=" -Dpostgres_database=$PG_DATABASE"
else
    OKAPI_JAVA_OPTS+=" -Dstorage=inmemory"
fi

#  Setup Kubernetes
if [ "$OKAPI_KUBERNETES" == "true" ]; then
    OKAPI_ROLE="cluster"
    sed -i "s/MULTICAST_BOOLEAN/false/g" $HAZELCAST_FILE
    sed -i "s/KUBERNETES_BOOLEAN/true/g" $HAZELCAST_FILE
    if [ $OKAPI_KUBERNETES_NAMESPACE ]; then
        sed -i "s/<namespace>KUBERNETES_NAMESPACE<\/namespace>/<namespace>${OKAPI_KUBERNETES_NAMESPACE}<\/namespace>/g" $HAZELCAST_FILE
        OKAPI_JAVA_OPTS+=" -Dkube_namespace=$OKAPI_KUBERNETES_NAMESPACE"
    else
        sed -i "s/<namespace>KUBERNETES_NAMESPACE<\/namespace>//g" $HAZELCAST_FILE
    fi
    if [ $OKAPI_KUBERNETES_SERVICE_NAME ]; then
        sed -i "s/<service-name>KUBERNETES_SERVICE_NAME<\/service-name>/<service-name>${OKAPI_KUBERNETES_SERVICE_NAME}<\/service-name>/g" $HAZELCAST_FILE
    else
        sed -i "s/<service-name>KUBERNETES_SERVICE_NAME<\/service-name>//g" $HAZELCAST_FILE
    fi
    /opt/okapi/create_kube_config.sh
    OKAPI_JAVA_OPTS+=" -Dkube_config=/root/.kube/config"
    OKAPI_JAVA_OPTS+=" -Dkube_server_pem=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
else
    sed -i "s/MULTICAST_BOOLEAN/true/g" $HAZELCAST_FILE
    sed -i "s/KUBERNETES_BOOLEAN/false/g" $HAZELCAST_FILE
fi


# if role is not set to 'dev', set okapi nodename
if [ "$OKAPI_ROLE" != "dev" ]; then
    OKAPI_JAVA_OPTS+=" -Dnodename=$OKAPI_NODENAME"
    OKAPI_JAVA_OPTS+=" -Dhazelcast.ip=$HAZELCAST_IP"
    OKAPI_JAVA_OPTS+=" -Dhazelcast.port=$HAZELCAST_PORT"
    OKAPI_OPTIONS+=" -cluster-host $OKAPI_CLUSTERHOST"
    OKAPI_OPTIONS+=" -cluster-port $HAZELCAST_VERTX_PORT"
    OKAPI_OPTIONS+=" -hazelcast-config-file $HAZELCAST_FILE"
    OKAPI_JAVA_OPTS+=" --add-modules java.se"
    OKAPI_JAVA_OPTS+=" --add-exports java.base/jdk.internal.ref=ALL-UNNAMED"
    OKAPI_JAVA_OPTS+=" --add-opens java.base/java.lang=ALL-UNNAMED"
    OKAPI_JAVA_OPTS+=" --add-opens java.base/java.nio=ALL-UNNAMED"
    OKAPI_JAVA_OPTS+=" --add-opens java.base/sun.nio.ch=ALL-UNNAMED"
    OKAPI_JAVA_OPTS+=" --add-opens java.management/sun.management=ALL-UNNAMED"
    OKAPI_JAVA_OPTS+=" --add-opens jdk.management/com.ibm.lang.management.internal=ALL-UNNAMED"
    OKAPI_JAVA_OPTS+=" --add-opens jdk.management/com.sun.management.internal=ALL-UNNAMED"
fi


if [ "$OKAPI_KUBE_SERVER_URL" ]; then
    OKAPI_JAVA_OPTS+=" -Dkube_server_url=$OKAPI_KUBE_SERVER_URL"
fi


if [ "$OKAPI_KUBE_CONFIG" ]; then
    OKAPI_JAVA_OPTS+=" -Dkube_config=$OKAPI_KUBE_CONFIG"
fi


if [ "$OKAPI_KUBE_SERVER_PEM" ]; then
    OKAPI_JAVA_OPTS+=" -Dkube_server_pem=$OKAPI_KUBE_SERVER_PEM"
fi


# Set performance metric options
if [ "$OKAPI_METRICS" == 1 ]; then
    OKAPI_OPTIONS+=" -enable-metrics"
fi


# configure okapi host
OKAPI_JAVA_OPTS+=" -Dhost=$OKAPI_HOST"


# configure okapi http port
OKAPI_JAVA_OPTS+=" -Dhttp.port=$OKAPI_HTTP_PORT"


# configure module port range
OKAPI_JAVA_OPTS+=" -Dport_start=$OKAPI_PORT_START -Dport_end=$OKAPI_PORT_END"

# configure dockerURL
if [ $DOCKER_URL ] ; then
    OKAPI_JAVA_OPTS+=" -DdockerUrl=$DOCKER_URL"
fi

# configure okapi URL
OKAPI_JAVA_OPTS+=" -Dokapiurl=$OKAPI_URL"


# configure iterations for readiness check
OKAPI_JAVA_OPTS+=" -Ddeploy.waitIterations=$OKAPI_DEPLOY_WAIT_ITERATIONS"


# configure Vert.x cache dir
OKAPI_JAVA_OPTS+=" -Dvertx.cacheDirBase=$VERTX_CACHE_DIR_BASE"


# configure loglevel
OKAPI_JAVA_OPTS+=" -Dloglevel=$OKAPI_LOGLEVEL"


echo ""
echo "############################"
echo "JAVA: $JAVA $VERSION"
echo "JVM OPTIONS: $OKAPI_JAVA_OPTS"
echo "OKAPI ROLE: $OKAPI_ROLE"
echo "OKAPI OPTIONS: $OKAPI_OPTIONS"
echo "OKAPI JAR: $OKAPI_JAR"
echo "############################"
echo ""

CMD="$JAVA $OKAPI_JAVA_OPTS -jar "$OKAPI_JAR" $OKAPI_ROLE $OKAPI_OPTIONS"
echo $CMD

echo -n "Starting Okapi..."
exec $CMD

