'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?


# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.


# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?

import seaborn as sns
import matplotlib.pyplot as plt
import os 

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def seaborn_settings():
    '''
    Applies the default seaborn theme and sets the default figure size
    '''
    sns.set_theme()
    sns.set(rc={'figure.figsize':(6, 4)})

def create_directories(directories):
    """
    Creates the necessary directories for storing plots and data.
    """
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        
def scatter_nonf_vs_f(felony_charge):
    '''
    Creates a scatter plot for predictions of felony and non felony and a hue that depicts of the current charge is a felony.
    
    Parameter: 
        new_df (DF)

    '''
    sns.lmplot(data=felony_charge, 
                    x='prediction_felony', 
                    y='prediction_nonfelony', 
                    hue='has_charge_felony')  
    plt.savefig('./data/part5_plots/scatter1.png', bbox_inches='tight')
      
    
def scatter_actually_rearrested(felony_charge):
    '''
    Creates a scatterplot that shows the prediction felony and if someone was actually rearrested. 
    
    Parameter: 
        new_df (DF)
        
    Returns: 
        Scatterplot with a regression line.
    '''
    sns.lmplot(data=felony_charge,
               x='prediction_felony', 
               y='has_felony_charge', 
               fit_reg=True)
    plt.savefig('./data/part5_plots/scatter2.png', bbox_inches='tight')


