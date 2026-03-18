import re

with open("raw.txt", "r") as f:
    text = f.read()

prices = re.findall(r"\d+\.\d{2}", text)
total = sum(map(float, prices))

date = re.search(r"\d{2}/\d{2}/\d{4}", text)
time = re.search(r"\d{2}:\d{2}", text)
payment = re.search(r"(Cash|Card)", text)

print("Prices:", prices)
print("Total:", total)
print("Date:", date.group() if date else None)
print("Time:", time.group() if time else None)
print("Payment:", payment.group() if payment else None)