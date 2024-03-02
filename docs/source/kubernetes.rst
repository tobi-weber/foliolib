Kubernetes installation
=======================


The following installation steps assumes that a kubernetes server
with Okapi, Postgres, Kafka/Zookeeper, Elasticsearch and a
namespace **folio** is available.

So that the deployment works, Okapi needs to be running with
`service discovery enabled <https://github.com/folio-org/okapi/blob/master/doc/guide.md#kubernetes-integration>`_.

`Here <https://github.com/tobi-weber/foliolib/tree/master/extras/okapi-docker>`_
is a Dockerfile to build an image of Okapi with Kubernetes integration.


1. Create a config named myFolio, with th e fqdn of okapi and the port.
   If Okapi is running with ssl add *--ssl* to the command:

  .. code-block:: bash

      foliolib server create myFolio --host <fqdn okapi> --port 9130 --admin [--ssl]

2. Copy the kube config file to $HOME/.foliolib/myFolio/kube_config


3. Edit the File $HOME/.foliolib/myFolio/server.conf and
   add the following **Kubernetes** and **Env** section and replace the
   database and kafka config with your values:

  .. code-block:: cfg

    [Kubernetes]
    enable = True
    namespace = folio
    memoryRequestPercentage = 10

    [Env]
    db_host = <fqdn postgres>
    db_port = 5432
    db_username = folio
    db_password = folio_password
    db_database = okapi_modules
    db_querytimeout = 120000
    db_charset = UTF-8
    db_maxpoolsize = 50
    db_connection_timeout = 100
    kafka_host = <fqdn kafka>
    kafka_port = 9092
    okapi_url = http://okapi:9130
    # replication_factor = 3


4. Create module config files:
   
  Create the file $HOME/.foliolib/myFolio/modules/mod-erm-usage-harvester.conf

  .. code-block:: cfg

    [Kubernetes]
    hazelcast = True



  Create the file $HOME/.foliolib/myFolio/modules/mod-agreements.conf

  .. code-block:: cfg

    [Env]
    okapi_service_host = okapi
    okapi_service_port = 9130

    [Resources]
    max-memory = 1200Mi

    [Kubernetes]
    hazelcast = True

   

  Create the file $HOME/.foliolib/myFolio/modules/mod-search.conf and
  replace the ELASTIC_PASSWORD, MOD_SEARCH_USER and MODSEARCH_PASSOWRD with your own value:

  .. code-block:: cfg

    [Env]
    ELASTICSEARCH_URL = http://<fqdn elasticsearch>:9200
    ELASTICSEARCH_PORT = 9200
    ELASTICSEARCH_HOST = <fqdn elasticsearch>
    ELASTICSEARCH_USERNAME = elastic
    ELASTICSEARCH_PASSWORD = ELASTIC_PASSWORD
    INITIAL_LANGUAGES = eng,ger
    SYSTEM_USER_NAME = MOD_SEARCH_USER
    SYSTEM_USER_PASSWORD = MODSEARCH_PASSOWRD



  Create the file HOME/.foliolib/myFolio/modules/mod-consortia.conf
  and replace MOD_CONSORTIA_USER and MOD_CONSORTIA_PASSWORD with your own value:

  .. code-block:: cfg

      [Env]
      SYSTEM_USER_NAME = MOD_CONSORTIA_USER
      SYSTEM_USER_PASSWORD = MOD_CONSORTIA_PASSWORD



  Create the file HOME/.foliolib/myFolio/modules/mod-data-export-spring.conf
  and replace MOD_DATA_EXPORT_SPRING_USER and MOD_DATA_EXPORT_SPRING_PASSWORD with your own value:

  .. code-block:: cfg

      [Env]
      SYSTEM_USER_NAME = MOD_DATA_EXPORT_SPRING_USER
      SYSTEM_USER_PASSWORD = MOD_DATA_EXPORT_SPRING_PASSWORD



  Create the file HOME/.foliolib/myFolio/modules/mod-dcb.conf
  and replace MOD_DCB_USER_USER and MOD_DCB_PASSWORD with your own value:

  .. code-block:: cfg

      [Env]
      SYSTEM_USER_NAME = MOD_DCB_USER_USER
      SYSTEM_USER_PASSWORD = MOD_DCB_PASSWORD



  Create the file HOME/.foliolib/myFolio/modules/mod-entities-links.conf
  and replace MOD_ENTITIES_LINKS_USER and MOD_ENTITIES_LINKS_PASSWORD with your own value:

  .. code-block:: cfg

      [Env]
      SYSTEM_USER_NAME = MOD_ENTITIES_LINKS_USER
      SYSTEM_USER_PASSWORD = MOD_ENTITIES_LINKS_PASSWORD
      DB_CONNECTION_TIMEOUT = 30000



  Create the file HOME/.foliolib/myFolio/modules/mod-inn-reach.conf
  and replace MOD_INN_REACH_USER and MOD_INN_REACH_PASSWORD with your own value:

  .. code-block:: cfg

      [Env]
      SYSTEM_USER_NAME = MOD_INN_REACH_USER
      SYSTEM_USER_PASSWORD = MOD_INN_REACH_PASSWORD
   


  Create the file HOME/.foliolib/myFolio/modules/mod-pubsub.conf and
  replace MOD_PUBSUB_USER and MOD_PUBSUB_PASSWORD with your own value:

  .. code-block:: cfg

      [Env]
      SYSTEM_USER_NAME = MOD_PUBSUB_USER
      SYSTEM_USER_PASSWORD = MOD_PUBSUB_PASSWORD



  Create the file HOME/.foliolib/myFolio/modules/mod-remote-storage.conf and
  replace MOD_REMOTE_STORAGE_USER and MOD_REMOTE_STORAGE_PASSWORD with your own value:

  .. code-block:: cfg

      [Env]
      SYSTEM_USER_NAME = MOD_REMOTE_STORAGE_USER
      SYSTEM_USER_PASSWORD = MOD_REMOTE_STORAGE_PASSWORD

      [Kubernetes]
      hazelcast = True


5.  Install a folio tenant named **test**:

  .. code-block:: bash

    foliolib platform install -t test --loadReference --loadSample -a -p R2-2023-csp-1


6. Create a superuser for the tenant **test** with username **test**
    and password **test**:

  .. code-block:: bash

    foliolib tenant superuser -t test -u test -p test


7. Install the Frontend for the folio platform R2-2023-csp-1
    for the tenant test.

