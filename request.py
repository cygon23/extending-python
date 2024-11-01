import requests

x = requests.get('domain.com')

if x.status_code == 200:
    print("success")
elif x.status_code == 404:
    print("not found")

print(x.elapsed)
print(x.cookies)
print(x.text)

#for request in paraeters
x = requests.get('domain.com', params={'id':1})
print(x.url)