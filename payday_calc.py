import time
import requests
from datetime import datetime
import datetime

# Just for fun rate calculator, change USD to any currency or whatever

def usd_php():
    base = "USD"
    today = datetime.date.today()
    url = f"https://api.frankfurter.dev/v1/latest?base={base}&symbols=PHP"

    response = requests.get(url)
    data = response.json()
    #print(f"{data}\n")
    php_rate = data["rates"]["PHP"]
    return php_rate

def compute_income(convert):
    try:
        rate = float(input("How much is your hourly rate?: "))
        #usd_to_php = float(input("Currently, how much is 1 USD to PHP?: "))
        tax = float(input("Enter your tax %?: "))
        month_hours = 160
        tax_decimal = tax / 100
        monthly_no_tax = rate * month_hours
        m_income = (monthly_no_tax - (monthly_no_tax * tax_decimal))
        converted_monthly_income = m_income * convert

        # Output
        print("Computing...")
        time.sleep(1)
        print(f"\n{'Salary Table':<26}")
        print("==========================|===============|")
        print(f"{'Monthly Income by $$':<26}| ${m_income:<13.2f}|")
        print(f"{'Converted to PHP Monthly':<26}| PHP {converted_monthly_income:<10.2f}|")

    except ValueError:
        print("\nYour input is invalid. Use numbers only!!\n")


print("   Salary Calculator")
print("=======================\n")

convert = usd_php()
compute_income(convert)



