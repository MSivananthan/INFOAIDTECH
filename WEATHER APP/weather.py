print('To exit press Ctrl + C')
while True:
        import requests as r
        import json as j

        try:

                prefix_url='http://api.openweathermap.org/data/2.5/weather?appid='
                key='df2af62b7ee6bab8ec2992a2dd2fc3c9'
                suffix_url='&q='
                country=str(input("enter any country"))

                weather=prefix_url+key+suffix_url+country

        
                detialss=r.get(weather)
                detials=detialss.json()

                #print(detials)

                print('Temperature:',int(detials['main']['temp']) - 273.15)
                print('Humidity:',detials['main']['humidity'])
                print('Weather description:', detials['weather'][0]['description'])

        except KeyError:
                print('country not found!')

        except KeyboardInterrupt:
                print('Loop breaks')
                break;
