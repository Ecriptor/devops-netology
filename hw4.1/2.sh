while ((1==1))
do
	curl https://localhost:4747
	if (($? != 0))
	then
		date >> curl.log
	else
		break
	fi
done
