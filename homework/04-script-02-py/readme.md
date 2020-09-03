# 04-script-02-py
1. Задание 1
* Будет ошибка из-за несовпадения типов
* Нужно переменную a задать в кавычках  **a = '2'** или при присвоении c = str(a) + str(b) 
* Нужно у переменной b убрать кавычки  **b = 2** или при присвоении c = int(a) + int(b)
2. Задание 2
```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```
3. Задание 3

4. Задание 4
 
