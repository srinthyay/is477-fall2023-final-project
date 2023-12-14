# Reproduction of: Retiring Adult - New Datasets for Fair Machine Learning (IS477)

[![DOI](https://zenodo.org/badge/730421604.svg)](https://zenodo.org/doi/10.5281/zenodo.10373096)  

## Overview 

The Car Evaluation dataset is from the UC Irvine Machine Learning Repository and was uploaded on May 31, 1997. It includes information about a car's buying price (vhigh, high, med, low), it's price of maintenance (vhigh, high, med, low), the number of doors (2, 3, 4, 5more), the number of people it seats (2, 4, more), the size of the trunk(also called luggage boot)(small, med, big), the estimated safety of the car (low, med, high), and the evaluation level of the car(unacceptable, acceptable, good, very good) and the variables are called buying, maint, doors, persons, lug_boot, safety,  class, respectively. There are 6 variables and they are all categorical and the target variable is class while the other variables are features.

The analysis that I decided to do with this car dataset is find its descriptive statistics to get to understand the basics of the dataset better such as the number of rows, the most frequent attributes of a car and the counts of them.

## Analysis 

<img src = "results/summary_stats.csv" width="150">
Like mentioned before I wanted to perform some descriptive analytics on this car dataset. I first used the value_counts() function to create a frequency distribution and then I used normalize=True to just double check that the data isn't super skewed. The analysis generated a csv file with a chart and that chart broke down the frequencies. The number of cars(rows) in the car dataset was 1728 cars. The most common buying price was vhigh with a count 432, the most common maintenance condition was also vhigh with a count 432, most common number of doors was 2 with a count 432, the most common number of people the car could hold was 2 with a count of 576, the most common trunk(lug_boot) size was small with a count of also 576, the most common safety condition was low with a count of 576, and lastly the most common car condition was unacceptable with a count of 1210. These numbers suprised me as it seems that there are a lot of "bad" cars being sold to people, but we also have to consider the fact that this dataset is from 20 years ago and car quality has substantially increased. I wonder the descriptive statistics look like from a car dataset with more recent data.

## Workflow 

 <img src = "results/graph.png" width="150">

## Reproducing 

Information about the environment: 
   - macOS Version: 13.2.1
   - Python Version: 3.9.12
   - BuildVersion: 22D68

Installing the Dependencies:
   Install the following required Python packages found in the requirements.txt:
   
   pip install -r requirements.txt

Running The Script:

Execute the scripts in order:

     python scripts/prepare_data.py

     python scripts/profiling.py

     python scripts/analysis.py
     
     python scripts/dag.py

Going through with these steps will help you set up the necessary environment, run the script successfuly resulting in the proper outputs.

## License
Software License: MIT License 
- open source and freely available allowing free use of data as long as credit is given to the original contributer.
Data License: Creative Commons Attribution 4.0 License (CC-BY-4.0) 
-  permits redistribution which is the sharing and use of data/content while giving appropriate credit.

## References 

Bohanec, M. (1997). Car Evaluation. UCI Machine Learning Repository. https://doi.org/10.24432/C5JP48.