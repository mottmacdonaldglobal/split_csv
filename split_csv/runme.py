"""
Helper functions to complement main split_csv function

    Split a column in the csv into multiple columns using a given character
    Check uniqueness of data in a certain column
    
Author: Maria Mingallon
Link to github: https://github.com/mottmacdonaldglobal/split_csv

"""

# builtin modules
import os

# 3rd party modules
import pandas as pd
import numpy as np


## Input data specific to project

### general
source_filepath = r'C:\Users\yourpath\file.csv'

### specific for split_csv.py functions
input_path = r'C:\Users\yourpath'
dest_folder = os.path.join(input_path,'out')
split_file_prefix = 'file'
records_per_file = 5000

### specific for helpers.py functions
name_col_split = 'A'
name_new_col = 'B'
index = 1
char = '-'
check_col = 'C'

#local modules
from split_csv.split_col import split_col
from split_csv.split_csv import split_csv
from split_csv.check_dup import check_dup

## Run the functions

check_dup(source_filepath, check_col)

split_csv(source_filepath, dest_folder, split_file_prefix, records_per_file, char, index, name_col_split, name_new_col)

