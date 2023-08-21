def pkr_to_usd(pkr_amount):
    exchange_rate = 0.0029  # 1 USD = 300 PKR (sample exchange rate)
    usd_amount = pkr_amount * exchange_rate
    return usd_amount

def usd_to_pkr(usd_amount):
    exchange_rate = 290  # 1 USD = 160 PKR (sample exchange rate)
    pkr_amount = usd_amount * exchange_rate
    return pkr_amount

print("Currency Converter")
print("1. PKR to USD")
print("2. USD to PKR")

choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    pkr_amount = float(input("Enter amount in PKR: "))
    usd_amount = pkr_to_usd(pkr_amount)
    print(f"{pkr_amount:.2f} PKR is equal to {usd_amount:.2f} USD")
elif choice == 2:
    usd_amount = float(input("Enter amount in USD: "))
    pkr_amount = usd_to_pkr(usd_amount)
    print(f"{usd_amount:.2f} USD is equal to {pkr_amount:.2f} PKR")
else:
    print("Invalid choice")

