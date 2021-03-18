# Brayden Werner
# Motec_convert.py
# Converts .csv files to the Motec ld format

from parse import *
from os import write
from sys import argv 
import csv
import sys
import time 
import datetime


def write_header(outfile, unique1, unique2):
    # Constant
    outfile.write(b"\x40\x00\x00\x00\x00\x00\x00\x00\x48\x34\x00\x00")
    
    # Unique
    outfile.write(b"\x40\xD0")

    # Constant
    outfile.write(b"\x00" * 22)
    outfile.write(b"\xE2\x06")
    outfile.write(b"\x00" * 28)
    outfile.write(b"\x40\x42\x0F\x00\xE7\x2E\x00\x00\x41\x44\x4C\x00\x00\x00"\
                  b"\x00\x00\xA4\x01\x80")

    # Unique
    outfile.write(b"\x00\x42\x01\x42\x01\x3C\x00\x01\x00")


def write_metadata(outfile):
    today = datetime.date.today()
    date = (f"{today.day}/{today.month}/{today.year}")
    zeros = 32 - len(date)
    outfile.write(date.encode() + b"\x00" * zeros)

def write_hex(outfile):
    pass


def parse_csv(csv_file):
    # Read Metadata @ write
    # Read all datatypes @ write
    # Read and write telemetry
    pass


def main():
    start = time.perf_counter()
    outfile = open("../out/test.ld", "wb")
    write_header(outfile, "garabage", "garabage")
    write_metadata(outfile)
    end = time.perf_counter()
    print(f"Task Completed In : {end-start:0.2f}s")
    # if(len(sys.argv) != 2):
    #     print("Invalid Format : python3 motec_convert.py {filename}")
    #     exit()
    # else:
    #     try:
    #         f_name = argv[1]
    #         file = open(f_name, "r")
    #         parse_csv(file)
        
    #     except:
    #         print(f"Error when opening File {argv[1]} ... Quitting")
    #         exit()
main()