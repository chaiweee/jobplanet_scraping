#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 09:41:07 2023

@author: tanchaiwee
"""
import csv
# write to excel function

def write_to_csv(dict_data):
    print('Writing result to csv...')
    
    keys = dict_data[0].keys()
    
    filename = 'companies.csv'
    
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dict_data)
    
    print('Finish writing result to csv')
    return filename