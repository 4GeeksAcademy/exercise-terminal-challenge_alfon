#!/bin/bash

## Worked in the terminal ##
# Create an empty .csv file
touch output.csv

# list the main directory and paste the output into the .csv
ls -l ../ | tee output.csv

# Display the output
cat output.csv