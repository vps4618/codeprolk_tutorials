#date
import datetime
birth_year=datetime.date(2005,5,10)
print(birth_year)

#today
today=datetime.date.today()
print(today)

#STRING FORMAT STYLE

# %a  -	weekday(short) -	Wed
# %A -	weekday(full) -	Wednesday
# %b -	month_name(short) -	Dec
# %B -	month_name( fu11) -	December
# %y -	Year(short) -20
# %Y -	Year(full) -2020
# %d -	day -31
# %H -	Hour(00-23) -19
# %l -	Hour(00-12) -08
# %M -	Minute -43
# %S -	Second -27
# %f -	Microsecond -45377
# %p -	AM/PM -AM

print(birth_year.strftime('%A ,%B %d ,%Y'))  

#age

age=today-birth_year
print(age)

print(today.weekday())#in weekday,monday=0,tuesday=1,w=2,th=3,f=4,s=5,su=6
print(today.isoweekday())#in isoweekday,monday=1,tuesday=2


#time

t=datetime.time(12,45,12,565656)
print(t)

#access hour
print(t.hour)

#access minutes
print(t.minute)

#how to show date and time at once
a=datetime.datetime.today()
print(a)

#how to access only date
print(a.date())

#how to access only time
print(a.time())

#adding and subtracting days
time_delta=datetime.timedelta(days=20)
print(a-time_delta)
print(a+time_delta)

#adding and subtracting hours
time_delta=datetime.timedelta(hours=20)
print(a-time_delta)
print(a+time_delta)