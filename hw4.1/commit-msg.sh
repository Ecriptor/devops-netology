#!/bin/bash 
#Скрипт /devops-netology/.git/hooks/commit-msg
#!/usr/bin/env bash
#while read line
#do
#       	# пропускаем строки комментариев	
#	if [ "${line:0:1}" == "#" ]
#	then
#		continue
#	fi
#done < "${1}"
#commit_regex='^\[04-script-01-bash\]'
commit_regex='^(\[[0-9]{2}\-[a-zA-Z]+\-[0-9]{2}\-[a-z]+\])([a-z\ \-]{1,30})'
error_msg="Сообщение коммита должно начинаться с [04-script-01-bash]"
#если в сообщении коммита нет строки, начинающейся с нужного шаблона
if ! grep -iqE "$commit_regex" "$1"; then
	echo "$error_msg" >&2
	exit 1
fi
exit 0
