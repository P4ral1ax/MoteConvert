# Brayden Werner
# Motec_convert.py
# Converts .csv files to the Motec ld format

from sys import argv 
import csv
import sys 


def write_hex(outfile):
    pass


def parse_csv(csv_file):
    # Read Metadata @ write
    # Read all datatypes @ write
    # Read and write telemetry
    pass


def main():
    if(len(sys.argv) != 2):
        print("Invalid Format : python3 motec_convert.py {filename}")
        exit()
    else:
        try:
            f_name = argv[1]
            file = open(f_name, "r")
            parse_csv(file)
        
        except:
            print(f"Error when opening File {argv[1]} ... Quitting")
            exit()
main()