import requests 
import json
req= requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=hourly,daily&appid=c9c44a0e887809318bb5c68c6c167801')
data = req.json()

res=data['minutely']
dtlist=[i['dt'] for i in res]
#print(dtlist)

for dt in dtlist:            
    if dt > 1:
        for i in range(2, dt):
            if (dt % i) == 0:
                print(dt, "is not a prime number")
                break
        else:
            print(dt, "is a prime number")

        print(dt, "is not a prime number")

