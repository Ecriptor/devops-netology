# Домашнее задание к занятию "11.03 Микросервисы: подходы"
Обновил файл docker-compose
- [Репо с docker-compose](https://github.com/Ecriptor/devops-netology/blob/master/homeworks/11-microservices-02-principles/)
Добавил в docker-compose  prometheus и grafana
```
####### MONITORING #######
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus:/etc/prometheus
    ports:
      - 9090:9090
    expose:
      - 9090

  grafana:
    image: grafana/grafana
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=qwerty123456
      - GF_USERS_ALLOW_SIGN_UP=false
    volumes:
      - ./grafana/:/var/lib/grafana/
    ports:
      - 8081:3000
    expose:
      - 3000
```
Для prometheus добавил сбор метрик
```
- job_name: 'storage'
    scrape_interval: 5s
    metrics_path: /minio/v2/metrics/cluster
    bearer_token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJib2IifQ.hiMVLmssoTsy1MqbmIoviDeFPvo-nCd92d4UFiN2O2I
    static_configs:
      - targets: ['storage:9000']
```
Лог из контейнера, что метрика опрашивается
```
security_1       | 172.25.0.5 - - [08/Sep/2021 18:25:26] "GET /metrics HTTP/1.1" 200 -
security_1       | 172.25.0.5 - - [08/Sep/2021 18:25:41] "GET /metrics HTTP/1.1" 200 -
security_1       | 172.25.0.5 - - [08/Sep/2021 18:25:56] "GET /metrics HTTP/1.1" 200 -
security_1       | 172.25.0.5 - - [08/Sep/2021 18:26:11] "GET /metrics HTTP/1.1" 200 -
```
![Screenshot](grafana.png)
---
![Screenshot](prometheus.png)
