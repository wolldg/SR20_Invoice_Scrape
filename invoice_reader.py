import PyPDF2
import re
import os
from functools import lru_cache

# Searches current directory for invoices to be opened by a reader
@lru_cache
def get_lights():
    dir_files = []
    for subdir, dirs, files in os.walk('./'):
        for file in files:
            dir_files.append(file)
    bulbs = re.compile("bulbs")
    bulb_invoices = list(filter(bulbs.match, dir_files))
    return bulb_invoices

# Searches current directory for invoices to be opened by a reader
@lru_cache
def get_relays():
    dir_files = []
    for subdir, dirs, files in os.walk('./'):
        for file in files:
            dir_files.append(file)
    relays = re.compile("relay")
    relay_invoices = list(filter(relays.match, dir_files))
    return relay_invoices

# Returns a dictionary which is compiled into a df or database with other dictionaries
def light_reader ():
    # A single multidimensional array is the only way to do this because
    # there are too many duplicates of a tail number to build a dictionary
    list_of_data_lists = []

    # Patterns for regex
    tail_num_pattern = '(?:Western Michigan UniversityCollege of Aviation)(\d+\w{2})'
    pn_pattern = '(?:Part#)(\d*-*\d*-*\d*)'
    total_charge_pattern = '(?:Maintenance Release)(\d+.\d*)'
    tach_time_pattern = '(?:CirrusSR-20|CirrusSR-21|CirrusSR-22)(\d*.\d{1})'
    total_time_pattern = '(?:CirrusSR-20|CirrusSR-21|CirrusSR-22)(?:\d*.\d{1})(\d*.\d{1})'
    started_pattern = '(?:Date Started:)(\d+.\d+.\d+)'
    completed_pattern = '(?:Date Completed:)(\d+.\d+.\d+)'

    # Iterating through a list of file names
    for invoice in get_lights():
        file = open(invoice, 'rb')
        # print(type(i))
        pdf_file = PyPDF2.PdfFileReader(file)
        pdf_object = pdf_file.getPage(0)
        pdf_text = pdf_object.extractText()

        # Applying patterns to the pdf with regex to return strings
        tail_data = []

        # Then adding into a list to include into the multidimensional list
        tail = re.search(tail_num_pattern, pdf_text)
        tail = tail.group(1)
        tail_data.append(tail)

        pn = re.search(pn_pattern, pdf_text)
        pn = pn.group(1)
        tail_data.append(pn)

        cost = re.search(total_charge_pattern, pdf_text)
        cost = cost.group(1)
        tail_data.append(cost)

        tach = re.search(tach_time_pattern, pdf_text)
        tach = tach.group(1)
        tail_data.append(tach)

        tot_time = re.search(total_time_pattern, pdf_text)
        tot_time = tot_time.group(1)
        tail_data.append(tot_time)

        start = re.search(started_pattern, pdf_text)
        start = start.group(1)
        tail_data.append(start)

        end = re.search(completed_pattern, pdf_text)
        end = end.group(1)
        tail_data.append(end)

        list_of_data_lists.append(tail_data)

    file.close()

    return list_of_data_lists

def relay_reader ():
    # A single multidimensional array is the only way to do this because
    # there are too many duplicates of a tail number to build a dictionary
    list_of_data_lists = []

    # Patterns for regex
    tail_num_pattern = '(?:Western Michigan UniversityCollege of Aviation)(\d+\w{2})'
    pn_pattern = '(?:Part#)(\d*-*\d*-*\d*)'
    total_charge_pattern = '(?:Maintenance Release)(\d+.\d*)'
    tach_time_pattern = '(?:CirrusSR-20|CirrusSR-21|CirrusSR-22)(\d*.\d{1})'
    total_time_pattern = '(?:CirrusSR-20|CirrusSR-21|CirrusSR-22)(?:\d*.\d{1})(\d*.\d{1})'
    started_pattern = '(?:Date Started:)(\d+.\d+.\d+)'
    completed_pattern = '(?:Date Completed:)(\d+.\d+.\d+)'

    # Iterating through a list of file names
    for invoice in get_relays():
        file = open(invoice, 'rb')
        pdf_file = PyPDF2.PdfFileReader(file)
        pdf_object = pdf_file.getPage(0)
        pdf_text = pdf_object.extractText()
        #print(pdf_text)

        tail_data = []

        # Applying patterns to the pdf with regex to return strings
        # Then adding into a list to include into the multidimensional array
        tail = re.search(tail_num_pattern, pdf_text)
        tail = tail.group(1)
        tail_data.append(tail)

        pn = re.search(pn_pattern, pdf_text)
        pn = pn.group(1)
        tail_data.append(pn)

        cost = re.search(total_charge_pattern, pdf_text)
        cost = cost.group(1)
        tail_data.append(cost)

        tach = re.search(tach_time_pattern, pdf_text)
        tach = tach.group(1)
        tail_data.append(tach)

        tot_time = re.search(total_time_pattern, pdf_text)
        tot_time = tot_time.group(1)
        tail_data.append(tot_time)

        start = re.search(started_pattern, pdf_text)
        start = start.group(1)
        tail_data.append(start)

        end = re.search(completed_pattern, pdf_text)
        end = end.group(1)
        tail_data.append(end)

        list_of_data_lists.append(tail_data)

        file.close()

    return list_of_data_lists

