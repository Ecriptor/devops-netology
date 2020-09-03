#!/usr/bin/env python3

import os

# указывем наши URL сервиса
hostnames = ["drive.google.com", "mail.google.com", "google.com"]
# из созданного файла вычитываем связку URL - IP в словарь
if os.path.exists("host_ip.txt"):
    host_ip_dict={}

    with  open("host_ip.txt", "r") as file:
        for line in file:
            host = line.split(" - ")[0]
            ip = line.split(" - ")[1]
            host_ip_dict[host] = ip.replace('\n', '')
        print(host_ip_dict)
