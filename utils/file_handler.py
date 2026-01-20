def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues
    Returns list of raw lines (strings)
    """

    encodings = ['utf-8', 'latin-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = file.readlines()

            # remove header and empty lines
            cleaned_lines = []
            for line in lines[1:]:
                line = line.strip()
                if line:
                    cleaned_lines.append(line)

            print(f"File read successfully using {encoding}")
            return cleaned_lines

        except FileNotFoundError:
            print("ERROR: File not found.")
            return []

        except UnicodeDecodeError:
            continue

    print("ERROR: Could not read file with available encodings.")
    return []


