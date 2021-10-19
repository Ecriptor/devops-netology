# Домашнее задание к занятию "13.2 разделы и монтирование"
Приложение запущено и работает, но время от времени появляется необходимость передавать между бекендами данные. А сам бекенд генерирует статику для фронта. Нужно оптимизировать это.
Для настройки NFS сервера можно воспользоваться следующей инструкцией (производить под пользователем на сервере, у которого есть доступ до kubectl):
* установить helm: curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
* добавить репозиторий чартов: helm repo add stable https://charts.helm.sh/stable && helm repo update
* установить nfs-server через helm: helm install nfs-server stable/nfs-server-provisioner

В конце установки будет выдан пример создания PVC для этого сервера.

```yaml
---
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: test-dynamic-volume-claim
    spec:
      storageClassName: "nfs"
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 100Mi
```

## Задание 1: подключить для тестового конфига общую папку
В stage окружении часто возникает необходимость отдавать статику бекенда сразу фронтом. Проще всего сделать это через общую папку. Требования:
* в поде подключена общая папка между контейнерами (например, /static);
* после записи чего-либо в контейнере с беком файлы можно получить из контейнера с фронтом.
```shell
root@master-0001:~# kubectl apply -f pvc_nfs.yml
persistentvolumeclaim/test-dynamic-volume-claim created
```
Deployment с Volume
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
        volumeMounts:
        - mountPath: /static
          name: static-storage
      - name: backend
        image: ecriptor/netology-backend:0.1
        ports:
        - containerPort: 9000
        volumeMounts:
        - mountPath: /static
          name: static-storage
      volumes:
      - name: static-storage
        persistentVolumeClaim:
          claimName: test-dynamic-volume-claim
```
Проверка
```shell
root@master-0001:~# kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
frontend-backend-6f7d9b554-l7xns      2/2     Running   0          19s
hello-node-7567d9fdc9-ppht5           1/1     Running   0          13d
nfs-server-nfs-server-provisioner-0   1/1     Running   0          30m

root@master-0001:~# kubectl exec -it frontend-backend-6f7d9b554-l7xns -c frontend /bin/bash
root@frontend-backend-6f7d9b554-l7xns:/app# echo test_front > /static/test_front.log
root@frontend-backend-6f7d9b554-l7xns:/app# exit

root@master-0001:~# kubectl exec -it frontend-backend-6f7d9b554-l7xns -c backend /bin/bash
root@frontend-backend-6f7d9b554-l7xns:/app# cat /static/test_front.log
test_front
```

## Задание 2: подключить общую папку для прода
Поработав на stage, доработки нужно отправить на прод. В продуктиве у нас контейнеры крутятся в разных подах, поэтому потребуется PV и связь через PVC. Сам PV должен быть связан с NFS сервером. Требования:
* все бекенды подключаются к одному PV в режиме ReadWriteMany;
* фронтенды тоже подключаются к этому же PV с таким же режимом;
* файлы, созданные бекендом, должны быть доступны фронту.
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
        volumeMounts:
        - mountPath: /static
          name: static-storage
      volumes:
        - name: static-storage
          persistentVolumeClaim:
            claimName: test-dynamic-volume-claim
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
        volumeMounts:
          - mountPath: /static
            name: static-storage
      volumes:
        - name: static-storage
          persistentVolumeClaim:
            claimName: test-dynamic-volume-claim
```
```shell
root@master-0001:~# kubectl get pods
NAME                                  READY   STATUS              RESTARTS   AGE
backend-7f6c6dc544-6mgnw              1/1     Running             0          21s
frontend-5b98fddf7f-8sh2j             1/1     Running             0          21s
hello-node-7567d9fdc9-ppht5           1/1     Running             0          13d
nfs-server-nfs-server-provisioner-0   1/1     Running             0          37m

root@master-0001:~# kubectl exec -it backend-7f6c6dc544-6mgnw /bin/bash
root@backend-7f6c6dc544-6mgnw:/app# echo test_front2 > /static/test_front2.log
root@backend-7f6c6dc544-6mgnw:/app# exit

root@master-0001:~# kubectl exec -it frontend-5b98fddf7f-8sh2j /bin/bash
root@frontend-5b98fddf7f-8sh2j:/app# cat /static/test_front2.log
test_front2
```
---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
