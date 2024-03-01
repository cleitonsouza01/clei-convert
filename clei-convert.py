import csv
import sys
from datetime import datetime
import os


def convert_date_format(date_string):
    """Convert date from dd/mm/yyyy to mm/dd/yyyy format."""
    try:
        return datetime.strptime(date_string, '%d/%m/%Y').strftime('%m/%d/%Y')
    except ValueError:
        # Return the original string if it's not a valid date in the expected format
        return date_string


def main(input_file_path):
    """Main function to convert date format in a CSV file."""
    print(f"Converting file: {input_file_path}")
    # Construct the output file path by appending '-converted' before the file extension
    file_name, file_extension = os.path.splitext(input_file_path)
    output_file_path = f"{file_name}-converted{file_extension}"

    date_field_index = 3  # Adjust this index based on your needs

    with open(input_file_path, mode='r', newline='', encoding='utf-8') as infile, \
            open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Convert the date format in the specified field
            row[date_field_index] = convert_date_format(row[date_field_index])
            writer.writerow(row)

    print(f"File converted successfully: {output_file_path}")


if __name__ == "__main__":
    print("### Clei-Convert - version 0.01 ###")
    print("Author: Cleiton Souza")
    print("Script to convert date format in a CSV file.\n")
    print("Starting conversion...\n")
    if len(sys.argv) < 2:
        print("Usage: clei-convert.exe <input_file_path>")
    else:
        input_file_path = sys.argv[1]
        try:
            main(input_file_path)
            print("\nConversion completed.")
        except FileNotFoundError:
            print(f"File not found: {input_file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
