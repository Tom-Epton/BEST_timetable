#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:16:35 2022

@author: tomepton

"""
#initialise_stuff 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import imgkit
import PIL as pil 

pd.set_option("display.max_rows", 400)
csv_file = pd.read_csv('CSV_code/07_2018.csv')
day = 15
month = np.linspace(1, 30, 30)


def csv_cleaner(csv_file):
    """
    Cleans the csv file
    """
    dates_df = pd.read_csv('CSV_code/07_2018.csv')
    dates_df.columns = dates_df.iloc[0] 
    dates_df = dates_df.iloc[1: , :]
    dates_df = dates_df.iloc[ : , :-1]
    dates_df = dates_df.fillna(0)
    
    return dates_df




def date_selector(day, dates_df):
    
    """
    outputs the data for some given day 
    """
    
    day = dates_df[day*13:(day*13 + 10)]
    
    
    return day 


"""
def is_pool_open(day, dates_df):
    
    open_or_closed = [] 
    day_check = date_selector(day, dates_df)
    for j in range(np.shape(day_check)[1]):
        if sum(day_check[:, j])
        
    
    
    return open_or_closed
"""

def public_swim(day, dates_df):
    
    # current rules for public swim 
    # if lane occupied in that hour but lane free then yes 
    # if hour of no lane, not open (if all elements of col sum to zero)
    
    
    """
    Checks to see if there's space for public swim that day
    """
    
    day_check = date_selector(day, dates_df)
    
    day_with_public = [] 
    for i in range(np.shape(day_check)[0]):
        for j in range(np.shape(day_check)[1]):
            if day_check[i,j] == 0.0:
                day_with_public = 'yes'
            else:
                day_with_public = 'pool full'
                
    
    return day_with_public 

# if pool space check not empty - if empty all day, pool closed 

def image_from_date(date_data):
    
    """
    Turns spreadsheet information for a day 
    into a matrix of ones and zeros to be turned 
    into an image. 
    """
    
    # problem here - array wrong shape 
    # row deletion of lane labels causes problem in re-shape 
    # how to fix? 
    
    image = np.delete(date_data, [0, 1])
    print(np.shape(image))
    
    for i in range(np.shape(image)[0]):
        for j in range(np.shape(image)[1]):
            if type(image[i, j]) == str:
                image[i, j] = 1 
            else:
                pass 
            
    for i in range(np.shape(image)[0]):
        for j in range(np.shape(image)[1]):
            image[i, j] = float(image[i, j])
    
    return image 

def check_opening():
    
    image = image_from_date(date_data)
    
    open_or_closed_today = [] 
    
    if np.sum(image) == 0:
        open_or_closed_today = "closed today"
    else:
        open_or_closed_today = "open"
    
    return open_or_closed_today


dates_df = csv_cleaner(csv_file)
date_data = date_selector(day, dates_df)
# web_page_output = np.array(image_from_date(date_data), dtype = float)

img_filepath = './timetable/photo.png'
imgkit.from_string(date_data.to_html(), img_filepath)











