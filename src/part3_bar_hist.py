'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''


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

def barplot_for_fta(pred_universe):
   '''
   Creates a bar plot out of the pred_universe dataframe for the 'fta' column.
  
   Parameter: 
       pred_universe (DF)
      
   Returns:
       Bar plot saved as a PNG file
   '''
   sns.barplot(data=pred_universe, 
               x='fta')
   plt.savefig('./data/part3_plots/barplot_for_fta.png', bbox_inches='tight')


# 2. Hue the previous barplot by sex
def barplot_for_fta_by_sex(pred_universe):
   '''
   Creates a bar plot out of the pred_universe dataframe for the 'fta' column and includes a hue for sex.
  
   Parameter: 
       pred_universe (DF)
      
   Returns:
       Bar plot of the FTA column with a hue by sex, saved as a PNG file
  
   '''
   sns.barplot(data=pred_universe,
               x='fta', hue='sex')
   plt.savefig('./data/part3_plots/barplot_fta_by_sex.png', bbox_inches='tight')

# 3. Plot a histogram of age_at_arrest
def histogram_age_at_arrest(pred_universe):
   '''
   Creates a histogram of the age_at_arrest.
  
   Parameter: 
       pred_universe (DF)
      
   Returns:
       Histogram of age_at_arrest, saved as a PNG file
  
   '''
   sns.histplot(data=pred_universe, 
                x='age_at_arrest')
   plt.savefig('./data/part3_plots/histogram_age_at_arrest.png', bbox_inches='tight')


    # 4. Plot the same histogram, but create bins that represent the following age groups
    #  - 18 to 21
    #  - 21 to 30
    #  - 30 to 40
    #  - 40 to 100
def histogram_age_group_bins(pred_universe):
   '''
   Creates a histogram of age_at_arrest with the bins that represent the age groups.
  
   Parameter:
       pred_universe (DF)
      
   Returns:
       Histogram of age_at_arrest with the bins.
   '''
   bins = [18, 21, 30, 40, 100]
   sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)
   plt.savefig('./data/part3_plots/histogram_age_groups.png', bbox_inches='tight')
   
  