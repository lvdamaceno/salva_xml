import pandas as pd
import xml.etree.ElementTree as ET
import os
import time


def update_file_name(file):
    # creates the xml tree
    tree = ET.parse(file)
    root = tree.getroot()
    infnfe = root[0].attrib
    # gets Id tag from nfe xml
    filename = infnfe['Id']
    print(filename)
    # Update file name
    os.rename(file, f'{filename}.xml')


def create_xml(filename):
    # creates de pd
    data = pd.read_csv(f"{filename}.csv")
    # creates a folder
    os.mkdir(f'./{filename}')
    # set the folder as actual folder
    os.chdir(f'./{filename}')
    # initialize counter
    i = 0

    # iterates the xml content
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
        # changes the xml name to its CHAVE NFE
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
    # Creates the xmls files and count the time elapsed
    timer(create_xml, '2023_top10')
