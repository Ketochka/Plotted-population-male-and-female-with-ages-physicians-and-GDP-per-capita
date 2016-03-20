
# coding: utf-8

# In[76]:

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
from matplotlib import style
from matplotlib.collections import PatchCollection
from matplotlib.patches import Circle
from matplotlib.widgets import Slider, Button, RadioButtons


style.use('mystylepop_age')

fig, ax = plt.subplots(1, 1, figsize=(16, 8))

## reading data from csv
male_female_age = '/home/ketka/1/PYex/matplotlib/male_female_populatio_by_age_plus physicians_and_gdp/Male_Female_physicians.csv'


male = [[]]*17
female = [[]]*17

for i in range(0,17):
    male[i] = []
    female[i] = []
    
countries = []
population = []
gdp = []
physicians = []

## Reading and appending all the countries and population for every year
## countries_pop - list of all the countries
## pp[i][j] - population by country for a year, where i=year, j=country
with open(male_female_age) as ff:
        reader_ff = csv.reader(ff)
        next(reader_ff)
        for row in reader_ff:
            countries.append(str(row[0]))
            population.append(float(row[1]))
            gdp.append(float(row[2]))
            physicians.append(float(row[3]))
            for j in range(0, 17):
                female[j].append(int(row[j+4]))
                male[j].append(int(row[j+21]))

              
                
female_ = []
male_ = []
u = []
physicians_ = 0
gdp_ = 0
def select_country(k):
    for i in range(0,17):
            female_.append(female[i][k])
            male_.append(male[i][k])
            u.append(i*5)
            physicians_ = (physicians[k])
            gdp_ = (gdp[k]/population[k])
     
    ax5= plt.subplot2grid((12,6), (0,4), rowspan=4, colspan=2)
    plt.text(0.05,0.4,countries[k], color='#ffffff', fontsize=36, fontweight='bold')
    plt.axis('off') 
    
    ax1 = plt.subplot2grid((12,6), (0,0), rowspan=4, colspan=2)
    plt.title('GDP per person, $', color='#ffcc66',fontsize=14)
    #plt.xlim(0)
    plt.axis('off')
    patches = []
    
    standard_cn =  gdp[0]/population[0]
    circle1 = Circle((0, standard_cn/2),standard_cn/2)
    patches.append(circle1)
    p = PatchCollection(patches, facecolor='#035805')
    ax1.add_collection(p)
    if gdp_<9999:
        ax1.text((0-standard_cn/5.2),standard_cn/2.2,str(round(gdp_)), color='#ffdd99', fontsize=20, fontweight='bold')
    else:
        ax1.text((0-standard_cn/4),standard_cn/2.2,str(round(gdp_)), color='#ffdd99', fontsize=20, fontweight='bold')
    ax1.axis('equal')
    
    
    ax4 = plt.subplot2grid((12,6), (0,2), rowspan=4, colspan=2)
    plt.title('Physicians per 1000', color='#ffcc66',fontsize=14)
    plt.xlim(0)
    plt.axis('off')
    patches = []
    colors = ['#006766', '#ffcc66']
    circle1 = Circle((0, standard_cn/2), standard_cn/2)
    patches.append(circle1)
    p = PatchCollection(patches, facecolor='#035805')
    ax4.add_collection(p)
    if k==1 or k==7:
        ax4.text((0-standard_cn/6.9),standard_cn/2.2,str(physicians_), color='#ffdd99', fontsize=20, fontweight='bold')
    else:    
        ax4.text((0-standard_cn/5.2),standard_cn/2.2,str(physicians_), color='#ffdd99', fontsize=20, fontweight='bold')
    ax4.axis('equal')
        
    # the barchart of the data
    # Female population
    ax2 = plt.subplot2grid((12,4), (5,0), rowspan=7, colspan=2)
    ax2.bar(u, female_, 5, facecolor='#035805')
    if k==6:
        ax2.text(22,650000,'WTF?', color='#ffffff', fontsize=30, fontweight='bold')
    plt.xlabel('Ages', color='#ffcc66')
    plt.locator_params(axis = 'x', nbins = 8)
    plt.locator_params(axis = 'y', nbins = 6)
    plt.title('Female population', color='#ffcc66',fontsize=14)
    plt.ticklabel_format(style='plain')

    # Male population
    ax3 = plt.subplot2grid((12,4), (5,2), rowspan=7, colspan=2, sharey=ax2)
    ax3.bar(u, male_, 5, facecolor='#035805')
    plt.xlabel('Ages', color='#ffcc66')
    plt.locator_params(axis = 'x', nbins = 8)
    plt.locator_params(axis = 'y', nbins = 6)
    plt.title('Male population', color='#ffcc66',fontsize=14)
    plt.ticklabel_format(style='plain')
    plt.tick_params(axis='both', which='both', bottom='off', top='off',
                    labelbottom='on', left='off', right='off', labelleft='off') 


     
    
country = 11
select_country(country) 
plt.savefig('%s.png' %countries[country])
## select_country(6) -- poor women: https://www.youtube.com/watch?v=0ytiXRyc0qk 

###.........................###
### and here's the buttons part:
### there are 12 countries in total, I show buttons for the first 3
### plotting takes a lot of time
### so I see buttons as something inefficient
### that's much easier would be to make buttons in web and just simply assign appropriate images

#resetax0 = plt.axes([0.92, 0.955, 0.08, 0.04])
#button0 = Button(resetax0, countries[0], color='#909090', hovercolor='0.975')
#l = 0.042
#resetax1 = plt.axes([0.92, 0.955-l, 0.08, 0.04])
#resetax2 = plt.axes([0.92, 0.955-2*l, 0.08, 0.04])
#button1 = Button(resetax1, countries[1], color='#909090', hovercolor='0.975')
#button2 = Button(resetax2, countries[2], color='#909090', hovercolor='0.975')

#def clck0(p):
#        select_country(0)
#        plt.show()
#def clck1(p):
#        select_country(1)
#        plt.show()
#def clck2(p):
#        select_country(2)
#        plt.show() 
      
#button0.on_clicked(clck0)
#button1.on_clicked(clck1)
#button2.on_clicked(clck2)
###.........................###

#plt.show()  



