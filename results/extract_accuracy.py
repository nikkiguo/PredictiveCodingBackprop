import re
import sys
import os

def extract_accuracy(input_file, output_file):
    accuracy_pattern = re.compile(r"TEST ACCURACY:\s*(\d+\.\d+)")
    
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    accuracies = []

    for line in lines:
        match = accuracy_pattern.search(line)
        if match:
            accuracies.append(match.group(1))
    
    with open(output_file, 'w') as outfile:
        for accuracy in accuracies:
            outfile.write(f"{accuracy}\n")
    
    print(f"Extraction complete - wrote accuracies to {output_file}")

def main():
    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' doesn't exist.")
        sys.exit(1)

    base_name, _ = os.path.splitext(input_file)
    output_file = f"./test_accuracies/{base_name}_accuracies.txt"

    extract_accuracy(input_file, output_file)

if __name__ == "__main__":
    main()
