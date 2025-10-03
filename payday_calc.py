import time
import requests
import datetime

# Just for fun rate calculator, change base currency to any currency or whatever

def get_exchange_rate():
    base = input("Enter base currency (e.g., USD, CAD, EUR): ").upper()
    target = input("Enter target currency (e.g., JPN, KRW, PHP): ").upper()
    today = datetime.date.today()
    url = f"https://api.frankfurter.dev/v1/latest?base={base}&symbols={target}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"][target]
        #print(f"{data}\n")
        return rate, base, target
    except Exception as e:
        print("\nError fetching exchange rate:", e)
        return None, base, target



def compute_income(convert):
    try:
        rate = float(input("How much is your hourly rate?: "))
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

convert, base, target = get_exchange_rate()
if convert is not None:
    print(f"\nExchange rate: 1 {base} = {convert:.2f} {target}\n")
    compute_income(convert)
else:
    print("Could not fetch exchange rate. Try again later.")




