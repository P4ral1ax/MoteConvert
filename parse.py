'''
File where CSV file will be parsed
'''
import pandas as pd
import csv

def read_metadata(csv_file):
    pass
    metadata = pd.read_csv(csv_file, nrows=12, header= None, error_bad_lines=False)
    laps = pd.read_csv(csv_file, skiprows=12, nrows=1, header=None, error_bad_lines=False)
    return(metadata, laps)

def get_telemetry_headers(csv_file):
    pass

def read_telemetry(csv_file):
    data_desc = pd.read_csv(csv_file, skiprows=14, nrows=4, header=None, error_bad_lines=False)
    data = pd.read_csv(csv_file, skiprows=18, header=None, error_bad_lines=False)
    return(data)

def parse_telemetry():
    pass