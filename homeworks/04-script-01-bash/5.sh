#ip=('192.168.0.1' '173.194.222.113' '87.250.250.242')
ip=('192.168.0.1')
set -x
for i in ${ip[@]}
do
	echo $i >> log
	var1=5
	while [ $var1 -gt 0 ]
	do
	var1=$[ $var1 - 1 ]
	curl -s -w '%{http_code}\n' $i:80 -o /dev/null >> log
	if [[ $? == 0 ]]
	then
		continue
	else
		echo $i > error
		break 2
	fi
	done
done
