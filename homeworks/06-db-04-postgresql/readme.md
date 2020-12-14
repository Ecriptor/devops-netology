# Ответы на вопросы

## Задача 1

Используя docker поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume.<br>
Подключитесь к БД PostgreSQL используя psql.
```
docker run  --name postgres-server -d -e POSTGRES_PASSWORD=password -v /data/postgres:/var/lib/postgresql/data postgres:13
docker exec -it postgres-server bash
su - postgres
psql
```
Воспользуйтесь командой \? для вывода подсказки по имеющимся в psql управляющим командам.<br>
Найдите и приведите управляющие команды для:<br>
вывода списка БД<br>
подключения к БД<br>
вывода списка таблиц<br>
вывода описания содержимого таблиц<br>
выхода из psql<br>
Подключитесь к восстановленной БД и получите список таблиц из этой БД.
```
\l[+] - вывод списка БД
\c - подключение к БД
\dt[+] - вывод списка таблиц
\d[+] NAME - вывод описания содержимого таблиц
\q - выход из psql
```
## Задача 2

Используя psql создайте БД test_database.
```
create database test_database;
```
Восстановите бэкап БД в test_database.
```
curl -LO https://raw.githubusercontent.com/netology-code/virt-homeworks/master/06-db-04-postgresql/test_data/test_dump.sql
psql test_database < test_dump.sql
```
Перейдите в управляющую консоль psql внутри контейнера.<br>
Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.
```
psql
\c test_database
analyze verbose;
```
Используя таблицу pg_stats столбец таблицы orders с наибольшим средним значением размера элементов в байтах.
Приведите в ответе команду, которую вы использовали для вычисления и полученный результат.
```
select max(avg_width) from pg_stats where tablename='orders';
```

## Задача 3

Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и поиск по ней занимает долгое время. Вам, как успешному выпускнику курсов DevOps в нетологии предложили провести разбиение таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499).<br>
Предложите SQL-транзакцию для проведения данной операции.
```
CREATE TABLE orders_1 (CHECK (price > 499)) INHERITS (orders);
INSERT INTO orders_1 SELECT * FROM orders WHERE price > 499;

CREATE TABLE orders_2 (CHECK (price <= 499)) INHERITS (orders);
INSERT INTO orders_2 SELECT * FROM orders WHERE price <= 499;
```
Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?
```
CREATE RULE order_with_price_more_than_499 AS ON INSERT TO orders WHERE (price > 499) DO INSTEAD INSERT INTO orders_1 VALUES (NEW.*);
CREATE RULE order_with_price_less_than_499 AS ON INSERT TO orders WHERE (price <= 499) DO INSTEAD INSERT INTO orders_2 VALUES (NEW.*);
```

## Задача 4

Используя утилиту pg_dump создайте бекап БД test_database.
```
pg_dump -U postgres test_database > test_database.dump
```
Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца title для таблиц test_database?
```
CREATE TABLE public.orders (
    id integer NOT NULL,
    title character varying(80) UNIQUE NOT NULL,
    price integer DEFAULT 0
);
```
