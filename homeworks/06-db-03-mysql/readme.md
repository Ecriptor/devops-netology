# Ответы на вопросы

## Задача 1

Найдите команду для выдачи статуса БД и приведите в ответе из ее вывода версию сервера БД.
```
mysql> \s
```
```
--------------
mysql  Ver 8.0.22 for Linux on x86_64 (MySQL Community Server - GPL)

```
Подключитесь к восстановленной БД и получите список таблиц из этой БД.
```
mysql> USE test_db
mysql> SHOW TABLES;
```
```
+-------------------+
| Tables_in_test_db |
+-------------------+
| orders            |
+-------------------+
1 row in set (0.01 sec)
```

Приведите в ответе количество записей с price > 300.
```
SELECT * FROM orders WHERE price > 300;
```
```
+----+----------------+-------+
| id | title          | price |
+----+----------------+-------+
|  2 | My little pony |   500 |
+----+----------------+-------+
1 row in set (0.00 sec)
```
## Задача 2

Создайте пользователя test в БД c паролем test-pass, используя:

* плагин авторизации mysql_native_password
* срок истечения пароля - 180 дней
* количество попыток авторизации - 3
* максимальное количество запросов в час - 100
* аттрибуты пользователя:
	* Фамилия "Pretty"
	* Имя "James"
```
mysql> CREATE USER 'test'@'%' IDENTIFIED WITH mysql_native_password BY 'test-pass'
WITH MAX_QUERIES_PER_HOUR 100
PASSWORD EXPIRE INTERVAL 180 DAY
FAILED_LOGIN_ATTEMPTS 3
ATTRIBUTE '{"fname": "James", "lname": "Pretty "}';
Query OK, 0 rows affected (0.02 sec)
```
Предоставьте привелегии пользователю test на операции SELECT базы test_db
```
mysql> GRANT SELECT ON test_db.* TO 'test'@'%';
Query OK, 0 rows affected (0.00 sec)
```
Используя таблицу INFORMATION_SCHEMA.USER_ATTRIBUTES получите данные по пользователю test и приведите в ответе к задаче.
```
mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES WHERE USER='test';
```
```
+------+------+----------------------------------------+
| USER | HOST | ATTRIBUTE                              |
+------+------+----------------------------------------+
| test | %    | {"fname": "James", "lname": "Pretty "} |
+------+------+----------------------------------------+
1 row in set (0.00 sec)
```

## Задача 3
pass
## Задача 4
pass
