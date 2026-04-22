# Practice 5 – Python Regular Expressions (RegEx)

## 📌 Description

This project demonstrates the use of **Python Regular Expressions (re module)** to parse and extract information from raw text data (receipt).

The program reads a receipt from a file and extracts useful information such as prices, date, time, and payment method.

---

## 📂 Project Structure

```
Practice5/
│── receipt_parser.py   # Main script for parsing receipt
│── raw.txt             # Raw receipt data
│── README.md           # Project documentation
```

---

## ⚙️ Features

* Extract all prices from the receipt
* Calculate total amount
* Extract date and time
* Detect payment method
* Demonstrate usage of:

  * `re.search()`
  * `re.findall()`
  * `re.split()`
  * `re.sub()`

---

## 🧾 Example Input (`raw.txt`)

```
Walmart Store
Date: 12/03/2025
Time: 14:35

Milk        2.50
Bread       1.20
Eggs        3.00

Total: 6.70
Payment: Card
```

---

## ▶️ How to Run

1. Make sure Python is installed
2. Run the script:

```
python receipt_parser.py
```

---

## 🧠 Technologies Used

* Python 3
* Regular Expressions (`re` module)

---

## 🎯 Learning Outcomes

* Understanding RegEx syntax and patterns
* Extracting structured data from text
* Working with files in Python
* Applying pattern matching in real tasks

---

## 🚀 Author

Nurkanat
