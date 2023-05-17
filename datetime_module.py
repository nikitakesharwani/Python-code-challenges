from datetime import datetime

now = datetime.now().time()
print("now = " , now)

start_date = datetime(2010 , 1 ,1)
end_date = datetime(2012 , 1 , 1)
difference = end_date - start_date
print(difference)

print(difference.days , difference.seconds)

difference_in_years = (difference.days + difference.seconds/86400)/365.2425

print(difference_in_years)

