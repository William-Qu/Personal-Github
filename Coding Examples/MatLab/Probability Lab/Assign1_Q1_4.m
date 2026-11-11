%Q1 Part 4 

% Number of times rolling the three dices
N = 100;

% Initializing the array x with possible values in the set
x = [1, 2, 3, 4, 5, 6];

% Constructing the probabiility mass function of a fair dice. P[x=k] = 1/[omega]
pmf_x = (1/length(x)) * ones(1, length(x));

% Complete 100 (N) rolls of the dice for each dice
x_1 = rand_gen(x, pmf_x, N);
x_2 = rand_gen(x, pmf_x, N);
x_3 = rand_gen(x, pmf_x, N);

%Sum the number of times each value occurs in dice 1,2, and 3 
H1 = zeros(1, length(x));
H2 = zeros(1, length(x));
H3 = zeros(1, length(x)); 

for i = 1:N
    H1(x_1(i)) = H1(x_1(i)) + 1;
    H2(x_2(i)) = H2(x_2(i)) + 1;
    H3(x_3(i)) = H3(x_3(i)) + 1;
end 

%plotting the sums of various value occurences
stem(x, H1, 'Color', 'b', 'LineWidth', 1.5);
hold on
stem(x, H2, 'r', 'LineWidth', 1.5);
stem(x, H3, 'k', 'LineWidth', 1.5);
hold off
title('Dice Value Occurences', 'FontWeight', 'normal');
legend('Die 1','Die 2','Die 3','Location', 'southwest');
set(gca,'FontSize', 12);
ax = gca;
ax.XLabel.String = 'Die Values';
ax.XLim = [0,7];
ax.YLabel.String = 'Occurences';
ax.YLim = [0, max([H1 H2 H3]) + 2];

