# -*- coding: UTF-8 -*-
from snakebite.client import Client

client = Client('master', 9000)
for ln in client.text(['/wordcount/input/yarn.txt']):
    print ln