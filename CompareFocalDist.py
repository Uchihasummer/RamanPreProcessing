from Tools import *

# Average Spectrums
links = getLinks()
Spectrums, Labels = getData(links)

plot(Spectrums, Labels, 'Maltol Spectrums', 1)

