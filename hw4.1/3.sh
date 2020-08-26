ip=('192.168.1.1' '173.194.222.113' '87.250.250.242')
#set -x
var1=5
while [ $var1 -gt 0 ]
do
	for i in ${ip[@]}
	do
		echo $i >> log
		curl -s -w '%{http_code}\n' $i:80 -o /dev/null >> log
	done
	var1=$[ $var1 - 1 ]
done
