# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 19:18:28 2021

@author: PNCSI
"""


# Creat List of Dictionaries...
ls =[]
ls.append({"County": "Middlesex", "Population": 100234})
ls.append({"County": "Sussex", "Population": 56234})
ls.append({"County": "Bergen", "Population": 2100234})
ls.append({"County": "Mercer", "Population": 200234})
#print(ls)
#print(ls[0]["County"])
#print(ls[0:])

#int(input("enter age"))

# Printing dictonary using f-String
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#    print(f'{county} county has {voters:,} registered voters.')
    
    
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
               {"county":"Denver", "registered_voters": 463353}, 
               {"county":"Jefferson", "registered_voters": 432438}]   

for vData in range(len(voting_data)):
    print(f'{voting_data[vData]["county"]} county has {voting_data[vData]["registered_voters"]:,} registered voters.')
 