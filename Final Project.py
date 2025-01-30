import os
import csv
import random

# Clears screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Loads file
def load_file():
    data = []
    folder_path = "/Users/theyarecoming/Documents/CSV Files"
    files = os.listdir(folder_path)
    if data == None:
        with open("error_log.csv", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(f"Error: {Exception}")
        print("Error has been recorded. Check file 'error_log.csv'.")
    
    for x, file in enumerate(files, start = 1):
        print(f"{x}. {file}")

    while True:
        try:
            choice = int(input("\nEnter choice: "))
            if 1 <= choice <= len(files):
                break
            else:
                print("Invalid choice. Enter within range.")
        except ValueError:
            print("Invalid input. Enter a number.")

    file_name = os.path.join(folder_path, files[choice-1])
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        return data

# Checks for header row
def set_header_row(data):
    if not data:
        print("No data to display.")
        return
    print()
    column_widths = [max(len(str(value)) for value in column) for column in zip(*data)] #stackoverflow
    for x, row in enumerate(data[:6]):
        row_format = " | ".join(f"{str(value):^{column_widths[y]}}" for y, value in enumerate(row))
        print(f"| {row_format} |")
        if x == 0:
            print("-" * (sum(column_widths) + 3 * len(column_widths) + 1))
            
    while True:
        has_header = input("\nDoes dataset have header (yes/no)? ").lower()
        if not has_header.isalpha():
            print("Invalid input. Enter a choice.")
        else:
            if has_header == "yes":
                print("Header row recorded.")
                break
            elif has_header == "no":
                print("No header row recorded.")
                break
            elif has_header != "yes" or has_header != "no":
                print("Invalid input. Enter yes or no.")
    return has_header

# Displays table of data
def display_data(data):
    if not data:
        print("No data to display.")
        return
    print()
    column_widths = [max(len(str(value)) for value in column) for column in zip(*data)] #stackoverflow
    for x, row in enumerate(data[:50]):
        row_format = " | ".join(f"{str(value):^{column_widths[y]}}" for y, value in enumerate(row))
        print(f"| {row_format} |")
        if x == 0:
            print("-" * (sum(column_widths) + 3 * len(column_widths) + 1))

    while True:
        validate = input("\nConfirm content and format (yes/no)? ").lower()
        if not validate.isalpha():
            print("Invalid input. Enter a choice.")
        else:
            if validate == "yes":
                print("Content and format validated.")
                break
            elif validate == "no":
                print("Content and format invalidated.")
                break
            elif validate != "yes" or validate != "no":
                print("Invalid input. Enter yes or no.")

# Count for occurrences
def count_for_ranges(data, has_header):
    if not data:
        print("No data to count.")
        return
    if has_header == "yes":
        value_counts = {}

        for row in data[1:]:
            for value in row:
                if value in value_counts:
                    value_counts[value] += 1
                else:
                    value_counts[value] = 1
        print("Data counted.")
        return value_counts
    
    elif has_header == "no":
        value_counts = {}

        for row in data:
            for value in row:
                if value in value_counts:
                    value_counts[value] += 1
                else:
                    value_counts[value] = 1
        print("Data counted.")
        return value_counts

# Displays occurrences
def display_ranges(value_counts):
    if not value_counts:
        print("No data to display.")
        return
    print("Occurences:")
    for x, (value, count) in enumerate(value_counts.items()):
        if x >= 50:
            break
        print(f"{value}: {count} times")

# Generates synthetic data
def roll_data(data,has_header):
    if not data:
        print("No data to use.")
        return
    while True:
        try:
            rows = int(input("\nEnter number of records to generate: "))
            if rows <= 0:
                print("Enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Enter a number.")
    clear_screen()

    if has_header == "yes":
        header = data[0]
        new_data = [header]

        for _ in range(rows):
            new_row = []
            for column in zip(*data[1:]):
                if all(item.replace('.', '', 1).isdigit() for item in column):
                    column = list(map(float, column))
                    new_value = round(random.uniform(min(column), max(column)), 2)
                else:
                    new_value = random.choice(column)
                new_row.append(new_value)
            new_data.append(new_row)
        
        column_widths = [max(len(str(value)) for value in column) for column in zip(*data)] #stackoverflow
        for x, row in enumerate(new_data[:50]):
            row_format = " | ".join(f"{str(value):^{column_widths[y]}}" for y, value in enumerate(row))
            print(f"| {row_format} |")
            if x == 0:
                print("-" * (sum(column_widths) + 3 * len(column_widths) + 1))
        
        while True:
            validate = input("\nContinue(yes/no)? ").lower()
            if not validate.isalpha():
                print("Invalid input. Enter a choice.")
            else:
                if validate == "yes":
                    column_widths = [max(len(str(value)) for value in column) for column in zip(*data)] #stackoverflow
                    for x, row in enumerate(new_data[51:]):
                        row_format = " | ".join(f"{str(value):^{column_widths[y]}}" for y, value in enumerate(row))
                        print(f"| {row_format} |")
                    break
                elif validate == "no":
                    break
                elif validate != "yes" or validate != "no":
                    print("Invalid input. Enter yes or no.")
        return new_data
    if has_header == "no":
        new_data = []

        for _ in range(rows):
            new_row = []
            for column in zip(*data):
                if all(item.replace('.', '', 1).isdigit() for item in column):
                    column = list(map(float, column))
                    new_value = round(random.uniform(min(column), max(column)), 2)
                else:
                    new_value = random.choice(column)
                new_row.append(new_value)
            new_data.append(new_row)
        
        column_widths = [max(len(str(value)) for value in column) for column in zip(*data)]
        for x, row in enumerate(new_data[:50]):
            row_format = " | ".join(f"{str(value):^{column_widths[y]}}" for y, value in enumerate(row))
            print(f"| {row_format} |")
            if x == 0:
                print("-" * (sum(column_widths) + 3 * len(column_widths) + 1))
        
        while True:
            validate = input("\nContinue(yes/no)? ").lower()
            if not validate.isalpha():
                print("Invalid input. Enter a choice.")
            else:
                if validate == "yes":
                    column_widths = [max(len(str(value)) for value in column) for column in zip(*data)] #stackoverflow
                    for x, row in enumerate(new_data[51:]):
                        row_format = " | ".join(f"{str(value):^{column_widths[y]}}" for y, value in enumerate(row))
                        print(f"| {row_format} |")
                    break
                elif validate == "no":
                    break
                elif validate != "yes" or validate != "no":
                    print("Invalid input. Enter yes or no.")
        return new_data

# Writes synthetic data into a new csv file
def write_file(data):
    if not data:
        print("No data to write.")
        return
    
    new_file = input("New file name for synthetic data: ")
    try:
        with open(f"{new_file}.csv", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"{new_file}.csv created.")
    except Exception as e:
        print(f"Error: {e}")

def check_values(source_data, synthetic_data):
    """Compare the statistical distributions of source and synthetic data and provide total and column-wise scores."""
    if source_data is None or len(source_data) == 0:
        print("No source data loaded. Please load a file first.")
        return
    if synthetic_data is None or len(synthetic_data) == 0:
        print("No synthetic data available. Please generate data first using option 6.")
        return

    try:
        # Ask the user for a margin of error
        margin_of_error = float(input("Enter the margin of error percentage (e.g., 5 for 5%): ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Remove header row if set
    source_data_values = source_data[1:] if isinstance(source_data[0], list) and source_data[0] == source_data[0] else source_data
    synthetic_data_values = synthetic_data

    # Determine the maximum column count
    max_columns = max(len(row) for row in source_data_values)

    # Prepare for comparison
    overall_total_divergence = 0
    overall_total_values = 0
    column_scores = []

    print("\nChecking statistical divergence between source and synthetic data...\n")

    for col_index in range(max_columns):
        # Safely collect column data
        source_column = [row[col_index] for row in source_data_values if col_index < len(row)]
        synthetic_column = [row[col_index] for row in synthetic_data_values if col_index < len(row)]

        if not source_column or not synthetic_column:
            # Skip empty or mismatched columns
            print(f"Skipping column {col_index + 1} due to missing data in source or synthetic data.")
            continue

        # Get counts for each value in the column
        source_counts = get_column_counts(source_column)
        synthetic_counts = get_column_counts(synthetic_column)

        # Normalize counts to percentages
        source_total = sum(source_counts.values())
        synthetic_total = sum(synthetic_counts.values())

        total_divergence = 0
        total_values = 0

        for value in set(source_counts.keys()).union(synthetic_counts.keys()):
            source_percentage = (source_counts.get(value, 0) / source_total) * 100
            synthetic_percentage = (synthetic_counts.get(value, 0) / synthetic_total) * 100
            divergence = abs(source_percentage - synthetic_percentage)

            # Track total divergence for scoring
            total_divergence += divergence
            total_values += 1

        # Calculate average divergence for the column
        average_divergence = total_divergence / total_values if total_values > 0 else 0
        column_scores.append((col_index + 1, average_divergence))

        # Update overall scores
        overall_total_divergence += total_divergence
        overall_total_values += total_values

    # Calculate overall score for the dataset
    overall_score = overall_total_divergence / overall_total_values if overall_total_values > 0 else 0

    # Display results
    print(f"Total Dataset Score: Average Divergence = {overall_score:.2f}%")
    print("\nColumn-Wise Score Breakdown:")
    for col_index, avg_divergence in column_scores:
        status = "<good>" if avg_divergence <= margin_of_error else "<bad>"
        print(f"Column {col_index}: Average Divergence = {avg_divergence:.2f}% {status}")

def display_menu():
    """Display the main menu to the user."""
    while True:
        print("\nMain Menu:")
        print("1. Load File")
        print("2. Header Row")
        print("3. Display Read Data")
        print("4. Count For Ranges")
        print("5. Display Ranges")
        print("6. Roll Data")
        print("7. Write File")
        print("8. Check Values")
        print("9. Exit")
        try:
            choice = int(input("\nEnter Choice: "))
            if choice < 1 or choice > 9:
                print("Enter a number in range (1-9).")
        except ValueError:
            print("Enter a number.")

        if choice == 1:
            data = load_file()
            print("Data has been loaded.")
            input("\nPress Enter to go back to main menu...")
            clear_screen()
        elif choice == 2:
            if data is None:
                print("No data loaded. Please load a file first.")
            else:
                clear_screen()
                has_header = set_header_row(data)
            input("\nPress Enter to go back to main menu...")
            clear_screen()
        elif choice == 3:
            clear_screen()
            display_data(data)
            input("\nPress Enter to go back to main menu...")
            clear_screen()
        elif choice == 4:
            value_counts = count_for_ranges(data, has_header)
            input("\nPress Enter to go back to main menu...")
            clear_screen()
        elif choice == 5:
            clear_screen()
            display_ranges(value_counts)
            input("\nPress Enter to go back to main menu...")
            clear_screen()
        elif choice == 6:
            new_data = roll_data(data,has_header)
            input("\nPress Enter to go back to main menu...")
            clear_screen()
        elif choice == 7:
            write_file(new_data)
            input("\nPress Enter to go back to main menu...")
            clear_screen()
        elif choice == 8:
            check_values(data, new_data)
            input("\nPress Enter to go back to main menu...")
            clear_screen()
        elif choice == 9:
            print("Exiting program. Goodbye!")
            break

display_menu()
