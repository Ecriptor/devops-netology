# Домашнее задание к занятию "12.4 Развертывание кластера на собственных серверах, лекция 2"
Новые проекты пошли стабильным потоком. Каждый проект требует себе несколько кластеров: под тесты и продуктив. Делать все руками — не вариант, поэтому стоит автоматизировать подготовку новых кластеров.

## Задание 1: Подготовить инвентарь kubespray
Новые тестовые кластеры требуют типичных простых настроек. Нужно подготовить инвентарь и проверить его работу. Требования к инвентарю:
* подготовка работы кластера из 5 нод: 1 мастер и 4 рабочие ноды;
* в качестве CRI — containerd;
* запуск etcd производить на мастере.
### Решение

Не получилось реализовать на 5 нодах т.к. моя подписка в облаке не дает создать больше 4 нод, а с пробросом в интернет можно только 2 =((

Поэтому инвентарник вот такой:
![invent.png](invent.png)
Запуск плейбука:
```shell
ansible-playbook -i inventory/netology/inventory.ini cluster.yml -u root
```
Результат выполнения в ansible:
![ansible.png](ansible.png)
Проверка кластера
![result.png](result.png)



## Задание 2 (*): подготовить и проверить инвентарь для кластера в AWS
Часть новых проектов хотят запускать на мощностях AWS. Требования похожи:
* разворачивать 5 нод: 1 мастер и 4 рабочие ноды;
* работать должны на минимально допустимых EC2 — t3.small.
