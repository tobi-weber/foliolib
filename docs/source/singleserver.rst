Singleserver installation
=========================

The following installation steps  assumes that a server with the FQDN
**folioserver** with Okapi, Postgres, Kafka/Zookeeper and Elasticsearch running
on it is available.

1. Create a config named myFolio with for the server **folioserver**:

  .. code-block:: bash

      foliolib server create myFolio --host folioserver --admin

2. Edit the File $HOME/.foliolib/myFolio/server.conf and
   add the following **Env** section:

  .. code-block:: cfg

      [Env]
      db_host = folioserver
      db_port = 5432
      db_username = okapi
      db_password = okapi25
      db_database = okapi_modules
      db_querytimeout = 120000
      db_charset = UTF-8
      kafka_host = folioserver
      kafka_port = 9092
      okapi_url = http://folioserver:9130


3. Create module config files:
 
   Create the file $HOME/.foliolib/myFolio/modules/mod-search.conf and
   replace the ELASTIC_PASSWORD, MOD_SEARCH_USER and MODSEARCH_PASSOWRD with your own value:

  .. code-block:: cfg

      [Env]
      ELASTICSEARCH_URL = http://folioserver:9200
      ELASTICSEARCH_PORT = 9200
      ELASTICSEARCH_HOST = folioserver
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


4. Install a folio tenant named **test**:

  .. code-block:: bash

    foliolib platform install -t test --loadReference --loadSample -a -p R2-2023-csp-1


5. Create a superuser for the tenant **test** with username **test**
   and password **test**:

  .. code-block:: bash

    foliolib tenant superuser -t test -u test -p test


6. Install the Frontend for the folio platform R2-2023-csp-1
   for the tenant test.

