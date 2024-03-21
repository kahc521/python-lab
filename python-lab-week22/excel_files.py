import csv

with open("week23.csv", 'w') as f:  # 'w' , 'r', 'a'
   pen = csv.writer(f) 
   header = ["Name", "Cell Phone" , "city"]
   pen.writerow(header)
   entry1 = ["serge", "555 555 5555", "houston"]
   pen.writerow(entry1)
f.close

