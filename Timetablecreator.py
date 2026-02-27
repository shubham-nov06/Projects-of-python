# This Python code snippet is taking user input for subject names separated by commas and the total
# number of hours available for studying. It then calculates the number of hours per subject based on
# the total hours and the number of subjects entered. Finally, it prints out a study plan showing the
# distribution of hours for each subject.

subject = input("Enter the subject name spereatd with , ")
total_hours = float(input("Enter the number of hours you have "))
subject_list = subject.split(",")
hours_per_subject = total_hours / len(subject_list)
print("\n Your study plan is = \n ")
for subject in subject_list:
    print(subject.strip(), " ->  ", round(hours_per_suject), 2, "hours"s)



