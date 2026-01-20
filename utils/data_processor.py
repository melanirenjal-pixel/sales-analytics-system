def process_sales_data(raw_lines):
    records = []

    for line in raw_lines:
        parts = line.split("|")

        # skip invalid rows
        if len(parts) != 8:
            continue

        transaction_id, date, product_id, product_name, quantity, unit_price, customer_id, region = parts

        # validation
        if not transaction_id.startswith("T"):
            continue

        try:
            quantity = int(quantity)
            unit_price = float(unit_price.replace(",", ""))
        except:
            continue

        if quantity <= 0 or unit_price <= 0:
            continue

        records.append({
            "date": date,
            "product": product_name,
            "amount": quantity * unit_price
        })

    return records


   