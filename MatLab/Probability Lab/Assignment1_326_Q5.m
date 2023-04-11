% Simulates N trials of rolling 3 dice. Stores the results from each individual trial
% in the vectors x_1, x_2, x_3 for each die and in y for their sum. The number of occurences
% of each sum and plotted to a graph.

% Number of times rolling the three dices
N = 100;

% Initializing the array x with possible values in the set
x = [1, 2, 3, 4, 5, 6];

% Constructing the probabiility mass function of a fair dice. P[x=k] = 1/[omega]
pmf_x = (1 / length(x)) * ones(1, length(x));

% Complete 100 (N) rolls of the dice for each dice
x_1 = rand_gen(x, pmf_x, N);
x_2 = rand_gen(x, pmf_x, N);
x_3 = rand_gen(x, pmf_x, N);

% Construct y as an array of sums of all three dice values for each trial
y = x_1 + x_2 + x_3;

% Count the number of times each sum occurs
H = zeros(1, 18);
for n=1:N
        H(y(n)) = H(y(n)) + 1;
end

% Plot the number of occurrences of each sum
fig_a = figure('Name', 'Number of Occurences');
stem(1:18, H, 'Color', 'b', 'LineWidth', 1.75);
title('Number of Sum Occurences for Three Die');
set(gca, 'FontSize', 14);
axi = gca;
axi.XLabel.String = 'Sum of Die Values from Three Die';
axi.XLim = [0, 20];
axi.YLabel.String = 'Count';
axi.YLim = [0, max(H) + 2];
