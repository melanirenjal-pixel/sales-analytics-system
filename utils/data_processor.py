def calculate_total_sales(lines):
    total = 0
    for line in lines[1:]:  # skip header
        parts = line.strip().split(",")
        amount = int(parts[2])
        total += amount
    return total