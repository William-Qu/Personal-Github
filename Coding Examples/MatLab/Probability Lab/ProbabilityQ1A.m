%Declare the possible values of x
x = [1, 2, 3, 4, 5, 6];

%Declare the probability mass function of x and assign it
pmf_x = (1 / length(x)) * ones(length(x));

%Sum the different outcomes of the 3 dice rolls into the array y
y = 0;
for i = 1:length(x)
    for j = 1:length(x)
        for k = 1: length(x)
            die_sum = x(i) + x(j) + x(k);
            y = [y die_sum];
        end
    end
end

%Sort the array of y for graphing purposes
y = y(y > 0);
y = sort(y);

%Remove all duplicate items in array y and count the number of duplicates
[y, ~, count] = unique(y);
count = accumarray(count, 1);

%Make the probability mass function of y so that its ready to graph
pmf_y = zeros(1, length(y));
for i = 1:length(y)
    pmf_y(i) = count(i) / sum(count);
end

%Generate the PMF graph of x with MATLAB graphing tools
fig1 = figure('Name', 'PMF of x');
fig1.Units = 'centimeters';
stem(x, pmf_x, 'b', 'LineWidth', 1.5);
title('Probability Mass Function of x', 'FontWeight', 'normal');
set(gca, 'FontSize', 12);
ax1 = gca;
ax1.XLabel.String = 'Possible Values of x';
ax1.XLim = [0, 7];
ax1.YLabel.String = 'Probability (decimal)';

%Generate the PMF graph of y with MATLAB graphing tools
fig2 = figure('Name', 'PMF of y');
fig2.Units = 'centimeters';
stem(y, pmf_y, 'r', 'LineWidth', 1.5);
title('Probability Mass Function of y', 'FontWeight', 'normal');
set(gca, 'FontSize', 12);
ax2 = gca;
ax2.XLabel.String = 'Possible Values of y';
ax2.YLabel.String = 'Probability (decimal)';




