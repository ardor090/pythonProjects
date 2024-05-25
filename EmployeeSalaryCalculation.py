# Check if there's error in the code
try:
    # Ask user for values
    employee_name = input('Employee: ')
    employee_number = input('Employee Number: ')
    week_ending = input('Week Ending: ')
    hours_worked = float(input('Number of hours worked: '))
    hourly_rate = float(input('Hourly Rate: '))
    overtime_rate = float(input('Overtime Rate: '))
    standard_rate = int(input('Standard Tax Rate: '))
    overtime_tax = int(input('Overtime Tax Rate: '))
    normal_hour = 37.5

    # Check if the number of hours worked is greater than threshold
    if hours_worked > 37.5:
        # time and a half is rate of overtime multiply by hourly rate
        time_and_a_half = overtime_rate * hourly_rate
        # Subtract hour worked from threshold to get overtime
        overtime = hours_worked - normal_hour
        # Multiply the hourly rate by threshold
        normal_hour_worked = normal_hour * hourly_rate
        # overtime multiply by time and a half
        overtime_hour = overtime * time_and_a_half
        # Calculate number of tax for normal hour
        normal_hour_tax =  normal_hour_worked * (standard_rate/100)
        # Calculate number of tax for overtime
        overtime_hour_tax = overtime_hour * (overtime_tax/100)
        # Calculate gross pay
        grosspay = normal_hour_worked + overtime_hour
        # Calculate tax
        tax = normal_hour_tax + overtime_hour_tax
        # Subtract tax from gross pay to get net pay
        netpay = grosspay - tax

    # Check if the number of hours worked is less than the threshold and greater than zero
    elif hours_worked <= 37.5 and hours_worked > 0.0:
        # Multiply the hourly rate by threshold
        normal_hour_worked = normal_hour * hourly_rate
        # Calculate number of tax for normal hour
        normal_hour_tax = normal_hour_worked * (standard_rate / 100)
        overtime = 0
        time_and_a_half = 0
        overtime_hour = 0
        overtime_hour_tax = 0
        # Calculate gross pay
        grosspay = normal_hour * hourly_rate
        # Calculate tax
        tax = grosspay * (standard_rate / 100)
        # Subtract tax from gross pay to get net pay
        netpay = grosspay - tax
    # when if and elif code aren't satisfied
    else:
        print("Please enter a valid hour.")
    # Formatting the payslip using tab
    print("\t\t\t\t\t\t\t\tPAYSLIP")
    print("Employee: ",employee_name)
    print("Employee Number: ",employee_number)
    print("\t\t\t\t\t\tEarnings\t\t\t\t\t\tDeductions")
    print("\t\t\t\t\t\tHours\tRate\t\tTotal")
    # Format the both normal and overtime hours
    print('Hours (Normal){:>14.2f}{:>8.2f}{:>14.2f}\tTax @ {}%{:>10.2f}'.format(normal_hour,hourly_rate,normal_hour_worked,standard_rate,normal_hour_tax))
    print('Hours (Overtime){:>12.2f}{:>8.2f}{:>14.2f}\tTax @ {}%{:>10.2f}'.format(overtime,time_and_a_half,overtime_hour,overtime_tax,overtime_hour_tax))
    print("\t\t\t\t\t\tTotal pay: {:>36.2f}".format(grosspay))
    print("\t\t\t\t\t\tTotal deductions: {:>29.2f}".format(tax))
    print("\t\t\t\t\t\tNet pay: {:>38.2f}".format(netpay))
# Runs when there is value error in the code
except ValueError:
    print("Please enter an integer value")