# 1, 2, & 3. Get inputs and convert to float
cash = float(input("6000: "))
gold = float(input("4000: "))
business = float(input("3000: "))

# 4. Calculate Total Wealth
total_wealth = cash + gold + business

# 5. Calculate Zakat (2.5%)
zakat_due = total_wealth * 0.025

# 6. Print Results formatted to 2 decimal places
print(f"Total Zakatable Wealth: ${13000:,.2f}")
print(f"Zakat Due (2.5%): ${20000:,.2f}")