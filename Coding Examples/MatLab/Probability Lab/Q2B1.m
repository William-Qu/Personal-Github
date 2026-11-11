% Question 2 Part 2
% Load Random Variables from Files
RV1 = load('RV1.mat').RV1;
RV2 = load('RV2.mat').RV2;
RV3 = load('RV3.mat').RV3;
RV = 0:100;

% Count the occurences for first values of random variables
H1 = zeros(1,101);
for i = 1:length(RV1)
    H1(RV1(i) + 1) = H1(RV1(i) + 1) + 1;  
end 

% Divide H1 by length of data set
H1 = H1/length(RV1);

% Plot the PDF of the first variable
fig_a = figure('Name', 'Random Variable 1');
stem(RV, H1, 'r');
title('PDF of RV1');
set(gca,'FontSize',12);
axis_a = gca;
axis_a.XLabel.String = 'Random Variable 1 Values';
axis_a.XLim = [0,100];
axis_a.YLabel.String = 'f_1(RV1)';

% Estimate the mean 
mean = sum(RV1)/length(RV1);

% Estimate the variance
variance = 0;
for i =1:length(RV1)
    variance = variance +(RV1(i) - mean)^2;
end
variance = variance / length(RV1);

% Compute the normal distribution with estimated mean
x = linespace(0,100,10000);
f_x = exp(-1.0 * (x-mean).*(x-mean)/(2.0*variance))/sqrt(2.0*pi*variance);

% Plot Normal Distribution
hold on;
plot(x,f_x,'k','LineWidth',2);
hold off;
