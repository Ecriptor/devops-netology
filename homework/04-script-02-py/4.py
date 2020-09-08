#!/usr/bin/env python3

import os
import socket

# указывем наши URL сервиса
hostnames = ["drive.google.com", "mail.google.com", "google.com"]
# из созданного файла вычитываем связку URL - IP в словарь, если файла нет создаем словарь с известными IP для URL
if os.path.exists("host_ip.txt"):
    host_ip_dict = {}

    with  open("host_ip.txt", "r") as file:
        for line in file:
            host = line.split(" - ")[0]
            ip = line.split(" - ")[1]
            host_ip_dict[host] = ip.replace('\n', '')
else:
    host_ip_dict = {'drive.google.com': '64.233.162.194', 'mail.google.com': '173.194.73.19', 'google.com': '64.233.161.100'}
    
# Производим проверку из словаря
new_dict = {}
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
    with open("host_ip.txt", "w") as file:
        for key, value in new_dict.items():
            out = out+key+' - '+value+"\n"
        file.write(out)

