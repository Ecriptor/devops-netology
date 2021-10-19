# Домашнее задание к занятию "13.1 контейнеры, поды, deployment, statefulset, services, endpoints"
Настроив кластер, подготовьте приложение к запуску в нём. Приложение стандартное: бекенд, фронтенд, база данных (пример можно найти в папке 13-kubernetes-config).

## Задание 1: подготовить тестовый конфиг для запуска приложения
Для начала следует подготовить запуск приложения в stage окружении с простыми настройками. Требования:
* под содержит в себе 3 контейнера — фронтенд, бекенд, базу;
* регулируется с помощью deployment фронтенд и бекенд;
* база данных — через statefulset.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-backend
  labels:
    app: netology
spec:
  replicas: 1
  selector:
    matchLabels:
      app: netology
  template:
    metadata:
      labels:
        app: netology
    spec:
      containers:
      - name: frontend
        image: ecriptor/netology-frontend:0.1
        ports:
        - containerPort: 80
      - name: backend
        image: ecriptor/netology-backend:0.1
        env:
          - name: DATABASE_URL
            value: postgres://postgres:postgres@db:5432/news
        ports:
        - containerPort: 9000
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db
spec:
  selector:
    matchLabels:
      app: db
  serviceName: "postgesql"
  replicas: 1
  template:
    metadata:
      labels:
        app: db
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: db
        image: postgres:13-alpine
        ports:
        - containerPort: 5432
        env:
          - name: POSTGRES_PASSWORD
            value: postgres
          - name: POSTGRES_USER
            value: postgres
          - name: POSTGRES_DB
            value: news
---
apiVersion: v1
kind: Service
metadata:
  name: db
spec:
  selector:
    app: db
  ports:
    - protocol: TCP
      port: 5432
      targetPort: 5432
```
```shell
root@master-0001:~# kubectl apply -f front-back-db.yml
deployment.apps/frontend-backend created
statefulset.apps/db created
service/db created

root@master-0001:~# kubectl get deploy
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
frontend-backend   1/1     1            1           2m13s
hello-node         1/1     1            1           13d

root@master-0001:~# kubectl get statefulsets.apps
NAME   READY   AGE
db     1/1     2m29s

root@master-0001:~# kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
db-0                                1/1     Running   0          2m53s
frontend-backend-79bb8996c9-q5v62   2/2     Running   0          2m53s
hello-node-7567d9fdc9-ppht5         1/1     Running   0          13d

root@master-0001:~# kubectl get service
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
db           ClusterIP   10.233.42.13   <none>        5432/TCP   3m10s
kubernetes   ClusterIP   10.233.0.1     <none>        443/TCP    14d
```

## Задание 2: подготовить конфиг для production окружения
Следующим шагом будет запуск приложения в production окружении. Требования сложнее:
* каждый компонент (база, бекенд, фронтенд) запускаются в своем поде, регулируются отдельными deployment’ами;
* для связи используются service (у каждого компонента свой);
* в окружении фронта прописан адрес сервиса бекенда;
* в окружении бекенда прописан адрес сервиса базы данных.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  labels:
    app: frontend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: ecriptor/netology-frontend:0.1
        ports:
        - containerPort: 80
        env:
          - name: BASE_URL
            value: http://backend:9000
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
  labels:
    app: backend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: ecriptor/netology-backend:0.1
        ports:
        - containerPort: 9000
        env:
          - name: DATABASE_URL
            value: postgres://postgres:postgres@db:5432/news
        
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db
spec:
  selector:
    matchLabels:
      app: db
  serviceName: "db-postgres"
  replicas: 1
  template:
    metadata:
      labels:
        app: db
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: db
        image: postgres:13-alpine
        ports:
        - containerPort: 5432
        env:
          - name: POSTGRES_PASSWORD
            value: postgres
          - name: POSTGRES_USER
            value: postgres
          - name: POSTGRES_DB
            value: news
---
apiVersion: v1
kind: Service
metadata:
  name: frontend
spec:
  selector:
    app: frontend
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: backend
spec:
  selector:
    app: backend
  ports:
    - protocol: TCP
      port: 9000
      targetPort: 9000
---
apiVersion: v1
kind: Service
metadata:
  name: db
spec:
  selector:
    app: db
  ports:
    - protocol: TCP
      port: 5432
      targetPort: 5432
```
```shell
root@master-0001:~# kubectl apply -f front-back-db-prod.yml
deployment.apps/frontend created
deployment.apps/backend created
statefulset.apps/db created
service/frontend created
service/backend created
service/db created

root@master-0001:~# kubectl get deploy
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
backend      1/1     1            1           8s
frontend     1/1     1            1           8s
hello-node   1/1     1            1           13d

root@master-0001:~# kubectl get statefulsets.apps
NAME   READY   AGE
db     1/1     21s

root@master-0001:~# kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
backend-65c4dbd9f4-szr2d      1/1     Running   0          27s
db-0                          1/1     Running   0          27s
frontend-99b857b9-wpvm8       1/1     Running   0          27s
hello-node-7567d9fdc9-ppht5   1/1     Running   0          13d

root@master-0001:~# kubectl get service
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
backend      ClusterIP   10.233.58.20    <none>        9000/TCP   45s
db           ClusterIP   10.233.41.171   <none>        5432/TCP   45s
frontend     ClusterIP   10.233.2.34     <none>        8000/TCP   45s
kubernetes   ClusterIP   10.233.0.1      <none>        443/TCP    14d
```

## Задание 3 (*): добавить endpoint на внешний ресурс api
Приложению потребовалось внешнее api, и для его использования лучше добавить endpoint в кластер, направленный на это api. Требования:
* добавлен endpoint до внешнего api (например, геокодер).

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

В качестве решения прикрепите к ДЗ конфиг файлы для деплоя. Прикрепите скриншоты вывода команды kubectl со списком запущенных объектов каждого типа (pods, deployments, statefulset, service) или скриншот из самого Kubernetes, что сервисы подняты и работают.

---
