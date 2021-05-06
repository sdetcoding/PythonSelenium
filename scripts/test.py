import requests
import json


class A:

    def run(self):
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Kolkata&appid=7e7c713211fd97fdac5e1330070499e9&units=metric')
        rs = json.dumps(response.json())
        js = json.loads(rs)
        print(js)
        x=js['main']
        for key, value in x.items():
            if key == "temp":
                str=value
                print(str)




ob = A()
ob.run()
