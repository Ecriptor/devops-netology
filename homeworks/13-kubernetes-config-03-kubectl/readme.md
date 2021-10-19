# Домашнее задание к занятию "13.3 работа с kubectl"
## Задание 1: проверить работоспособность каждого компонента
Для проверки работы можно использовать 2 способа: port-forward и exec. Используя оба способа, проверьте каждый компонент:
* сделайте запросы к бекенду;
* сделайте запросы к фронту;
* подключитесь к базе данных.

```shell
root@master-0001:~# kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
backend-65c4dbd9f4-777s5              1/1     Running   0          14s
db-0                                  1/1     Running   0          13s
frontend-99b857b9-cgp9n               1/1     Running   0          14s
hello-node-7567d9fdc9-ppht5           1/1     Running   0          13d
nfs-server-nfs-server-provisioner-0   1/1     Running   0          58m

root@master-0001:~# kubectl exec -it backend-65c4dbd9f4-777s5 -- curl localhost:9000
{"detail":"Not Found"}

root@master-0001:~# kubectl exec -it frontend-99b857b9-cgp9n -- curl localhost:80
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Список</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="/build/main.css" rel="stylesheet">
</head>
<body>
    <main class="b-page">
        <h1 class="b-page__title">Список</h1>
        <div class="b-page__content b-items js-list"></div>
    </main>
    <script src="/build/main.js"></script>
</body>
</html>

root@master-0001:~# kubectl exec -it db-0 -- psql -U postgres
psql (13.4)
Type "help" for help.

postgres=#
```
Port forward
```shell
root@master-0001:~# kubectl get svc
NAME                                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                                                                                                     AGE
backend                             ClusterIP   10.233.23.17    <none>        9000/TCP                                                                                                    9m24s
db                                  ClusterIP   10.233.15.50    <none>        5432/TCP                                                                                                    9m24s
frontend                            ClusterIP   10.233.44.176   <none>        8000/TCP                                                                                                    9m25s
kubernetes                          ClusterIP   10.233.0.1      <none>        443/TCP                                                                                                     14d
nfs-server-nfs-server-provisioner   ClusterIP   10.233.15.218   <none>        2049/TCP,2049/UDP,32803/TCP,32803/UDP,20048/TCP,20048/UDP,875/TCP,875/UDP,111/TCP,111/UDP,662/TCP,662/UDP   68m

root@master-0001:~# kubectl port-forward svc/frontend 8001:8000 &
[1] 3649696
root@master-0001:~# Forwarding from 127.0.0.1:8001 -> 80
Forwarding from [::1]:8001 -> 80

root@master-0001:~# curl localhost:8001
Handling connection for 8001
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>Список</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="/build/main.css" rel="stylesheet">
</head>
<body>
    <main class="b-page">
        <h1 class="b-page__title">Список</h1>
        <div class="b-page__content b-items js-list"></div>
    </main>
    <script src="/build/main.js"></script>
</body>
</html>

root@master-0001:~# kubectl port-forward svc/backend 9001:9000 &
[2] 3651694
root@master-0001:~# Forwarding from 127.0.0.1:9001 -> 9000
Forwarding from [::1]:9001 -> 9000

root@master-0001:~# curl localhost:9001
Handling connection for 9001

root@master-0001:~# kubectl port-forward svc/db 5432:5432 &
[3] 3657369
root@master-0001:~# Forwarding from 127.0.0.1:5432 -> 5432
Forwarding from [::1]:5432 -> 5432

root@master-0001:~# psql -h localhost -p 5432 -U postgres
Handling connection for 5432
psql (12.8 (Ubuntu 12.8-0ubuntu0.20.04.1), server 13.4)
WARNING: psql major version 12, server major version 13.
         Some psql features might not work.
Type "help" for help.

postgres=#
```

## Задание 2: ручное масштабирование
При работе с приложением иногда может потребоваться вручную добавить пару копий. Используя команду kubectl scale, попробуйте увеличить количество бекенда и фронта до 3. После уменьшите количество копий до 1. Проверьте, на каких нодах оказались копии после каждого действия (kubectl describe).
```shell
root@master-0001:~# kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
backend-65c4dbd9f4-777s5              1/1     Running   0          24m
db-0                                  1/1     Running   0          24m
frontend-99b857b9-cgp9n               1/1     Running   0          24m
hello-node-7567d9fdc9-ppht5           1/1     Running   0          13d
nfs-server-nfs-server-provisioner-0   1/1     Running   0          83m

root@master-0001:~# kubectl scale --replicas=3 deployment/frontend
deployment.apps/frontend scaled
root@master-0001:~# kubectl scale --replicas=3 deployment/backend
deployment.apps/backend scaled

root@master-0001:~# kubectl get pods
NAME                                  READY   STATUS              RESTARTS   AGE
backend-65c4dbd9f4-777s5              1/1     Running             0          26m
backend-65c4dbd9f4-b6w7r              0/1     Pending             0          3s
backend-65c4dbd9f4-cxmsp              0/1     Pending             0          3s
db-0                                  1/1     Running             0          25m
frontend-99b857b9-6nv57               0/1     ContainerCreating   0          11s
frontend-99b857b9-cb4xd               0/1     ContainerCreating   0          11s
frontend-99b857b9-cgp9n               1/1     Running             0          26m
hello-node-7567d9fdc9-ppht5           1/1     Running             0          13d
nfs-server-nfs-server-provisioner-0   1/1     Running             0          84m

root@master-0001:~# kubectl scale --replicas=1 deployment/backend
deployment.apps/backend scaled
root@master-0001:~# kubectl scale --replicas=1 deployment/frontend
deployment.apps/frontend scaled

root@master-0001:~# kubectl get pods
NAME                                  READY   STATUS        RESTARTS   AGE
backend-65c4dbd9f4-777s5              1/1     Running       0          26m
backend-65c4dbd9f4-b6w7r              0/1     Terminating   0          55s
backend-65c4dbd9f4-cxmsp              0/1     Terminating   0          55s
db-0                                  1/1     Running       0          26m
frontend-99b857b9-6nv57               0/1     Terminating   0          63s
frontend-99b857b9-cb4xd               0/1     Terminating   0          63s
frontend-99b857b9-cgp9n               1/1     Running       0          26m
hello-node-7567d9fdc9-ppht5           1/1     Running       0          13d
```
kubectl get pods -o wide выдаст более подробную информацию
```shell
root@master-0001:~# kubectl get pods -o wide
NAME                                  READY   STATUS              RESTARTS        AGE    IP              NODE        NOMINATED NODE   READINESS GATES
backend-65c4dbd9f4-6mnq9              0/1     ContainerCreating   0               33s    <none>          node-0001   <none>           <none>
backend-65c4dbd9f4-777s5              1/1     Running             0               30m    10.233.105.19   node-0001   <none>           <none>
backend-65c4dbd9f4-hfw5p              0/1     ContainerCreating   0               33s    <none>          node-0001   <none>           <none>
db-0                                  1/1     Running             0               30m    10.233.105.18   node-0001   <none>           <none>
frontend-99b857b9-cgp9n               1/1     Running             0               30m    10.233.105.20   node-0001   <none>           <none>
frontend-99b857b9-dn7zp               0/1     Pending             0               27s    <none>          node-0001   <none>           <none>
frontend-99b857b9-tpdfz               0/1     Pending             0               27s    <none>          node-0001   <none>           <none>
```
Или через kubectl describe
```shell
root@master-0001:~# kubectl describe pods backend | grep "Node: "
Node:         node-0001/192.168.1.11
Node:         node-0001/192.168.1.11
Node:         node-0001/192.168.1.11
```

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
