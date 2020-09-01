#!/bin/bash 
#Скрипт расположен в директории /<репозиторий>/.git/hooks/commit-msg
commit_regex='^(\[[0-9]{2}\-[a-zA-Z]+\-[0-9]{2}\-[a-z]+\])([a-zA-Zа-яА-Я\ \-\,\.\:\;]{1,30})'
error_msg='Сообщение коммита должно иметь следующий вид "[01-script-01-bash] messages" (messages не больше 30 символов)'
if ! grep -iqE "$commit_regex" "$1"; then
	echo "$error_msg" >&2
	exit 1
fi
exit 0
