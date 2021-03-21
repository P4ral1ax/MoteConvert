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
    metadata = data[0]
    laps = data[1]

    # Write Date
    date = metadata.values[6][1]
    zeros = 32 - len(date)
    outfile.write(date.encode() + b"\x00" * zeros)

    # Write Time
    time = metadata.values[7][1]
    zeros = 32 - len(time)
    outfile.write(time.encode() + b"\x00" * zeros)

    # Write Driver
    driver = metadata.values[3][1]
    zeros = 64 - len(driver)
    outfile.write(driver.encode() + b"\x00" * zeros)

    # Write Car
    car = metadata.values[2][1]
    zeros = 128 - len(car)
    outfile.write(car.encode() + b"\x00" * zeros)

    # Write Track + lots of Zeros
    track = metadata.values[1][1]
    zeros = 1152 - len(track)
    outfile.write(track.encode() + b"\x00" * zeros)

    # Write Unknown
    outfile.write(b"\x22\x02\xD2\x00\x00\x00\x54\x65\x73\x74")
    outfile.write(b"\x00" * 60)

    # Write Comment



def write_telemetry_headers(outfile, data):
    pass


def write_telemetry(outfile):
    pass


def parse_csv(outfile, csv_file):
    metadata = parse.read_metadata(csv_file)
    write_metadata(outfile, metadata)
    
    data_desc = parse.get_telemetry_headers(csv_file) # Does Nothing
    #write_telemetry_headers(outfile, data_desc)
    
    data = parse.read_telemetry(csv_file) 
    #write_telemetry(outfile, csv)


def test_write_header():
    outfile = open("out/test.ld", "wa")
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
    
    outfile = open("out/test.ld", "wb")
    csv = "data/07-2020-Liberator-Session1.csv"
    
    write_header(outfile, "garbage", "garbage")
    parse_csv(outfile, csv)
    # test_write_header()
    
    end = time.perf_counter()
    print(f"Task Completed In : {end-start:0.2f}s")
    


main()