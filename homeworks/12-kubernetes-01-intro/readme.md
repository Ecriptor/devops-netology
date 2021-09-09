# Домашнее задание к занятию "12.1 Компоненты Kubernetes"

## Задача 1: Установить Minikube
- Проверить версию можно командой minikube version
```
root@kuber1:~# minikube version
minikube version: v1.23.0
commit: 5931455374810b1bbeb222a9713ae2c756daee10
```
- Переключаемся на root и запускаем миникуб: minikube start --vm-driver=none
```
root@kuber1:~# minikube start --vm-driver=none
😄  minikube v1.23.0 on Ubuntu 20.04 (amd64)
✨  Using the none driver based on user configuration
👍  Starting control plane node minikube in cluster minikube
🤹  Running on localhost (CPUs=2, Memory=3935MB, Disk=40252MB) ...
ℹ️  OS release is Ubuntu 20.04.1 LTS
🐳  Preparing Kubernetes v1.22.1 on Docker 20.10.7 ...
...
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```
- После запуска стоит проверить статус: minikube status
```
root@kuber1:~# minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```
- Запущенные служебные компоненты можно увидеть командой: kubectl get pods --namespace=kube-system
```
root@kuber1:~# kubectl get pods --namespace=kube-system
NAME                             READY   STATUS    RESTARTS   AGE
coredns-78fcd69978-4x4rk         1/1     Running   0          27s
etcd-kuber1                      1/1     Running   0          40s
kube-apiserver-kuber1            1/1     Running   0          40s
kube-controller-manager-kuber1   1/1     Running   0          39s
kube-proxy-v2dcg                 1/1     Running   0          27s
kube-scheduler-kuber1            1/1     Running   0          40s
storage-provisioner              1/1     Running   0          39s
```

## Задача 2: Запуск Hello World
После установки Minikube требуется его проверить. Для этого подойдет стандартное приложение hello world. А для доступа к нему потребуется ingress.

- развернуть через Minikube тестовое приложение по [туториалу](https://kubernetes.io/ru/docs/tutorials/hello-minikube/#%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BA%D0%BB%D0%B0%D1%81%D1%82%D0%B5%D1%80%D0%B0-minikube)
```
root@kuber1:~# kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4
deployment.apps/hello-node created
root@kuber1:~# kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
hello-node   1/1     1            1           10s
root@kuber1:~# kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
hello-node-7567d9fdc9-rnf4c   1/1     Running   0          23s
root@kuber1:~# kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /root/.minikube/ca.crt
    extensions:
    - extension:
        last-update: Thu, 09 Sep 2021 19:52:38 MSK
        provider: minikube.sigs.k8s.io
        version: v1.23.0
      name: cluster_info
    server: https://192.168.1.232:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Thu, 09 Sep 2021 19:52:38 MSK
        provider: minikube.sigs.k8s.io
        version: v1.23.0
      name: context_info
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /root/.minikube/profiles/minikube/client.crt
    client-key: /root/.minikube/profiles/minikube/client.key
root@kuber1:~# kubectl expose deployment hello-node --type=LoadBalancer --port=8080
service/hello-node exposed
root@kuber1:~# kubectl get services
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
hello-node   LoadBalancer   10.100.191.161   <pending>     8080:30824/TCP   10s
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          34m
```
- установить аддоны ingress и dashboard
```
root@kuber1:~# minikube addons enable ingress
    ▪ Using image k8s.gcr.io/ingress-nginx/controller:v1.0.0-beta.3
    ▪ Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.0
    ▪ Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.0
🔎  Verifying ingress addon...
root@kuber1:~# minikube addons list
|-----------------------------|----------|--------------|-----------------------|
|         ADDON NAME          | PROFILE  |    STATUS    |      MAINTAINER       |
|-----------------------------|----------|--------------|-----------------------|
| ambassador                  | minikube | disabled     | unknown (third-party) |
| auto-pause                  | minikube | disabled     | google                |
| csi-hostpath-driver         | minikube | disabled     | kubernetes            |
| dashboard                   | minikube | enabled ✅   | kubernetes            |
| default-storageclass        | minikube | enabled ✅   | kubernetes            |
| efk                         | minikube | disabled     | unknown (third-party) |
| freshpod                    | minikube | disabled     | google                |
| gcp-auth                    | minikube | disabled     | google                |
| gvisor                      | minikube | disabled     | google                |
| helm-tiller                 | minikube | disabled     | unknown (third-party) |
| ingress                     | minikube | enabled ✅   | unknown (third-party) |
| ingress-dns                 | minikube | disabled     | unknown (third-party) |
| istio                       | minikube | disabled     | unknown (third-party) |
| istio-provisioner           | minikube | disabled     | unknown (third-party) |
| kubevirt                    | minikube | disabled     | unknown (third-party) |
| logviewer                   | minikube | disabled     | google                |
| metallb                     | minikube | disabled     | unknown (third-party) |
| metrics-server              | minikube | disabled     | kubernetes            |
| nvidia-driver-installer     | minikube | disabled     | google                |
| nvidia-gpu-device-plugin    | minikube | disabled     | unknown (third-party) |
| olm                         | minikube | disabled     | unknown (third-party) |
| pod-security-policy         | minikube | disabled     | unknown (third-party) |
| portainer                   | minikube | disabled     | portainer.io          |
| registry                    | minikube | disabled     | google                |
| registry-aliases            | minikube | disabled     | unknown (third-party) |
| registry-creds              | minikube | disabled     | unknown (third-party) |
| storage-provisioner         | minikube | enabled ✅   | kubernetes            |
| storage-provisioner-gluster | minikube | disabled     | unknown (third-party) |
| volumesnapshots             | minikube | disabled     | kubernetes            |
|-----------------------------|----------|--------------|-----------------------|
```

## Задача 3: Установить kubectl

Подготовить рабочую машину для управления корпоративным кластером. Установить клиентское приложение kubectl.
- подключиться к minikube
```
root@kuber1:~# kubectl version --client
Client Version: version.Info{Major:"1", Minor:"22", GitVersion:"v1.22.1", GitCommit:"632ed300f2c34f6d6d15ca4cef3d3c7073412212", GitTreeState:"clean", BuildDate:"2021-08-19T15:45:37Z", GoVersion:"go1.16.7", Compiler:"gc", Platform:"linux/amd64"}
``` 
- проверить работу приложения из задания 2, запустив port-forward до кластера
```
root@kuber1:~# kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
hello-node-7567d9fdc9-rnf4c   1/1     Running   0          12m
root@kuber1:~# kubectl port-forward hello-node-7567d9fdc9-rnf4c 8080:8080
Forwarding from 127.0.0.1:8080 -> 8080
Forwarding from [::1]:8080 -> 8080
```

## Задача 4 (*): собрать через ansible (необязательное)
