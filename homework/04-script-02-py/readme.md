# 04-script-02-py
1. Ex1
* Будет ошибка из-за несовпадения типов
* Нужно переменную a задать в кавычках  **a = '2'** или при присвоении c = str(a) + str(b) 
* Нужно у переменной b убрать кавычки  **b = 2** или при присвоении c = int(a) + int(b)
2. [Ex2]()
```python
#!/usr/bin/env python3
  
import os

git_repo_dir = '/home/ecriptor/devops-netology/'
bash_command = ["cd "+git_repo_dir, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = git_repo_dir + result.replace('\tизменено:      ', '')
        print(prepare_result)
```
3. [Ex3]()

```python
#!/usr/bin/env python3
  
import os

git_repo_dir = '/home/ecriptor/devops-netology/'
bash_command = ["cd "+git_repo_dir, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = git_repo_dir + result.replace('\tизменено:      ', '')
        print(prepare_result)
        break
```
4. [Ex4]()
 
