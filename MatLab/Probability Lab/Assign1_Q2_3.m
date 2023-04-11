%Q3 Part 3
% Load Random Variables from Files
RV1 = load('RV1.mat').RV1;
RV2 = load('RV2.mat').RV2;
RV3 = load('RV3.mat').RV3;

% Count the occurences for first values of random variables
H1 = zeros(1,101);
for i = 1:length(RV1)
    H1(RV1(i) + 1) = H1(RV1(i) + 1) + 1;  
end 

% Divide H1 by length of data set
H1 = H1/length(RV1);

% Estimated probability that RV1 be between 10 and 40
p1 = sum(H1(11:41));

% Estimated mean of RV1
mean1 = sum(RV1) / length(RV1);

% Estimated variance of RV1 
variance1 = 0;
for i =1:length(RV1)
    variance1 = variance1 +(RV1(i) - mean1)^2;
end
variance1 = variance1 / length(RV1);

% Estimating Probability using normal distribution
f_x = @(x) exp(-1.0 * (x-mean1).*(x-mean1)/(2.0*variance1))/sqrt(2.0*pi*variance1);
p1_norm = integral(f_x, 10, 40);

%----------------------------------------------------

% Count the occurences for first values of random variables
H2 = zeros(1,101);
for i = 1:length(RV2)
    H2(RV2(i) + 1) = H2(RV2(i) + 1) + 1;  
end 

% Divide H2 by length of data set
H2 = H2/length(RV2);

% Estimated probability that RV1 be between 10 and 40
p2 = sum(H2(11:41));

% Estimated mean of RV2
mean2 = sum(RV2) / length(RV2);

% Estimated variance of RV2 
variance2 = 0;
for i =1:length(RV2)
    variance2 = variance2 +(RV2(i) - mean2)^2;
end
variance2 = variance2 / length(RV2);

% Estimating Probability using normal distribution
f_x = @(x) exp(-1.0 * (x-mean2).*(x-mean2)/(2.0*variance2))/sqrt(2.0*pi*variance2);
p2_norm = integral(f_x, 10, 40);

%----------------------------------------------------

% Count the occurences for first values of random variables
H3 = zeros(1,101);
for i = 1:length(RV3)
    H3(RV3(i) + 1) = H3(RV3(i) + 1) + 1;  
end 

% Divide H3 by length of data set
H3 = H3/length(RV3);

% Estimated probability that RV3 be between 10 and 40
p3 = sum(H3(11:41));

% Estimated mean of RV3
mean3 = sum(RV3) / length(RV3);

% Estimated variance of RV3 
variance3 = 0;
for i =1:length(RV3)
    variance3 = variance3 +(RV3(i) - mean3)^2;
end
variance3 = variance3 / length(RV3);

% Estimating Probability using normal distribution
f_x = @(x) exp(-1.0 * (x-mean3).*(x-mean3)/(2.0*variance3))/sqrt(2.0*pi*variance3);
p3_norm = integral(f_x, 10, 40);
