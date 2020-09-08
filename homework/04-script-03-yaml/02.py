#!/usr/bin/env python3

import os
import sys
import socket
import json
import yaml

# указывем наши URL сервиса
hostnames = ["drive.google.com", "mail.google.com", "google.com"]
# из созданного файла вычитываем связку URL - IP в словарь, если файла нет генерим словарь.
# Проверяем, что введено имя файла
if len(sys.argv) < 2:
    print("Введите имя файла host_ip.json или host_ip.yaml")
    exit(0)
# Проверяем, что это файл JSON
elif os.path.exists(sys.argv[1]) is True and sys.argv[1] == "host_ip.json":
    with  open(sys.argv[1], "r") as file:
        host_ip_dict = json.load(file)
# Проверяем что файл YAML
elif os.path.exists(sys.argv[1]) is True and sys.argv[1] == "host_ip.yaml":
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
        if sys.argv[1] == "host_ip.json":
            json.dump(new_dict, file)
        elif sys.argv[1] == "host_ip.yaml":
            yaml.dump(new_dict, file)
