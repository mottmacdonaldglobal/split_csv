"""
Split a source csv into multiple csvs of equal numbers of records,
    except the last file.

    Includes the initial header row in each split file.

    Includes for last few rows when counter exceeds total number of rows.

    Split files follow a zero-index sequential naming convention like so:

        `{split_file_prefix}_0.csv`

Author: Maria Mingallon
Link to github: https://github.com/mottmacdonald/split_csv

Adapted from: https://stackoverflow.com/questions/36445193/splitting-one-csv-into-multiple-files-in-python/36445821 
by Affifa Taskeen https://stackoverflow.com/users/10739107/affifa-taskeen

"""

# note input variables are declared in runme.py file

# builtin modules
import os

# 3rd party modules
import pandas as pd
import numpy as np

# local modules
from split_csv.split_col import split_col


def split_csv(source_filepath, dest_folder, split_file_prefix, records_per_file, char, index, name_col_split, name_new_col):
    """
    Split a source csv into multiple csvs of equal numbers of records,
    except the last file.

    Includes the initial header row in each split file.

    Split files follow a zero-index sequential naming convention like so:

        `{split_file_prefix}_0.csv`
    """
    #df = pd.read_csv(source_filepath)

    df = split_col(source_filepath, char, index, name_col_split, name_new_col)

    file_idx = 0
    low = 0
    high = records_per_file

    while (high < len(df)):
        df_new = df[low:high] #slicing dataframe based on index
        target_filename = f'{split_file_prefix}_{file_idx}.csv'
        target_filepath = os.path.join(dest_folder, target_filename)
        df_new.to_csv(target_filepath, index = False, index_label = False) #output file
        low = high #changing the lower limit to the previous high for next iteration
        high = high + records_per_file #changing the upper limit for next iteration
        file_idx=high #changing the file_idx to the upper limit for next iteration

    # add to include for last few rows when counter exceeds total number of rows
    df_last = df[low:(df.shape[0] - 1)]
    file_idx = df.shape[0]
    target_filename = f'{split_file_prefix}_{file_idx}.csv'
    target_filepath = os.path.join(dest_folder, target_filename)
    df_new.to_csv(target_filepath, index = False, index_label=False) #output files

