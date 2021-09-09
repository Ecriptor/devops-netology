# Домашнее задание к занятию "11.01 Микросервисы: принципы"
Для решения необходимо создать конфиг файл nginx и далее запустить docker-compose
- [nginx.conf](gateway/nginx.conf)
## Выполнение
```
$ curl -X POST -H 'Content-Type: application/json' -d '{"login":"bob", "password":"qwe123"}' http://localhost/token
```
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJib2IifQ.hiMVLmssoTsy1MqbmIoviDeFPvo-nCd92d4UFiN2O2I
```

## Загрузка
Использовать полученный токен для загрузки картинки
```
$ curl -X POST -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJib2IifQ.hiMVLmssoTsy1MqbmIoviDeFPvo-nCd92d4UFiN2O2I' -H 'Content-Type: octet/stream' --data-binary @1.jpg http://localhost/upload
```
```
{"filename":"edf205f7-bbf4-4ceb-934f-70bac9323acb.jpg"}
```
## Проверка
```
curl localhost/image/edf205f7-bbf4-4ceb-934f-70bac9323acb.jpg > edf205f7-bbf4-4ceb-934f-70bac9323acb.jpg
```
```
ls
edf205f7-bbf4-4ceb-934f-70bac9323acb.jpg
```
