import json

# Read the JSON file
with open('aviation.json', 'r') as file:
    data = json.load(file)

# Open the output CSV file in write mode
with open('chacon.csv', 'w') as csv_file:
    count = 0  # Counter to limit output to 5 lines

    for item in data:
        # Simulate the required fields
        name = f"Record-{count + 1}"  # Use a placeholder or generate a name
        html_url = f"https://example.com/record/{item.get('icaoId', 'Unknown')}"  # Simulate URL
        updated_at = item.get('receiptTime', '')  # Use receiptTime as updated_at
        visibility = "public"  # Assume visibility is public

        # Print extracted fields for debugging
        print(f"Extracted fields - Name: {name}, URL: {html_url}, Updated At: {updated_at}, Visibility: {visibility}")

        # Skip entries with missing critical fields
        if not (name and html_url and updated_at and visibility):
            print("Skipping due to missing fields.")
            continue

        # Create a comma-separated line
        csv_line = f"{name},{html_url},{updated_at},{visibility}\n"

        # Write the line to the CSV file
        csv_file.write(csv_line)

        # Increment the counter
        count += 1

        # Stop after writing 5 lines
        if count == 5:
            break

