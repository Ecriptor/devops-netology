#!/usr/bin/env python3

import os

git_repo_dir = '/home/ecriptor/devops-netology/'
bash_command = ["cd "+git_repo_dir, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
#is_change = False
prepare_result = ""
for result in result_os.split('\n'):
    if result.find('изменено') != -1:
        prepare_result = prepare_result + git_repo_dir + result.replace('\tизменено:      ', '') + '\n'
print(prepare_result)
