import requests

url="https://restcountries.eu/rest/v2/all"
# this is a link of rest country API where you will see the bunch of JSON data (copy whole data and paste into this site https://jsoneditoronline.org/ to view it in Graphically).z=requests.get(url)
# here i loaded it into json format
z=requests.get(url)
# I used requests module to fetch data from above link.
data=z.json()
#in this step it json data defined
print("""******* This is a python program to fetch data from rest country api ******* """)
print(" ")
country = input("enter your country name to fetch its details:")
country=country.capitalize()
#  Here I use capitalize method to make first latter capital.
for i in data:
# I used for loop to iterate through every index of data  (you can check len data file by using len(data))
    if i["name"]==country:
        #Here I implemented a condition that if "country name" present in data then it goes further otherwise it breaks
        print("")
        print(''' **** congratulation your country is present in our database ****
            o>.press 0 for exit
            o>.press 1 for view domain of this nation
            o>.press 2 for view capital of this nation
            o>.press 3 for view region of this nation
            o>.press 4 for view subregion of this nation
            o>.press 5 for view total population of this nation
            o>.press 6 for view total area of this nation in km square
            o>.press 7 for view timezone of this nation
            o>.press 8 for view share border of this nation
            o>.press 9 for view currency of this nation
            o>.press 10 for view languages spoken in this nationie
            o>.press 11 for view regionalBlocs of this nation
            o>.press 12 for view nativeName of this nation            ''')
        while True:
            print(" ")
            choice=int(input("enter your choice :"))
            if choice==1:
                x=i['topLevelDomain']
                print("domain of {} is :{}".format(country,x))
            elif choice==2:
                x=i['capital']
                print("capital of {} is :{}".format(country,x))
            elif choice==3:
                x=i['region']
                print("region of {} is :{}".format(country,x))
            elif choice==4:
                x=i['subregion']
                print("subregion of {} is :{}".format(country,x))
            elif choice==5:
                x=i['population']
                print("population of {} is :{}".format(country,x))
            elif choice==6:
                x=i['area']
                print("The total area  of this  {} is :{} in km square".format(country,x))
            elif choice==7:
                x=i['timezones']
                print("timezone of {} is :{}".format(country,x))
            elif choice==8:
                x=i['borders']
                print("shared border of {} with these countries :{}".format(country,x))
            elif choice==9:
                x=i['currencies']
                print("currency of {} is :{}".format(country,x))
            elif choice==10:
                x=i['languages']
                print("languages spoken in {} is :{}".format(country,x))
            elif choice==11:
                x=i['regionalBlocs']
                print("regionalBlocs of  {} is :{}".format(country,x))
            elif choice==12:
                x=i['nativeName']
                print("nativeName {} is :{}".format(country,x))
            elif choice==0:
                exit()
            else:
                print("enter a valid input")

print("sorry this api did not have this country details")