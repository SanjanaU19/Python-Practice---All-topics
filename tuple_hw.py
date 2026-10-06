
# WAP to print names of students who are absent today

total_student = ["Raj","Amit","Jay","Payal","Priya","Rahul","Pavan","Kiran","Prachi"]

present_attendence = ("Raj","Jay","Payal","Priya","Pavan","Kiran")

count_present = 0
count_absent = 0
total = 0

for name in total_student:
    if name not in present_attendence:
        print(name)
        count_present += 1
    total += 1

count_absent = total - count_present

print(f"Total student present in class :",total)
print(f"Total present count :" ,count_present)
print(f"Total absent count :" ,count_absent)