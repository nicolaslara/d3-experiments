import json
import requests
import datetime

from datetime import timedelta

#ttps://api.forecast.io/forecast/3f166df6cbac36dc7b6ea176021bcb69/59.3294,18.0686,2013-02-12T14:00:00+0200

base = datetime.datetime(2012,1,1)
end = datetime.datetime(2013,1,1)

dates = []

while base < end:
    dates.append(base)
    base = base + timedelta(days=1)

# Stockholm: 59.3294,18.0686
# Taussat: 44.7208,-1.0722
coords = '44.7208,-1.0722'

days = [d.isoformat() + '+0200' for d in dates]
urls = ['https://api.forecast.io/forecast/3f166df6cbac36dc7b6ea176021bcb69/'+coords+',' + day
            for day in days]

data = []
for url in urls:
    response = requests.get(url)
    for day in [i['temperature'] for i in json.loads(response.content)['hourly']['data']]:
        print day
