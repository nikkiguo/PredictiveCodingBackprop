#!/bin/bash

input_directory="."
python_script="extract_accuracy.py"

for input_file in "$input_directory"/*; do
    if [ -f "$input_file" ]; then
        base_name=$(basename "$input_file")
        
        # skip extract_accuracy.py, compare.py, extract_all.sh
        if [[ "$base_name" == "extract_accuracy.py" || "$base_name" == "compare.py" || "$base_name" == "extract_all.sh" ]]; then
            echo "Skipping file: $input_file"
            continue
        fi

        echo "Processing file: $base_name"
        python3 $python_script "$base_name" 
    fi
done

echo "Processing complete for all files."
