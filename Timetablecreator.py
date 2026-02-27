subject = input("Enter the subject name spereatd with , ")
total_hours = float(input("Enter the number of hours you have "))
subject_list = subject.split(",")
hours_per_subject = total_hours / len(subject_list)
print("\n Your study plan is = \n ")
for subject in subject_list:
    print(subject.strip(), " ->  ", round(hours_per_suject), 2, "hours"s)
