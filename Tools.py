import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog as fld
import os


savefig = 'Figures\\'
saveDFLoc = 'DataFrames\\'


def getLinks(Files=None):
    if Files:
        new = list(fld.askopenfilenames())
        for newfile in new:
            Files.append(newfile)
    else:
        Files = list(fld.askopenfilenames())

    return Files


def getData(links):
    # Establish Index
    frequency, intensity = np.loadtxt(links[0], skiprows=2, delimiter='  ', unpack=True)
    df = pd.DataFrame(index=frequency)

    # Loop through files and fill in DataFrame
    labels = []
    i = 0
    for link in links:
        frequency, intensity = np.loadtxt(link, skiprows=2, delimiter='  ', unpack=True)
        labels.append(os.path.basename(links[i]).replace('.SSM', ''))
        df[labels[i]] = intensity
        i += 1
    return df, labels


def saveDF(Data, Name):
    filename = saveDFLoc + Name + '.csv'
    Data.to_csv(filename)


def averagePiecewise(Data, labels, Col_Name='Piecewise'):
    averages = []
    for row in range(len(Data.index)):
        averages.append(np.average(Data[labels].iloc[row]))
    Data[Col_Name] = averages
    return Data


def averageSpectrum(Data, Columns):
    for Column in Columns:
        Data[Column + ' Averaged'] = np.average(Data[Column])
    return Data


def subtractPiecewise(Data, Columns, Col_Name='Subtract'):
    subtractions = []
    for row in range(len(Data.index)):
        subtractions.append(np.subtract(Data[Columns[0]].iloc[row], Data[Columns[1]].iloc[row]))
    Data[Col_Name] = subtractions
    return Data


def plot(Data, Columns, title='Title', fig=1, cushion=0.05, Loc=savefig, legMax = 10):
    plt.figure(fig, figsize=[12.8, 4.8], dpi=100, tight_layout=True, frameon=False)
    plt.plot(Data.index, Data[Columns], linewidth=0.5)

    xlim = [min(Data.index), max(Data.index)]

    try:
        ymax = max(Data[Columns].max())
        ymin = min(Data[Columns].min())
    except:
        ymax = Data[Columns].max()
        ymin = Data[Columns].min()

    spacing = (ymax - ymin) * cushion
    ylim = [ymin - spacing, ymax + spacing]

    plt.xlim(xlim)
    plt.ylim(ylim)

    font, small, large, ticks, legend = ['Arial', 14, 16, 8, 12]
    plt.title(title, fontname=font, fontsize=small)
    plt.xlabel('Frequency', fontname=font, fontsize=small)
    plt.ylabel('Counts', fontname=font, fontsize=small)
    plt.xticks(fontname=font, fontsize=ticks)
    plt.yticks(fontname=font, fontsize=ticks)

    if len(Columns) > legMax:
        Columns = []

    font = {'size': 10}
    mpl.rc('font', **font)
    leg = plt.legend(Columns, prop={'family': 'Arial'})

    plt.savefig(fname=Loc + title + '.png')


def subplot(fig):
    pass
