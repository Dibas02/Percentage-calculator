math = int(input("Enter the number of achieved marks in Math: "))
english = int(input("Enter the number of achieved marks in English: "))
science = int(input("Enter the number of achieved marks in Science: "))
social_studies = int(input("Enter the number of achieved marks in Social Studies: "))
arts = int(input("Enter the number of achieved marks in Arts: "))


sum = math+english+science+social_studies+arts

percentage = sum/500*100
print("The percentage of achieved marks is: ", percentage)