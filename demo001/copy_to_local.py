from snakebite.client import Client

client = Client('master', 9000)
for f in client.copyToLocal(['/wordcount/input/yarn.txt'], './tmp/yarn.txt'):
    print f