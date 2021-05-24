from Tools import *

# # Subtract two spectrums
# Spectrum1 = ['D:/OneDrive - Fort Lewis College/Research_CourseWork_Li/Raman Research Project/Data/5-20-21/Maltol 1.SSM']
# Spectrum2 = ['D:/OneDrive - Fort Lewis College/Research_CourseWork_Li/Raman Research Project/Data/5-20-21/Maltol 2.SSM']
# Noise = [
#     'D:/OneDrive - Fort Lewis College/Research_CourseWork_Li/Raman Research Project/Data/5-19-21/DarkSpectrum1.SSM']
#
# SpecDiff, Labels2 = tls.getData(Spectrum1 + Spectrum2 + Noise)
# tls.plot(SpecDiff, Labels2, 'Spectrums and Background', fig=1)
#
# SpecDiff = tls.subtractPiecewise(SpecDiff, Labels2[0:2], 'Spec Diff')
# tls.plot(SpecDiff, SpecDiff.columns[[0, 1, 3]], 'Difference Between Spectrums', fig=2)
#
# tls.plot(SpecDiff, SpecDiff.columns[[2, 3]], 'Difference Between Spectrums vs Noise', fig=3)

# # Average Spectrums
# links = tls.getLinks()
#
# Spectrums, Labels = tls.getData(links)
#
# Spectrums = tls.averagePiecewise(Spectrums, Labels)
# tls.plot(Spectrums, Labels, 'All Maltol', 1)
#
# tls.plot(Spectrums, Spectrums.columns[[1, 11]], 'Average Spectrums', 2)

# links = getLinks()

# # Average Vial Spectrums
# links = ['C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 1.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 2.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 3.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 4.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 5.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 6.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 7.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 8.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 9.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 10.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 11.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 12.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 13.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 14.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 15.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 16.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 17.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 18.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 19.SSM',
#          'C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Vial 20.SSM']
#
# Spectrums, Labels = getData(links)
# Spectrums = averagePiecewise(Spectrums, Labels)
#
# # plot(Spectrums, ['Piecewise'], 'Average Vial Spectrums', 1) # Average
# # plot(Spectrums, Labels, 'Vial Spectrums', 2) # All Spectrums
# # saveDF(Spectrums, 'Raman Vial')
#
#
# links = ['C:/Users/nstheobald.FORTLEWIS.008/Desktop/Raman_Spec/Data/5-21-21/Maltol 1.SSM']
# Maltol, Labels = getData(links)
# Maltol['Raman Vial'] = Spectrums['Piecewise'] + 709.7030
#
# plot(Maltol, Maltol.columns, title = 'Average Vial vs Average Maltol', fig = 3)
#
# Maltol = subtractPiecewise(Maltol,Maltol.columns, 'Maltol - Vial')
#
# plot(Maltol, Maltol.columns, title = 'Vial Spectrum Subtracted from Maltol', fig = 4)


links = getLinks()