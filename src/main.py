# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
import os
import time
import pandas as pd

# Get the current work directory
workspace_dir = os.getcwd()

# Make a function to get the size of the file
def get_file_size(file_name):
    return os.path.getsize(file_name)

# Make a function to get and convert the date time
def get_file_date(file_name):
    mod_time = os.path.getmtime(file_name)
    mod_time_struct = time.gmtime(mod_time)
    return time.strftime("%d/%m/%Y %H:%M:%S", mod_time_struct)

# Get a list with all the files of the directory
files = os.listdir(workspace_dir)

# Create a empty list to store 
file_data = []

# Loop through the files list to call the functions and append the results into the empty list
for file_name in files:
    file_size = get_file_size(file_name)
    file_mod_date = get_file_date(file_name)
    file_data.append([
                        file_name,
                        file_size,
                        file_mod_date
    ])

# Print to check
print(file_data)


# Convert the list into DataFrame
df = pd.DataFrame(file_data)

# Name the columns
df.columns = ["Name", "Size", "Last modification"]

# Print the DataFrame
print (df)

# Convert to csv
csv = df.to_csv

# Print the csv
print(csv)


# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV