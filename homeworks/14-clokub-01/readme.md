# Домашнее задание к занятию "14.1 Создание и использование секретов"

## Задача 1: Работа с секретами через утилиту kubectl в установленном minikube

Выполните приведённые ниже команды в консоли, получите вывод команд. Сохраните
задачу 1 как справочный материал.

### Как создать секрет?

```
openssl genrsa -out cert.key 4096
openssl req -x509 -new -key cert.key -days 3650 -out cert.crt \
-subj '/C=RU/ST=Moscow/L=Moscow/CN=server.local'
kubectl create secret tls domain-cert --cert=certs/cert.crt --key=certs/cert.key
```

### Как просмотреть список секретов?

```
kubectl get secrets
kubectl get secret
```

### Как просмотреть секрет?

```
kubectl get secret domain-cert
kubectl describe secret domain-cert
```

### Как получить информацию в формате YAML и/или JSON?

```
kubectl get secret domain-cert -o yaml
kubectl get secret domain-cert -o json
```

### Как выгрузить секрет и сохранить его в файл?

```
kubectl get secrets -o json > secrets.json
kubectl get secret domain-cert -o yaml > domain-cert.yml
```

### Как удалить секрет?

```
kubectl delete secret domain-cert
```

### Как загрузить секрет из файла?

```
kubectl apply -f domain-cert.yml
```
### Результат
Создадим сертификат и добавим в кубер
```shell
root@master-0001:~# openssl genrsa -out cert.key 4096
Generating RSA private key, 4096 bit long modulus (2 primes)
..............................................................++++
...........................++++
e is 65537 (0x010001)

root@master-0001:~# openssl req -x509 -new -key cert.key -days 3650 -out cert.crt \
-subj '/C=RU/ST=Moscow/L=Moscow/CN=server.local'

root@master-0001:~# kubectl create secret tls domain-cert --cert=cert.crt --key=cert.key
secret/domain-cert created
```
Просмотр сикрета
```shell
root@master-0001:~# kubectl get secrets
NAME                                            TYPE                                  DATA   AGE
default-token-l67lp                             kubernetes.io/service-account-token   3      15d
domain-cert                                     kubernetes.io/tls                     2      22s
nfs-server-nfs-server-provisioner-token-vqslr   kubernetes.io/service-account-token   3      24h
sh.helm.release.v1.nfs-server.v1                helm.sh/release.v1                    1      24h

root@master-0001:~# kubectl get secret domain-cert
NAME          TYPE                DATA   AGE
domain-cert   kubernetes.io/tls   2      41s

root@master-0001:~# kubectl describe secret domain-cert
Name:         domain-cert
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type:  kubernetes.io/tls

Data
====
tls.crt:  1944 bytes
tls.key:  3243 byte
```
Получить информацию о сикрете в формате YAML
```yaml
kubectl get secret domain-cert -o yaml
apiVersion: v1
data:
  tls.crt: LS0tL...
  tls.key: LS0tL...
kind: Secret
metadata:
  creationTimestamp: "2021-10-20T19:56:46Z"
  name: domain-cert
  namespace: default
  resourceVersion: "1998480"
  uid: 8e595b7d-1ff5-4bfd-be8e-96eb7a6993e2
type: kubernetes.io/tls
```
Получить информацию о сикрете в формате JSON
```json
root@master-0001:~# kubectl get secret domain-cert -o json
{
    "apiVersion": "v1",
    "data": {
        "tls.crt": "LS0tL...",
        "tls.key": "LS0tL..."
    },
    "kind": "Secret",
    "metadata": {
        "creationTimestamp": "2021-10-20T19:56:46Z",
        "name": "domain-cert",
        "namespace": "default",
        "resourceVersion": "1998480",
        "uid": "8e595b7d-1ff5-4bfd-be8e-96eb7a6993e2"
    },
    "type": "kubernetes.io/tls"
}
```
Эксопрт сикретов
```shell
root@master-0001:~# kubectl get secrets -o json > secrets.json
root@master-0001:~# kubectl get secret domain-cert -o yaml > domain-cert.yml
root@master-0001:~# ll
total 164
drwx------ 10 root root  4096 Oct 20 23:10 ./
drwxr-xr-x 19 root root  4096 Oct  5 16:39 ../
drwx------  3 root root  4096 Oct  5 17:10 .ansible/
-rw-r--r--  1 root root  7166 Oct 20 23:10 domain-cert.yml
-rw-r--r--  1 root root 36591 Oct 20 23:09 secrets.json
drwx------  2 root root  4096 Oct  5 16:39 .ssh/
-rw-------  1 root root 22754 Oct 19 23:14 .viminfo
```
Удалить сикрет
```shell
root@master-0001:~# kubectl delete secret domain-cert
secret "domain-cert" deleted
```
Импорт сикрета из файла
```shell
root@master-0001:~# kubectl apply -f domain-cert.yml
secret/domain-cert created
```

## Задача 2 (*): Работа с секретами внутри модуля

Выберите любимый образ контейнера, подключите секреты и проверьте их доступность
как в виде переменных окружения, так и в виде примонтированного тома.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

В качестве решения прикрепите к ДЗ конфиг файлы для деплоя. Прикрепите скриншоты вывода команды kubectl со списком запущенных объектов каждого типа (deployments, pods, secrets) или скриншот из самого Kubernetes, что сервисы подняты и работают, а также вывод из CLI.

---
