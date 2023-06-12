Singleserver installation
=========================

The following installation steps  assumes that a server with the FQDN
**folioserver** with Okapi, Postgres, Kafka/Zookeeper and Elasticsearch running
on it is available.

1. Create a config named myFolio with for the server **folioserver**:

  .. code-block:: bash

      foliolib server create myFolio -H folioserver

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


3. Create the file $HOME/.foliolib/myFolio/modules/mod-search.conf and
   replace the ELASTIC_PASSWORD and MODSEARCH_PASSOWRD with your own value:

  .. code-block:: cfg

      [Env]
      ELASTICSEARCH_URL = http://folioserver:9200
      ELASTICSEARCH_PORT = 9200
      ELASTICSEARCH_HOST = folioserver
      ELASTICSEARCH_USERNAME = elastic
      ELASTICSEARCH_PASSWORD = ELASTIC_PASSWORD
      INITIAL_LANGUAGES = eng,ger
      SYSTEM_USER_PASSWORD = MODSEARCH_PASSOWRD


4. Create the file HOME/.foliolib/myFolio/modules/mod-pubsub.conf and
   replace MOD_PUBSUB_PASSWORD with your own value:

  .. code-block:: cfg

      [Env]
      SYSTEM_USER_PASSWORD = MOD_PUBSUB_PASSWORD


5. Install a folio tenant named **test**:

  .. code-block:: bash

    foliolib platform install test --loadReference --loadSample -a -p R1-2023-GA


6. Create a superuser for the tenant **test** with username **test**
   and password **test**:

  .. code-block:: bash

    foliolib folio superuser test -u test -p test


7. Install the Frontend for the folio platform R1-2023-GA for the tenant test.
