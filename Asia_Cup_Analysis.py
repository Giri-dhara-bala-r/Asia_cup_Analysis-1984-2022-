#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import math
def validate_country(country):
    country_check = 0
    with open("asiacup.csv", "r") as fl:
        x = fl.readline()
        while country_check == 0:
            x = fl.readline()
            if x.strip() == '':
                break
            row = x.strip().split(",")
            if row[0].strip().lower() == country.lower() or row[0].strip().lower().replace(' ','') == country.lower():
                country_check = 1;break;
    return country_check

def analyse(country):
    result = {}
    with open("asiacup.csv", 'r') as fl:
        d_check = 0
        x = fl.readline()
        h = x.split(",")
        while d_check == 0:
            x = fl.readline().strip()
            if x == '':
                d_check = 1;break;
            r = x.split(",")
            if r[0].strip().lower() != country.lower() and r[0].strip().lower().replace(' ','') != country.lower():
                continue
            if r[4] not in result:
                result[r[4]] = {i:eval(r[h.index(i)]) if r[h.index(i)].strip() != '' else 0 for i in head}
                result[r[4]]["total_match"] = 1
            else:
                for i in head:
                    inx = h.index(i)
                    result[r[4]][i] += eval(r[inx].strip()) if r[inx].strip() != '' else 0
                result[r[4]]["total_match"] += 1
    final_result = {}
    for year in result:
        final_result[year] = {x:round(result[year][x]/result[year]["total_match"],2) for x in result[year]}

    return(final_result)

option =['Afghanistan','Bangladesh','Hong Kong','India','Pakistan','Sri Lanka','UAE']
with open("asiacup.csv", 'r') as file:
    head= file.readline().strip()
    head=head.split(',')

    
sel=0
while sel==0:
    inn =input('Choose your analysis\n(batting or bowling) : ')
    if inn.lower() == 'batting':
        print('\nYou have selected '+inn+' Analysis\n')
        head= head[7:15]
        sel=1
    elif inn.lower() == 'bowling':
        print('\nYou have selected '+inn+' Analysis\n')
        head= head[15:18]
        sel=1
    else:
        print('\nKindly enter a valid input\n')
        
if sel ==1:
    chk = 0
    while chk == 0:
        print(option)
        ct = input("\nSelect one country from the above options for getting Analytical graphs: ")
        if ct.lower() == "end":
            print ("\nYou are existing the application.  Bye.")
            break
        ct_validation = validate_country(ct)
        if ct_validation == 0:
            print ("\nGiven Country is not  valid.\n")
            chk = 0
        else:
            print ("\nCountry validation succeeded!!\n")
            print (ct.upper()+' '+inn.upper()+' '+'ANALYSIS\n')
            bating_analysis = analyse(ct)
            plot_col = 2
            plot_row = math.ceil(len(head) / 2)
            count = 0
            plt.figure(figsize=(6,6))
            for col in head:
                count += 1
                year = []
                value = []
                for yr in bating_analysis:
                    year.append(yr);value.append(bating_analysis[yr][col])
                plt.subplot(plot_row,plot_col,count)
                plt.bar(year,value,color='#6FC0F2')
                plt.plot(year,value,color="#2D8BBA")
                plt.scatter(year,value,color="#2D8BBA")
                plt.title(col)
                plt.xlabel("Year")
                plt.ylabel("Avg"+' '+col)
                plt.xticks(rotation=90)
            plt.subplots_adjust(right=2.5,top=3.5)
            plt.savefig("%s %s_Analysis_AC.jpg" %(ct,inn), bbox_inches="tight")
            plt.show()
            chk=1;break;

