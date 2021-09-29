# Домашнее задание к занятию "12.2 Команды для работы с Kubernetes"
Кластер — это сложная система, с которой крайне редко работает один человек. Квалифицированный devops умеет наладить работу всей команды, занимающейся каким-либо сервисом.
После знакомства с кластером вас попросили выдать доступ нескольким разработчикам. Помимо этого требуется служебный аккаунт для просмотра логов.

## Задание 1: Запуск пода из образа в деплойменте
Для начала следует разобраться с прямым запуском приложений из консоли. Такой подход поможет быстро развернуть инструменты отладки в кластере. Требуется запустить деплоймент на основе образа из hello world уже через deployment. Сразу стоит запустить 2 копии приложения (replicas=2). 

Требования:
 * пример из hello world запущен в качестве deployment
 * количество реплик в deployment установлено в 2
 * наличие deployment можно проверить командой kubectl get deployment
 * наличие подов можно проверить командой kubectl get pods
```shell
root@kuber1:~# kubectl scale --replicas=2 deployment/hello-node
deployment.apps/hello-node scaled
root@kuber1:~# kubectl get services
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
hello-node   LoadBalancer   10.100.191.161   <pending>     8080:30824/TCP   12h
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          13h
root@kuber1:~# kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
hello-node-7567d9fdc9-6n2jk   1/1     Running   0          7s
hello-node-7567d9fdc9-rnf4c   1/1     Running   0          12h
root@kuber1:~# kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
hello-node   2/2     2            2           12h
```

## Задание 2: Просмотр логов для разработки
Разработчикам крайне важно получать обратную связь от штатно работающего приложения и, еще важнее, об ошибках в его работе. 
Требуется создать пользователя и выдать ему доступ на чтение конфигурации и логов подов в app-namespace.

Требования: 
 * создан новый токен доступа для пользователя
 * пользователь прописан в локальный конфиг (~/.kube/config, блок users)
 * пользователь может просматривать логи подов и их конфигурацию (kubectl logs pod <pod_id>, kubectl describe pod <pod_id>)

### Решение!
Создаем пользователя
```shell
root@kuber1:~# kubectl create serviceaccount dev-user
serviceaccount/dev-user created
```
Привязываем к роли
```shell
root@kuber1:~# kubectl create rolebinding log-viewer --clusterrole=view --serviceaccount=default:dev-user --namespace=default
rolebinding.rbac.authorization.k8s.io/log-viewer created
```
Создаем токен для пользователя
```shell
root@kuber1:~# cat <<EOF | kubectl apply -f -
> apiVersion: v1
> kind: Secret
> metadata:
>   name: dev-user
>   annotations:
>     kubernetes.io/service-account.name: dev-user
> type: kubernetes.io/service-account-token
> EOF
secret/dev-user created
```
Просматриваем токен
```shell
root@kuber1:~# kubectl describe secret/dev-user
Name:         dev-user
Namespace:    default
Labels:       <none>
Annotations:  kubernetes.io/service-account.name: dev-user
              kubernetes.io/service-account.uid: 34183271-dd0d-4c48-84b5-209b1faa48f3

Type:  kubernetes.io/service-account-token

Data
====
ca.crt:     1111 bytes
namespace:  7 bytes
token:      eyJ...aZg
```
Добавляем пользователя в конфиг
```shell
root@kuber1:~# kubectl config set-credentials dev-user --token eyJ...aZg
User "dev-user" set.
```
Переключаемся на пользователя
```shell
root@kuber1:~# kubectl config set-context minikube --user dev-user
Context "minikube" modified.
root@kuber1:~# kubectl config use-context minikube
Switched to context "minikube".
```
Проверяем, что все работает как и задумывалось
```shell
root@kuber1:~# kubectl get pods
NAME                          READY   STATUS    RESTARTS      AGE
hello-node-7567d9fdc9-62h28   1/1     Running   1 (19d ago)   19d
hello-node-7567d9fdc9-66hbm   1/1     Running   1 (19d ago)   19d
hello-node-7567d9fdc9-6n2jk   1/1     Running   1 (19d ago)   19d
hello-node-7567d9fdc9-ds9hx   1/1     Running   1 (19d ago)   19d
hello-node-7567d9fdc9-rnf4c   1/1     Running   1 (19d ago)   20d
root@kuber1:~# kubectl delete pods/hello-node-7567d9fdc9-62h28
Error from server (Forbidden): pods "hello-node-7567d9fdc9-62h28" is forbidden: User "system:serviceaccount:default:dev-user" cannot delete resource "pods" in API group "" in the namespace "default"
```

## Задание 3: Изменение количества реплик 
Поработав с приложением, вы получили запрос на увеличение количества реплик приложения для нагрузки. Необходимо изменить запущенный deployment, увеличив количество реплик до 5. Посмотрите статус запущенных подов после увеличения реплик. 

Требования:
 * в deployment из задания 1 изменено количество реплик на 5
 * проверить что все поды перешли в статус running (kubectl get pods)
```shell
root@kuber1:~# kubectl scale --replicas=5 deployment/hello-node
deployment.apps/hello-node scaled
root@kuber1:~# kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
hello-node-7567d9fdc9-62h28   1/1     Running   0          2s
hello-node-7567d9fdc9-66hbm   1/1     Running   0          2s
hello-node-7567d9fdc9-6n2jk   1/1     Running   0          3m56s
hello-node-7567d9fdc9-ds9hx   1/1     Running   0          2s
hello-node-7567d9fdc9-rnf4c   1/1     Running   0          12h
```
