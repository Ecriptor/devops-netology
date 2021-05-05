# Домашнее задание к занятию "08.04 Создание собственных modules"

Cсылку на репозиторий с collection<br>
[https://github.com/Ecriptor/my_own_collection](https://github.com/Ecriptor/my_own_collection)<br>
Тестовый плейбук:
[test_module_play](https://github.com/Ecriptor/devops-netology/tree/master/homeworks/08-ansible-04-module/test_module_play)


Идемпотентность:
```ansible
PLAY [all] *************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************
ok: [192.168.43.200]

TASK [my_own_namespace.my_own_collection.my_own_role : Run my module for Netology homework] ****************************************
changed: [192.168.43.200]

TASK [my_own_namespace.my_own_collection.my_own_role : debug] **********************************************************************
ok: [192.168.43.200] => {
    "msg": "Hello, world!"
}

PLAY RECAP *************************************************************************************************************************
192.168.43.200             : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
```ansible
PLAY [all] *************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************
ok: [192.168.43.200]

TASK [my_own_namespace.my_own_collection.my_own_role : Run my module for Netology homework] ****************************************
ok: [192.168.43.200]

TASK [my_own_namespace.my_own_collection.my_own_role : debug] **********************************************************************
ok: [192.168.43.200] => {
    "msg": "Hello, world!"
}

PLAY RECAP *************************************************************************************************************************
192.168.43.200             : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

