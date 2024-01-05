#Rename columns
from asyncore import read
from operator import concat
from statistics import mean
import pandas as pd

covid = pd.read_table("data\scraped_data.txt")

covid = pd.DataFrame(covid)

covid = (covid.rename(columns={'jobs_lvl':'jobs_lvl_1000', 'jobs_mth':'jobs_month', 
    'unemp_rate':'unemploy_rate', 'unemp_mil':'unemploy_mil','emp_pop':'employ_pop', 
    'infl_rate':'infl_rate_perc','snp500_mean':'snp500_mean_lvl', 'public_debt':'public_debt_tril'}))


# Data wrangling 
#1. Select all columns that start with a j (i.e., (^j)) or contain an a (i.e., (a)). 
df = (covid.filter(regex ='(^j)|(a)'))
df

#2. Using your new data frame, select months with jobs_lvl_1000 > 135,000   
df.query('jobs_lvl_1000 > 135000')

#3. Perform the previous two operations together and save it as a new data frame
df2 = (covid.filter(regex ='(^j)|(a)')
       .query('jobs_lvl_1000 > 135000'))
df2

# Calculate the mean of jobs_lvl_1000
covid.agg({'jobs_lvl_1000':['mean']})

# Calculate the median of jobs_lvl_1000
covid.agg({'jobs_lvl_1000':['median']})

# Using Pandas piping notation, select all columns that end with l or contain the letter o.
# Additionally, select rows in which snp500_mean_lvl is greater than or equal to 3000
(covid.filter(regex = 'l$|o')
 .query('snp500_mean_lvl >= 3000'))

# Using the query just performed, calculate the mean and median of jobs_lvl_1000.
(covid.filter(regex = 'l$|o')
 .query('snp500_mean_lvl >= 3000')
 .agg({'jobs_lvl_1000':['mean','median']}))
