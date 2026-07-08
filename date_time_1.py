from datetime import datetime as dt 

#create datetime type object 
dt = dt.now()

print("Date ", dt.day)
print("Month ", dt.month)
print("Year ", dt.year)
print("weekday ", dt.weekday())
week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
today = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year)+" "+ week[dt.weekday()]
print("today=",today)

print("hours ",dt.hour)
print("minutes ",dt.minute)
print("seconds ",dt.second)
time= str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second)
print("time=",time)