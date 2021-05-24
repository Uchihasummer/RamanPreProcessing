from Tools import *

# Average Spectrums
links = ['C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 1.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 2.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 3.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 4.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 5.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 6.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 7.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 8.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 9.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 10.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 11.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 12.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 13.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 14.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 15.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 16.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 17.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 18.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 19.SSM',
         'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 20.SSM']

Spectrums, Labels = getData(links)

Spectrums = averagePiecewise(Spectrums, Labels)
plot(Spectrums, Labels, 'All Maltol', 1)

plot(Spectrums, Spectrums.columns[20], 'Average Spectrums', 2)
