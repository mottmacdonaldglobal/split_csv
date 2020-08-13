"""
Helper function to complement main split_csv function

    Split a column in the csv into multiple columns using a given character
    
Author: Maria Mingallon
Link to github: https://github.com/mottmacdonald/split_csv

"""

# note input variables are declared in runme.py file

# builtin modules
import os

# 3rd party modules
import pandas as pd
import numpy as np


def split_col(source_filepath, char, index, name_col_split, name_new_col):
    """
        Split a column in the csv into multiple columns using a given character 'char'
 
        Indicate index of column to be picked up from the split, starting at 0 
        e.g. using '-' as split AA-1234-ABCDEFG, we are interested in picking up '1234', we shall indicate index = 1
 
        Indicate the name of the column to split
        
        Rejoin the dataframe for further processing of the csv data

    """
    df=pd.read_csv(source_filepath)

    #new data frame with split value columns
    new = df[name_col_split].str.split(char, n = 1, expand = True)
    #split again to get only the data between the first two instances of 'char'
    new = new[index].str.split(char, n = 1, expand = True)

    # making separate column for new data resulting from split 
    df[name_new_col]=new[0]

    return df