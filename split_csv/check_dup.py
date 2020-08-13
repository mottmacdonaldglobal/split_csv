"""
Helper function to complement main split_csv function

    Check uniqueness of data in a certain column
    
Author: Maria Mingallon
Link to github: https://github.com/mottmacdonald/split_csv

"""

# note input variables are declared in runme.py file

# builtin modules
import os

# 3rd party modules
import pandas as pd
import numpy as np


def check_dup(source_filepath, check_col):

    df=pd.read_csv(source_filepath)

    if len(df[check_col].unique().tolist()) == len(df[check_col].tolist()):
        return print('Perfect! Values of '+ check_col + 'are all unique')

    elif len(df[df.duplicated()]) > 0:
        return print('Sorry, it looks like some rows are actually duplicated: \n' 
                        + df[df.duplicated()])
    elif len(df[df.duplicated()]) == 0:
        dup_list = df[df.duplicated([check_col],keep = 'first')]
        return print('Great news, full rows are all unique! However, there are some duplicates in the column:',check_col,'\n',
                        dup_list,
                        sep='\n')
