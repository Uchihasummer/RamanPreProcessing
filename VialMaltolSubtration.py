from Tools import *

# Average Spectrums
Viallinks = getLinks()
Maltollinks = getLinks()

Vial, VialLabels = getData(Viallinks)
Maltol, MaltolLabels = getData(Maltollinks)

Vial = averagePiecewise(Vial, VialLabels, 'Average')
Maltol = averagePiecewise(Maltol, MaltolLabels, 'Average')

df = pd.DataFrame()
df['Average Maltol Spectrum'] = Maltol['Average']
df['Average Vial Spectrum'] = Vial['Average']

plot(df, df.columns, 'Title', fig=1)

df = subtractPiecewise(df, df.columns, 'Subtract')
plot(df, df.columns, 'Title', fig=2, legendEntries=df.columns)
