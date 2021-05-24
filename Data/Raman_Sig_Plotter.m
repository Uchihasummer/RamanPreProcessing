% Nic Theobald
% Raman Signal Plotter

load Maltol_Data_12-29-2020
filename = 'figure';

selectedfiles = ["ProvidedMaltol","WDark50006T1","WDark50006T2","WDark50006T3","WODark50006T1","WODark50006T2","WODark50006T3"];

% for file = selectedfiles
%     disp(file)
% %     i=1;
% %     while i<length(file)
% %         Adjustedfile(i,1) = (10^7/785 - 10^7/(ProvidedMaltol(i,1)))';
% %         Adjustedfile(i,2) = ProvidedMaltol(i,2);
% %         i = i+1;
% %     end 
% end


figure(1);
hold on



plot(ProvidedMaltol(:,1), ProvidedMaltol(:,2))

xticks(0:2821/10:2821)

xlabel('Wavelength (nm)');
ylabel('Counts');
% legend('T1', 'T2', 'T3', 'T4')

act_filename = strcat(filename, '.svg');
saveas(gcf, act_filename)