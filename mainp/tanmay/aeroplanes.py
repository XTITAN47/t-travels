import csv
airt=open("airt.csv","a+",newline="")
airwriter=csv.writer(airt)
flights=[['AGRA','JAIPUR','8:10 AM','11:13 AM','1500','3000','4800'],['DELHI','MUMBAI','9:10 AM','02:13 PM','1500','3000','4800'],
         ['MUMBAI','JAIPUR','3:10 AM','4:13 AM','1500','3000','4800'],['JAIPUR','KOLKATA','8:10 AM','11:13 AM','1500','3000','4800'],
         ['KOLKATA','AGRA','8:10 AM','11:13 AM','1500','3000','4800']]
airwriter.writerows(flights)
airt.close()