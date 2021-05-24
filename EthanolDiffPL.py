from Tools import *

# Average Spectrums
links = getLinks()

Spectrums, Labels = getData(links)

plot(Spectrums, Labels, 'Raman Vials Different Integration Time', 1, legendEntries=['3','5','7'])

# plot(Spectrums, Spectrums.columns[5], 'Average Maltol Spectrum Monday', fig = 2, legendEntries='Average')
