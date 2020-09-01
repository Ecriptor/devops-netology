ip=('173.194.222.113' '87.250.250.242' '192.168.0.1')
#set -x
while :
do
	for i in "${ip[@]}"
	do
		echo $i >> log
		curl -s -w '%{http_code}\n' $i:80 -o /dev/null >> log
		if [[ $? == 0 ]]
		then
			continue
		fi
			echo $i > error
			break 2
	done
done
