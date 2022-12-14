import csv

def get_data(file_name):
    '''
    Receive an file_name, iterate through it and return all rows in a list

    Args:

    file_name(*.csv) = .csv to read
    '''
    rows = [] # Create an empty list
    data_file = open(file_name, 'r') # Open file in read mode ('r')
    reader = csv.reader(data_file) # Use csv.reader to read the file

    next(reader, None) # Don't raise exception if no line exist

    for row in reader: # Iterate through each line
        rows.append(row) # Append the line to the list
    return rows # Return list