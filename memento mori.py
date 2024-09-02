# Start of the program
print(r"""
     _____
    /     \
   | () () |
    \  ^  /
     |||||
     |||||
""")
print("Memento Mori")

# Calculator

age = input("How old are you?: ")

age_as_int = int(age)

years_remaining =   90 - age_as_int
days_remaining = years_remaining * 365 
months_remining = years_remaining * 52
weeks_remaining = years_remaining * 12

message = f'You have {days_remaining} days, {months_remining} months, and {weeks_remaining} weeks left.'
print(message) 

