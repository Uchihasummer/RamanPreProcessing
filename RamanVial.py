from Tools import *

# Average Spectrums
links = getLinks()

Spectrums, Labels = getData(links)

Spectrums = averagePiecewise(Spectrums, Labels)
plot(Spectrums, Labels, 'Maltol Spectrums Monday', 1)

plot(Spectrums, Spectrums.columns[5], 'Average Maltol Spectrum Monday', fig = 2, legendEntries='Average')
