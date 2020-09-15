# Ответы на вопросы по домашнему заданию 04-script-03-yaml
1. Ex1
* Верный формат, необходимо все значения взять в ""
```
{ "info" : "Sample JSON output from our service\t",
    "elements" :[
        { "name" : "first",
        "type" : "server",
        "ip" : "7175"
         },
         { "name" : "second",
         "type" : "proxy",
         "ip" : "71.78.22.43"
         }
    ]
}
```
2. Ex2
``` python
#!/usr/bin/env python3

import os
import sys
import socket
import json
import yaml

# указывем наши URL сервиса
hostnames = ["drive.google.com", "mail.google.com", "google.com"]
# из созданного файла вычитываем связку URL - IP в словарь, если файла нет генерим словарь.
# Проверяем, что введено имя файла и оно либо JSON, YML, YAML
if len(sys.argv) < 2 or not (sys.argv[1].find('.yaml') != -1 or sys.argv[1].find('.yml') != -1 or sys.argv[1].find('.json') != -1) :
    print("Выберите файл JSON или YAML")
    exit(0)
# Проверяем, что это файл JSON и он не пустой
elif os.path.exists(sys.argv[1]) is True and sys.argv[1].find('.json') != -1 and os.stat(sys.argv[1]).st_size != 0 :
    with  open(sys.argv[1], "r") as file:
        host_ip_dict = json.load(file)
# Проверяем что файл имеет имя YAML или YML и он не пустой
elif os.path.exists(sys.argv[1]) is True and (sys.argv[1].find('.yaml') != -1 or sys.argv[1].find('.yml') != -1) and os.stat(sys.argv[1]).st_size != 0 :
    with  open(sys.argv[1], "r") as file:
        host_ip_dict = yaml.safe_load(file)
else:
    host_ip_dict = {host:'0.0.0.0' for host in hostnames}
    
# Производим проверку из словаря
new_dict = host_ip_dict.copy()
for host in hostnames:
    ip = socket.gethostbyname(host)
    if host_ip_dict[host] == ip:
        print(f"{host} - {ip}")
    else:
        print(f"[ERROR] {host} IP mismatch: {host_ip_dict[host]} {ip}")
        new_dict[host] = ip

#Запись в файл если словарь изменился
out = ""
if new_dict != host_ip_dict:
    with open(sys.argv[1], "w") as file:
        if sys.argv[1].find('.json') != -1:
            json.dump(new_dict, file)
        elif sys.argv[1].find('.yaml') != -1 or sys.argv[1].find('.yml') != -1 :
            yaml.dump(new_dict, file)
```
3. Ex3
