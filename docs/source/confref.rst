Configuration Reference
=======================


foliolib.conf
-------------

.. code-block:: cfg

    # Section for node configuration where to pull module descriptors.
    [PullNode]

    # Host of the server.
    host = folio-registry.dev.folio.org

    # Port of the server.
    port = 443

    # Wether server is ssl.
    ssl = True


    # Section for cache configuration.
    [Cache]

    # Directory where to cache module descriptors.
    descriptors = [Home Directory]/.foliolib/cache/descriptors

    # Directory where to cache Folio platforms.
    platforms = [Home Directory]/.foliolib/cache/platforms



[Server Name]/server.conf
-------------------------

.. code-block:: cfg


    # Section for configuration of Okapi.
    [Okapi]

    # Okapi fqdn or ip.
    host = okapi

    # Okapi port. Default is 9130.
    port = 9130

    # Wether is ssl. Default is False.
    ssl = False

    # Wether verify ssl certificate. Default is True.
    verify_ssl = True

    # Wether foliolib handles global enviroment variables.
    # Default is True.
    foliolibenv = True


    # Section for command line interface
    [Cli]

    # Loglevel: INFO, WARNING, ERROR, DEBUG. Dfault is INFO
    loglevel = INFO

    # Wether every command needs to be confirmed.
    confirm = True

    # Wether display admin commands.
    isAdmin = True

    # Section for configuration for Kubernetes.
    [Kubernetes]

    # Wether Kubernetes is used. Default is False.
    enable = False

    # Namespace where modules are deployed. Default is folio.
    namespace = folio

    # Number of replicas of the modules. Default is 1.
    # mod-authtoken and mod-data-import can have always only
    # one replica and the value will be ignored.
    replicas = 1

    # Name of the Kubernetes Secret for a private registry.
    imagePullSecret = myPrivateRegistry

    # Deploy timeout in seconds. Default is 3600 seconds.
    deployTimeout = 3600

    # Memory request of the maximal memory usage of the modules.
    # The maximal memory usage is taken from the module descriptor.
    # Default is 100.
    memoryrequestpercentage = 100


    # Section for global enviroment variables.
    # Used if foliolibenv is True.
    [Env]

    # Example global enviroment variables.
    db_host = postgres
    db_port = 5432
    db_username = folio
    db_password = folio
    db_database = okapi_modules
    db_querytimeout = 120000
    db_charset = UTF-8
    kafka_host = kafka
    kafka_port = 9092
    okapi_url = http://okapi:9130

    # Reserved to handle login tokens.
    [Tokens]


[Server Name]/modules/[Module Name].conf
----------------------------------------

.. code-block:: cfg


    # Section for module enviroment variables.
    # This overwrites enviroment variables defined in server.conf,
    # if foliolibenv is True.
    [Env]


    # Section for Kubernetes configuration.
    [Kubernetes]

    # Kind of the deployment. Deployment or StatefulSet.
    # Default is Deployment.
    kind = Deployment

    # Number of replicas of the modules. Default is 1.
    # mod-authtoken and mod-data-import can have always only
    # one replica and the value will be ignored.
    replicas = 1

    # Memory request of the module. Default is the percentage
    # defined in memoryrequestpercentage in the server.conf of
    # the memory value from the module descriptor.
    min-memory = 1000Mi

    # Memory limit of the module. Default is the memory value from
    # the module descriptor of the module.
    max-memory = 1000Mi

    # CPU request of the module. Default is 10m.
    min-cpu = 10m

    # CPU limit of the module. Default not defined.
    max-cpu = 100m

    # Wether ReadinessProbe and LivenessProbe should be enabled.
    # Default is True.
    healthCheck = True

    # Wether the module supports Hazelcast. Default is False.
    hazelcast = False

    # Wether podAntiAffinity should be enabled.
    # Default is True.
    podAntiAffinity = True

    # Name of the Kubernetes Secret for a private registry.
    # Default it is not defined.
    imagePullSecret = myPrivateRegistry


    # Section to configure liveness probe of the module
    [LivenessProbe]

    # Default is 3
    failureThreshold = 3

    # Default is 45
    initialDelaySeconds = 45

    # Default is 60
    periodSeconds = 60

    # Default is 1
    successThreshold = 1

    # Default is 5
    timeoutSeconds = 5

    # Section to configure readiness probe probe of the module
    [ReadinessProbe]

    # Default is 3
    failureThreshold = 3

    # Default is 45
    initialDelaySeconds = 45

    # Default is 60
    periodSeconds = 60

    # Default is 1
    successThreshold = 1

    # Default is 5
    timeoutSeconds = 5


    # Section for defining a volume for the module.
    [Volume]

    # Mount path of the volume. Required if section Volume is defined.
    mountPath = /mnt

    # Size of the volume. Required if section Volume is defined.
    size = 1Gi

    # StorageClassName.
    storageClassName = myStorageClass


    # Section to define the security context.
    [SecurityContext]

    # UID as integer.
    runAsUser = 1000

    # Boolean.
    runAsNonRoot = True

    # GID as integer.
    runAsGroup = 1000

    # GID as integer.
    fsGroup = 1000

    fsGroupChangePolicy = Always
