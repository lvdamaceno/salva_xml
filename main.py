import pandas as pd
import xml.etree.ElementTree as ET
import os
import time


def update_file_name(file):
    # Update file name
    tree = ET.parse(file)
    root = tree.getroot()
    infnfe = root[0].attrib
    filename = infnfe['Id']
    print(filename)
    os.rename(file, f'{filename}.xml')


def create_xml(filename):
    data = pd.read_csv(f"{filename}.csv")
    os.mkdir(f'./{filename}')
    os.chdir(f'./{filename}')
    i = 0

    for index, row in data.iterrows():
        i += 1
        # Take content
        content = row[0]
        # Open text file in write mode
        text_file = open("sample.xml", "w")
        # Write content to file
        n = text_file.write(content)

        if n == len(content):
            print(f"Success! Xml {i} saved.")
        else:
            print("Failure!")

        # Close file
        text_file.close()
        update_file_name('sample.xml')


def timer(function, parameter):
    # Start timer
    start_time = time.perf_counter()
    # Execute function
    function(parameter)
    # End timer
    end_time = time.perf_counter()
    # Calculate elapsed time
    elapsed_time = end_time - start_time
    # Print elapsed timer
    return print("Elapsed time: ", elapsed_time)


if __name__ == '__main__':
    timer(create_xml, '2023_top10')
