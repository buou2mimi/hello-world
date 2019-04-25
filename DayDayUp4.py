#DayDayUpQ4.py
dayup=1.0
dayfactor=0.01
dayup2=pow(1.01,365)
while dayup < dayup2:
    dayfactor+=0.001
    dayup=1.0
    for i in range(365):
        if i % 7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+dayfactor)
print("{:.3f}".format(dayfactor))
   



