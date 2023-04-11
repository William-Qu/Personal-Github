% Simulates N trials of rolling 3 dice. Stores the results from each individual trial
% in the vectors x_1, x_2, x_3 for each die and in y for their sum. The number of occurences
% of each sum and plotted to a graph. The number of occurrences of each sum
% on each die was also plotted.

% Number of times rolling the three dices
N = 1000000;

% Initializing the array x with possible values in the set
x = [1, 2, 3, 4, 5, 6];

% Constructing the probabiility mass function of a fair dice. P[x=k] = 1/[omega]
pmf_x = (1 / length(x)) * ones(1, length(x));

% Complete N rolls of the dice for each dice
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
axa = gca;
axa.XLabel.String = 'Sum of Die Values from Three Die';
axa.XLim = [0, 20];
axa.YLabel.String = 'Count';
axa.YLim = [0, max(H) + 2];

% Count the number of times each sum occurs for each die
H_vec_1 = zeros(1, length(x));
H_vec_2 = zeros(1, length(x));
H_vec_3 = zeros(1, length(x));
for n=1:N
        H_vec_1(x_1(n)) = H_vec_1(x_1(n)) + 1;
        H_vec_2(x_2(n)) = H_vec_2(x_2(n)) + 1;
        H_vec_3(x_3(n)) = H_vec_3(x_3(n)) + 1;
end

% Plot the number of occurrences for each die
fig_b = figure('Name', 'Number of Roll Occurrences');
stem(x, H_vec_1, 'Color', 'r', 'LineWidth', 1.5);
hold on
stem(x, H_vec_2, 'b', 'LineWidth', 1.5);
stem(x, H_vec_3, 'k', 'LineWidth', 1.5);
title('Number of Sum Occurences for Three Die Rolls');
legend('Die 1', 'Die 2', 'Die 3', 'Location', 'southeast');
set(gca, 'FontSize', 14);
axb = gca;
axb.XLabel.String = 'Die Values from Three Die';
axb.XLim = [0, 7];
axb.YLabel.String = 'Count';
axb.YLim = [0, max([H_vec_1 H_vec_2 H_vec_3]) + 20000];
