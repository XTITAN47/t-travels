import csv
trains=open(r"mainp\tanmay\data\csvfiles\trains.csv","a+",newline="")
tt=csv.writer(trains)
my_trains=[["AGRA","JAIPUR","DURANTO EXPRESS","7:55 AM","3:12 PM",'256','302','450'],["AGRA","JAIPUR","SHATABDI EXPRESS","8:30 AM","11:13 AM",'-','-','615']]
tt.writerows(my_trains)
trains.close()