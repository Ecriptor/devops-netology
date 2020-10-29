# Ответы на вопросы

## Задача 1

* Docker-compose манифест
```
version: '3'
services:
  postgres-server:
    container_name: postgres12
    image: postgres:12.4
    volumes:
      - "./db-data:/var/lib/postgresql/data"
      - "./db-backup:/db_backup"
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres

```
## Задача 2

* создайте пользователя test-admin-user и БД test_db
```
test_db=# create database testdb ;
CREATE DATABASE
test_db=# create user "test-admin-user" with password 'password' ;
CREATE ROLE

```
* в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)
```
test_db=# create table orders(
id integer primary key,
"наименование" text,
"цена" integer
);
CREATE TABLE

test_db=# create table clients(
id integer primary key,
"фамилия" text,
"страна проживания" text,
"заказ" integer references orders(id)
);
CREATE TABLE

create index index_leave_country on clients using btree ("страна проживания") ;
CREATE INDEX
```
* предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db
```
test_db=# grant ALL on DATABASE test_db TO "test-admin-user";
GRANT
```
* создайте пользователя test-simple-user
```
test_db=# create user "test-simple-user" with password 'password' ;
CREATE ROLE

```
* предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db
```
test_db=# grant INSERT, SELECT, UPDATE, DELETE on TABLE orders TO "test-simple-user";
GRANT
test_db=# grant INSERT, SELECT, UPDATE, DELETE on TABLE clients TO "test-simple-user";
GRANT
```
Приведите:
* итоговый список БД после выполнения пунктов выше
```
test_db=# \l
                                     List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |       Access privileges        
-----------+----------+----------+------------+------------+--------------------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 qqq       | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                   +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                   +
           |          |          |            |            | postgres=CTc/postgres
 test_db   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =Tc/postgres                  +
           |          |          |            |            | postgres=CTc/postgres         +
           |          |          |            |            | "test-admin-user"=CTc/postgres
(5 rows)
```
* описание таблиц (describe)
```
test_db=# \d orders;
                  Table "public.orders"
    Column    |  Type   | Collation | Nullable | Default 
--------------+---------+-----------+----------+---------
 id           | integer |           | not null | 
 наименование | text    |           |          | 
 цена         | integer |           |          | 
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "clients" CONSTRAINT "clients_заказ_fkey" FOREIGN KEY ("заказ") REFERENCES orders(id)

test_db=# \d clients ;
                    Table "public.clients"
      Column       |  Type   | Collation | Nullable | Default 
-------------------+---------+-----------+----------+---------
 id                | integer |           | not null | 
 фамилия           | text    |           |          | 
 страна проживания | text    |           |          | 
 заказ             | integer |           |          | 
Indexes:
    "clients_pkey" PRIMARY KEY, btree (id)
    "index_leave_country" btree ("страна проживания")
Foreign-key constraints:
    "clients_заказ_fkey" FOREIGN KEY ("заказ") REFERENCES orders(id)
```
* SQL-запрос для выдачи списка пользователей с правами над таблицами test_db
```
test_db=# SELECT table_catalog, table_schema, table_name, privilege_type
FROM information_schema.table_privileges
WHERE grantee = 'test-admin-user';
```
**Как на отдельного пользователя понял, а как на всех не пойму!!!**
* список пользователей с правами над таблицами test_db
```
test_db=# \dp orders
                                      Access privileges
 Schema |  Name  | Type  |         Access privileges          | Column privileges | Policies 
--------+--------+-------+------------------------------------+-------------------+----------
 public | orders | table | postgres=arwdDxt/postgres         +|                   | 
        |        |       | "test-admin-user"=arwdDxt/postgres+|                   | 
        |        |       | "test-simple-user"=arwd/postgres   |                   | 
(1 row)

test_db=# \dp clients 
                                      Access privileges
 Schema |  Name   | Type  |         Access privileges          | Column privileges | Policies 
--------+---------+-------+------------------------------------+-------------------+----------
 public | clients | table | postgres=arwdDxt/postgres         +|                   | 
        |         |       | "test-admin-user"=arwdDxt/postgres+|                   | 
        |         |       | "test-simple-user"=arwd/postgres   |                   | 
(1 row)
```



## Задача 3
Используя SQL синтаксис - наполните таблицы следующими тестовыми данными:

Таблица orders
```
INSERT INTO orders(id,"наименование","цена") VALUES(1,'Шоколад', 10);
INSERT INTO orders(id,"наименование","цена") VALUES (2,'Принтер', 3000);
INSERT INTO orders(id,"наименование","цена") VALUES (3,'Книга', 500);
INSERT INTO orders(id,"наименование","цена") VALUES (4,'Монитор', 7000);
INSERT INTO orders(id,"наименование","цена") VALUES (5,'Гитара', 4000);
```
Таблица clients
```
INSERT INTO clients(id,"фамилия","страна проживания") VALUES (1,'Иванов Иван Иванович','USA');
INSERT INTO clients(id,"фамилия","страна проживания") VALUES (2,'Петров Петр Петрович', 'Canada');
INSERT INTO clients(id,"фамилия","страна проживания") VALUES (3,'Иоганн Себастьян Бах', 'Japan');
INSERT INTO clients(id,"фамилия","страна проживания") VALUES (4,'Ронни Джеймс Дио', 'Russia');
INSERT INTO clients(id,"фамилия","страна проживания") VALUES (5,'Ritchie Blackmore', 'Russia');
```
Используя SQL синтаксис - вычислите количество записей в каждой таблице и приведите в ответе запрос и получившийся результат.
```
test_db=# select count(*) from orders ;
 count 
-------
     5
(1 row)

test_db=# select count(*) from clients ;
 count 
-------
     5
(1 row)

```
## Задача 4
Приведите SQL-запросы для выполнения данных операций.
```
UPDATE clients SET "заказ" = (SELECT id FROM orders WHERE "наименование"='Книга') WHERE "фамилия"='Иванов Иван Иванович';
UPDATE clients SET "заказ" = (SELECT id FROM orders WHERE "наименование"='Монитор') WHERE "фамилия"='Петров Петр Петрович';
UPDATE clients SET "заказ" = (SELECT id FROM orders WHERE "наименование"='Гитара') WHERE "фамилия"='Иоганн Себастьян Бах';
```
Приведите SQL-запрос для выдачи всех пользователей, которые совершили заказ, а также вывод данного запроса.
```
SELECT "фамилия" FROM clients WHERE "заказ" IS NOT NULL ;
```
```
       фамилия        
----------------------
 Иванов Иван Иванович
 Петров Петр Петрович
 Иоганн Себастьян Бах
(3 rows)
```
## Задача 5
Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 (используя директиву EXPLAIN).<br>
Приведите получившийся результат и объясните что значат полученные значения.
```
EXPLAIN SELECT "фамилия" FROM clients WHERE "заказ" IS NOT NULL;
```
```
                       QUERY PLAN                       
--------------------------------------------------------
 Seq Scan on clients  (cost=0.00..1.05 rows=3 width=33)
   Filter: ("заказ" IS NOT NULL)
(2 rows)

Seq Scan -- последовательное сканирование
cost=0.00 -- стоимость запуска
cost=1.05 -- общая стоимость
rows=3 -- ожидаемое число строк
width=33 -- средний размер строк в байтах
Filter -- для каждой строки выполняется данное условие
```

## Задача 6
Создайте бэкап БД test_db и поместите его в volume, предназначенный для бэкапов (см. Задачу 1).
```
pg_dump test_db -U postgres > /db_backup/test_db_backup.sql
```
Остановите контейнер с PostgreSQL (но не удаляйте volumes).
```
docker-compose stop
```
Поднимите новый пустой контейнер с PostgreSQL.<br>
Создаем новый docker-compose файл для другого экземплра postgres изменяем volume для data

```
version: '3'
services:
  postgres-server2:
    container_name: postgres12_2
    image: postgres:12.4
    volumes:
      - "/db-data2:/var/lib/postgresql/data"
      - "/db-backup:/db_backup"
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
```
```
docker-compose up -d
```
Восстановите БД test_db в новом контейнере.<br>
Приведите список операций, который вы применяли для бэкапа данных и восстановления.
```
postgres=# create database db_test ;
CREATE DATABASE
postgres=# create user "test-simple-user" with password 'password' ;
CREATE ROLE
postgres=# create user "test-admin-user" with password 'password' ;
CREATE ROLE
psql -U postgres -d db_test -f /db_backup/test_db_backup.sql
```
Это как один из  вариантов бекапа, еще можно ипользовать pg_basebackup или можно копированием volume.
