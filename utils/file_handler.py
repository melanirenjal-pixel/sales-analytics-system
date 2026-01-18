def save_result(total_sales):
    output_path = "output/result.txt"
    with open(output_path, "w") as file:
        file.write(f"Total Sales Amount: {total_sales}")

