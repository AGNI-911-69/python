name = "john"
age = 20
language = "python"
hours = 3

# john is 20 years old. he studies python 3 hours a day.
print(name,"is",age,"years old. he studies",language,hours,"hours a day.")

#using fstring
print(f"{name} is {age} years old. he studies {language} {hours} hours a day.")

sub1=86
sub2=79
sub3=88

print(f"{name} scored {sub1 + sub2 + sub3} marks in total.")
percent = (sub1 + sub2 + sub3) / 3
print(f"{name} got {percent}%.")