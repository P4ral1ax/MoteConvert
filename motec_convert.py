# Brayden Werner
# Motec_convert.py
# Converts .csv files to the Motec ld format

import parse
from os import write
from sys import argv 
import csv
import sys
import time 
import datetime


def write_header(outfile, unique1, unique2):
    outfile.write(b"\x40\x00\x00\x00\x00\x00\x00\x00\x48\x34\x00\x00")
    outfile.write(b"\x40\xD0")
    outfile.write(b"\x00" * 22)
    outfile.write(b"\xE2\x06")
    outfile.write(b"\x00" * 28)
    outfile.write(b"\x40\x42\x0F\x00\xE7\x2E\x00\x00\x41\x44\x4C\x00\x00\x00"\
    b"\x00\x00\xA4\x01\x80")
    outfile.write(b"\x00\x42\x01\x42\x01\x3C\x00\x01\x00")


def write_metadata(outfile, data):
    today = datetime.date.today()
    date = (f"{today.day}/{today.month}/{today.year}")
    zeros = 32 - len(date)
    outfile.write(date.encode() + b"\x00" * zeros)


def write_telemetry_headers(outfile, data):
    pass


def write_telemetry(outfile):
    pass


def parse_csv(outfile, csv_file):
    metadata = parse.read_metadata(csv_file)
    write_metadata(outfile, metadata)
    
    data_desc = parse.get_telemetry_headers(csv)
    write_telemetry_headers(outfile, data_desc)
    
    data = parse.parse_telemetry(csv)
    write_telemetry(outfile, csv)


def test_write_header():
    outfile = open("out/test.ld", "wb")
    write_header(outfile, "garabage", "garabage")
    write_metadata(outfile)


def test_read_csv_header():
    csv = "data/07-2020-Liberator-Session1.csv"
    data = parse.read_metadata(csv)
    print(f"Data : \n------------\n {data[0]}")
    print(f"\nLaps : \n------------\n {data[1]}")
    
    data = parse.read_telemetry(csv)
    print(data)



def main():
    start = time.perf_counter()
    
    test_read_csv_header()
    # test_write_header()
    
    end = time.perf_counter()
    print(f"Task Completed In : {end-start:0.2f}s")
    


main()