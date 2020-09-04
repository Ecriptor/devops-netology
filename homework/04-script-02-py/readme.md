# Ответы на вопросы по домашнему заданию 04-script-02-py
1. Ex1
* Будет ошибка из-за несовпадения типов
* Нужно переменную a задать в кавычках  **a = '2'** или при присвоении c = str(a) + str(b) 
* Нужно у переменной b убрать кавычки  **b = 2** или при присвоении c = int(a) + int(b)
2. [Ex2](2.py)
```python
#!/usr/bin/env python3
  
import os

git_repo_dir = '/home/ecriptor/devops-netology/'
bash_command = ["cd "+git_repo_dir, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
prepare_result = ""
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = prepare_result + git_repo_dir + result.replace('\tизменено:      ', '') + '\n'
print(prepare_result)
```
3. [Ex3](3.py)

```python
#!/usr/bin/env python3
  
import os
import sys

# Проверяем, что передается дирктория и такая директория существует
if len(sys.argv) < 2 or os.path.exists(sys.argv[1]) is False:
        print("Введите локальный git репозиторий\nCтрока должна иметь вид /dir/../git_repo")
        exit(0)

git_repo_dir = sys.argv[1]
bash_command = ["cd " + git_repo_dir, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
prepare_result = ""
# Если вывод не пустой и нет строки "not a git repository", ищем измененные файлы
if result_os != "" and result_os.find("not a git repository") == -1:
    for result in result_os.split('\n'):
        if result.find('изменено') != -1:
            prepare_result = prepare_result + git_repo_dir + result.replace('\tизменено:      ', '') + '\n'
    print(prepare_result)
# Если строка "not a git repository" присутствовала, то выводим сообщение.
else:
    print(f"{git_repo_dir} не является git репозиторием")
```
4. [Ex4](4.py)
```python
#!/usr/bin/env python3
  
import os

# указывем наши URL сервиса
hostnames = ["drive.google.com", "mail.google.com", "google.com"]
# из созданного файла вычитываем связку URL - IP в словарь
if os.path.exists("host_ip.txt"):
    host_ip_dict={}

    with  open("host_ip.txt", "r") as file:
        for line in file:
            host = line.split(" - ")[0]
            ip = line.split(" - ")[1]
            host_ip_dict[host] = ip.replace('\n', '')
        print(host_ip_dict)
```

 
