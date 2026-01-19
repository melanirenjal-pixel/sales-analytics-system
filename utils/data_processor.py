def parse_sales_data(lines):
    records = []

    for line in lines:
        date, product, amount = line.strip().split(",")
        records.append({
            "date": date,
            "product": product,
            "amount": int(amount)
        })

    return records


def total_sales(records):
    return sum(item["amount"] for item in records)
