# Reflection 1:
# Python can automate reading, cleaning, and organizing large amounts of data.
# Excel is easier for manually viewing data and creating charts.

# Reflection 2:
# A business could use an append-mode log to record daily sales.
# Append mode keeps previous records instead of replacing them.


import csv
from datetime import datetime


# Exercise 1: Setup
file_path = "data/sales.csv"


# Exercise 2: Read and print raw rows
with open(file_path, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3: Skip the header
with open(file_path, "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# Exercise 4: Compute totals
total_revenue = 0

with open(file_path, "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(
            f"{product}: {quantity} units "
            f"× ${price:.2f} = ${total:.2f}"
        )

print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 5: Filter and write
written_count = 0
original_count = 0

with open(file_path, "r") as file:
    reader = csv.reader(file)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count += 1

print("Rows written:", written_count)
print("Original rows:", original_count)


# Exercise 6: DictReader
dict_total = 0

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        dict_total += price * quantity

print(f"DictReader total: ${dict_total:.2f}")

# csv.reader uses column positions and is useful for simple CSV files.
# DictReader uses column names and makes the code easier to understand.


# Exercise 7: Sales summary by product
summary = {}

with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])

        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(product, f"${summary[product]:.2f}")


# Exercise 8: Append mode log
with open("data/run_log.txt", "a") as log:
    timestamp = datetime.now()
    log.write(
        f"{timestamp} | Total revenue: ${total_revenue:.2f}\n"
    )

print("Run log updated.")