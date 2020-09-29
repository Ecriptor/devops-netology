# Ответы на вопросы

## Задача 1

* 100 виртуальных машин на базе Linux и Windows, общие задачи, нет особых требований. Преимущественно Windows based инфраструктура, требуется реализация программных балансировщиков нагрузки, репликации данных и автоматизированного механизма создания резервных копий.<br>
Если в основном Windows то подойдет **Hyper-V** c паравиртуализацией будет хорошая поддержка Windows машин или можно **VMware vSphere** будет меньше проблем с Linux машинами, но не будет работать паравиртуализация для Windows машин или **oVirt с отдельным гипервизором**, но тут только снапшоты неплохо работают, а в остальном не хуже VMware, только бесплатно.<p>
* Требуется наиболее производительное бесплатное opensource решение для виртуализации небольшой (20 серверов) инфраструктуры Linux и Windows виртуальных машин.<br>
 **KVM** отлично подойдет oVirt instance all-in-one.<p> 
* Необходимо бесплатное, максимально совместимое и производительное решение для виртуализации Windows инфраструктуры.<br>
 **Hyper-V** если есть лицензионная Windows 10 или **KVM**.<p>
* Необходимо рабочее окружение для тестирование программного продукта на нескольких дистрибутивах Linux.<br>
 **Vagrant** подойдет, но думаю лучше даже будет **Docker Container**.<p>


## Задача 2

1. Удалить с ВМ VMware Tools, выключить ВМ
2. Конвертировать диск при помощи V2V Converter в формат Hyper-V VHDX
3. Перенести сконвертированный диск на виртуализацию Hyper-V
4. Создать ВМ на виртуализации Hyper-V с необходимыми ресурсами (CPU,RAM,HDD)
5. Произвести запуск ВМ проверить что все работает без системных ошибок, установить тулзы Hyper-V 
6. Настроить сетевое взаимодействие и проверить
7. Удалить ВМ на VMware виртуализации

# Задача 3

Основная проблема это обслуживание нескольких систем виртуализации и поддержка внешних систем хранения(например одна система виртуализации поддерживает CEPH а другая нет), но тут можно более оптимизировать и распределить ВМ по разным системам виртуализации в зависимости от требований ОС и оптимизации самой системы виртуализации под определенную ОС. Можно еще можно сказать отказоустойчивость=)<br>
Я бы выбрал единую систему виртуализации с несколькими гипервизорами, изучив кол-во дистрибутивов ОС и требования к ВМ. 
