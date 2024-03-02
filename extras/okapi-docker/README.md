# Okapi Docker Image

## Build Okapi Docker Image

To build the okapi docker image run:

``` bash
docker build -t okapi:5.3.0 --build-arg version=5.3.0 .
```

## Enviroment Variables

- OKAPI_HOST
  - Hostname. Default is okapi.
- OKAPI_HTTP_PORT
  - Port. Default is 9130.
- OKAPI_PORT_START
  - Start range of ports for modules
- OKAPI_PORT_END
  - End range of ports for modules.
- OKAPI_ROLE
  - Role. Default is dev.
- OKAPI_KUBERNETES
  - Wether Kubernetes integration is enabled. If true, then OKAPI_ROLE is cluster. Default is false.
- OKAPI_KUBERNETES_SERVICE_NAME
  - Service name of the okapi deployment. Default is okapi.
- OKAPI_KUBERNETES_NAMESPACE
  - Namespace where okapi is deployed. Default is folio.
- OKAPI_METRICS
  - Set performance metric options. 0 or 1. Default is 0.
- OKAPI_DEPLOY_WAIT_ITERATIONS
  - configure iterations for readiness check. Default is 60.
- OKAPI_LOGLEVEL
  - Configure loglevel. Default is INFO.
- OKAPI_STORAGE
  - postgres or inmemory. Default is postgres.
- PG_HOST
  - Postgres hostname. Default is postgres.
- PG_PORT
  - Postgres port. Default is 5432
- PG_DATABASE
  - Okapi database. Default is okapi.
- PG_USERNAME
  - Postgres username. Default is okapi.
- PG_PASSWORD
  - Postgres password. Default is okapi25
- DOCKER_URL
  - http url of docker
- INITDB
  - Wether database should be initialized.
- PURGEDB
  - Wether database should be purged.

## Example Okapi Docker Compose

```yaml
version: "3"
services:

  okapi:
    image: <FQDN registry>/okapi:<VERSION>
    container_name: okapi
    restart: always
    ports:
      - 9130:9130
    environment:
      - OKAPI_HOST=okapi
      - PG_HOST=<FQDN postgres host>
      - PG_DATABASE=okapi
      - PG_USERNAME=okapi
      - PG_PASSWORD=okapi25
      - DOCKER_URL=http://<FQDN docker host>:4243
      - OKAPI_PORT_START=9131
      - OKAPI_PORT_END=9141
      - INITDB=true
```

## Example Kubernetes Deployment

``` yaml
apiVersion: v1
kind: Namespace
metadata:
  name: folio
  labels:
    name: folio

---

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: okapi-hazelcast-cluster-role
rules:
  - apiGroups:
      - ""
    resources:
      - endpoints
      - pods
      - nodes
      - services
    verbs:
      - get
      - list

---

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: okapi-hazelcast-cluster-role-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: okapi-hazelcast-cluster-role
subjects:
  - kind: ServiceAccount
    name: default
    namespace: folio

---

apiVersion: v1
kind: Service
metadata:
  name: okapi
  namespace: folio
  labels:
    app: okapi
spec:
  ports:
    - name: "okapi"
      protocol: TCP
      port: 9130
      targetPort: 9130
  selector:
    app: okapi

---

apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: okapi
  namespace: folio
spec:
  serviceName: "okapi"
  replicas: 3
  selector:
    matchLabels:
      app: okapi
  template:
    metadata:
      labels:
        app: okapi
    spec:
      containers:
        - env:
            - name: OKAPI_HOST
              value: okapi
            - name: PG_HOST
              value: postgres
            - name: OKAPI_KUBERNETES
              value: "true"
            - name: OKAPI_KUBERNETES_SERVICE_NAME
              value: "okapi"
            - name: OKAPI_KUBERNETES_NAMESPACE
              value: "folio"
            - name: INITDB
              value: "true"
          image: <FQDN registry>/okapi:<VERSION>
          name: okapi
          imagePullPolicy: Always
          ports:
            - containerPort: 9130
            - containerPort: 5701
            - containerPort: 5702
            - containerPort: 5703
            - containerPort: 5704
            - containerPort: 54327
          livenessProbe:
            failureThreshold: 2
            httpGet:
              path: /_/proxy/health
              port: 9130
              scheme: HTTP
            initialDelaySeconds: 30
            periodSeconds: 60
            successThreshold: 1
            timeoutSeconds: 5
          readinessProbe:
            failureThreshold: 2
            httpGet:
              path: /_/proxy/health
              port: 9130
              scheme: HTTP
            initialDelaySeconds: 30
            periodSeconds: 60
            successThreshold: 1
            timeoutSeconds: 5
```
