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
