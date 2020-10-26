happiness_numbers = list(map(int, input().split())) 
factor = int(input())

increased_happiness = list(map(lambda n: n * factor, happiness_numbers))
average_new_factor = sum(increased_happiness) / len(increased_happiness)
happy_employees = list(filter(lambda n: n >= average_new_factor, increased_happiness))

if len(happy_employees) >= 1/2 * len(increased_happiness):
    print(f"Score: {len(happy_employees)}/{len(increased_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(increased_happiness)}. Employees are not happy!")
