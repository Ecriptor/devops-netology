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
Установите профилирование SET profiling = 1. Изучите вывод профилирования команд SHOW PROFILES;.
```
mysql> SET profiling = 1;
Query OK, 0 rows affected, 1 warning (0.00 sec)
```
Исследуйте, какой engine используется в таблице БД test_db и приведите в ответе.
```
mysql> SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES where TABLE_SCHEMA = 'test_db';
```
```
+------------+--------+
| TABLE_NAME | ENGINE |
+------------+--------+
| orders     | InnoDB |
+------------+--------+
1 row in set (0.00 sec)
```
Измените engine и приведите время выполнения и запрос на изменения из профайлера в ответе:
* на MyISAM
* на InnoDB
```
ALTER TABLE orders ENGINE = MyISAM;
```
```
+------------+--------+
| TABLE_NAME | ENGINE |
+------------+--------+
| orders     | MyISAM |
+------------+--------+
1 row in set (0.01 sec)
```
Для отображения времени отображения
```
SHOW PROFILES;
```
```
+----------+------------+-----------------------------------------------------------------------------------------+
| Query_ID | Duration   | Query                                                                                   |
+----------+------------+-----------------------------------------------------------------------------------------+
|       12 | 0.00136775 | SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES where TABLE_SCHEMA = 'test_db' |
|       13 | 0.02542700 | ALTER TABLE orders ENGINE = MyISAM                                                      |
|       14 | 0.00219075 | SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES where TABLE_SCHEMA = 'test_db' |
+----------+------------+-----------------------------------------------------------------------------------------+
14 rows in set, 1 warning (0.00 sec)
```
Для просмотра более детальной информации
```
mysql> SHOW PROFILE FOR QUERY 14;
```
```
+--------------------------------+----------+
| Status                         | Duration |
+--------------------------------+----------+
| starting                       | 0.000103 |
| Executing hook on transaction  | 0.000007 |
| starting                       | 0.000008 |
| checking permissions           | 0.000007 |
| Opening tables                 | 0.001012 |
| init                           | 0.000033 |
| System lock                    | 0.000020 |
| optimizing                     | 0.000075 |
| statistics                     | 0.000270 |
| preparing                      | 0.000163 |
| executing                      | 0.000228 |
| checking permissions           | 0.000056 |
| end                            | 0.000009 |
| query end                      | 0.000006 |
| waiting for handler commit     | 0.000013 |
| closing tables                 | 0.000021 |
| freeing items                  | 0.000131 |
| cleaning up                    | 0.000030 |
+--------------------------------+----------+
18 rows in set, 1 warning (0.00 sec)
```
## Задача 4
Изучите файл my.cnf в директории /etc/mysql.<br>
Измените его согласно ТЗ (движок InnoDB):
* Скорость IO важнее сохранности данных
* Нужна компрессия таблиц для экономии места на диске
* Размер буффера с незакомиченными транзакциями 1 Мб
* Буффер кеширования 30% от ОЗУ
* Размер файла логов операций 100 Мб
Приведите в ответе измененный файл my.cnf.
```
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL

#Скорость IO важнее сохранности данных
innodb_flush_log_at_trx_commit = 2
#Нужна компрессия таблиц для экономии места на диске
innodb_file_per_table = ON
#Размер буффера с незакомиченными транзакциями 1 Мб
innodb_log_buffer_size = 1M
#Буффер кеширования 30% от ОЗУ
innodb_buffer_pool_size = 1G
#Размер файла логов операций 100 Мб
innodb_log_file_size = 100M

# Custom config should go here
!includedir /etc/mysql/conf.d/


```

