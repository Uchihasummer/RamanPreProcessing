from Tools import *

# Average Spectrums
links = ['Data/5-21-21/Vial 1.SSM', 'Data/5-21-21/Vial 2.SSM', 'Data/5-21-21/Vial 3.SSM', 'Data/5-21-21/Vial 4.SSM',
         'Data/5-21-21/Vial 5.SSM', 'Data/5-21-21/Vial 6.SSM', 'Data/5-21-21/Vial 7.SSM', 'Data/5-21-21/Vial 8.SSM',
         'Data/5-21-21/Vial 9.SSM', 'Data/5-21-21/Vial 10.SSM', 'Data/5-21-21/Vial 11.SSM', 'Data/5-21-21/Vial 12.SSM',
         'Data/5-21-21/Vial 13.SSM', 'Data/5-21-21/Vial 14.SSM', 'Data/5-21-21/Vial 15.SSM', 'Data/5-21-21/Vial 16.SSM',
         'Data/5-21-21/Vial 17.SSM', 'Data/5-21-21/Vial 18.SSM', 'Data/5-21-21/Vial 19.SSM', 'Data/5-21-21/Vial 20.SSM']

Spectrums, Labels = getData(links)

Spectrums = averagePiecewise(Spectrums, Labels)
plot(Spectrums, Labels, 'All Maltol', 1)

plot(Spectrums, Spectrums.columns[20], 'Average Spectrums', 2)
