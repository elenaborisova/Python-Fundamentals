companies = {}

command = input()
while not command == "End":
    company_data = command.split(" -> ")
    company_name = company_data[0]
    employee_id = company_data[1]

    if company_name not in companies:
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name] += [employee_id]

    command = input()

companies = dict(sorted(companies.items()))

for company, employees in companies.items():
    print(f"{company}")

    for employee in employees:
        print(f"-- {employee}")
