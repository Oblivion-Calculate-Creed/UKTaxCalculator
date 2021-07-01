def main():
    name = input("Enter full name: ")
    income = eval(input("Please enter income: "))
    tax = 0.0
    aftertax = 0.0
    afterni = 0.0
    grosspay = income
    nationalinsurance = 0.0
    taxablewage = income-12570

    if income >= 150000:
        tax = ((income - 150000) * .45) + \
            ((150000-50271) * .4) + ((50270-12571) * .2)
        aftertax = income - tax
    elif income >= 50270:
        tax = ((income - 50270) * .4) + (12570 * .2)
        aftertax = income - tax
    elif income >= 12570:
        tax = (income - 12570) * .2
        aftertax = income - tax
    elif income >= 0:
        aftertax = income
    else:
        print("Please enter a valid income of more than £0!")

    if income > (50336):
        nationalinsurance = ((income - 50336) * .02) + \
            ((50336-9568) * .12)
        afterni = income - nationalinsurance
    elif income >= (9568):
        nationalinsurance = ((income - 9568) * .12)
        afterni = income - nationalinsurance
    elif income <= 9568:
        afterni = income
    else:
        print("Please enter a valid income of more than £0!")

    afterdeductions = grosspay-tax-nationalinsurance
    monthlyincome = afterdeductions/12
    floatmonthlyincome = "{:.2f}".format(monthlyincome)

    print('----------')
    print(name)
    print('----------')
    print("Gross Pay:", grosspay)
    print("Taxable Pay £", taxablewage)
    print('----------')
    print("Amount you will pay in tax: £", tax)
    print("Amount you will pay in NI: £", nationalinsurance)
    print('----------')
    print("Net Pay (after deductions): £", afterdeductions)
    print("Monthly Salary: £", floatmonthlyincome)


main()
