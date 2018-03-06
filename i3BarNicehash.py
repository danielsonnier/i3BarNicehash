import urllib, json
url = "https://api.nicehash.com/api?method=stats.provider&addr=14SfhdUgw1gAfimCyATWcU5BxqxoqH9mWP&algo=3"
response = urllib.urlopen(url)
data = json.loads(response.read())


sum = 0

for x in data['result']['stats']:
    sum += float(x['accepted_speed'])

print sum * 1000
