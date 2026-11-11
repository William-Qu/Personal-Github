x = [1,2,3,4,5,6]; 

pmf_x = (1/length(x))*ones(length(x));	% Initialize x as an array

% Build the CDF of x by summing the PMF
cdf_x = zeros(1,length(x));
for i = 1:length(x);
	cdf_x(i) = sum(pmf_x(1:i));
end

y = 0;	% Build CDF of x by summing the PMF
for i=1:length(x)
	for j = 1:length(x)
		for k = 1:length(x)
			die_sum = x(i)+x(j)+x(k);
			y = [y die_sum];
		end
	end
end
y = y(y > 0);
y = sort(y);	% Sort sums within array 1

% Remove duplicate sums from y 

[y, ~, count] = unique(y);
count = accumarray(count,1).';

% Build PMF of y 
pmf_y = zeros(1,length(y));
for i = 1:length(y);
	pmf_y(i) = count(i)/sum(count);
end

% Build the CDF of y by summing the PMF
cdf_y = zeros(1,length(y));
for i = 1:length(y)
	cdf_y(i) = sum(pmf_y(1:i));
end 

% Plot CDF of x 
fig_a = figure('Name','CDF of x');
fig_a.Units = 'Centimeters';
stairs([0 x 7],[0 cdf_x 1],'b', 'LineWidth', 1.7);
title('CDF of x');
set(gca,'FontSize',12);
axis_a = gca;
axis_a.XLabel.String = 'x';
axis_a.XLim = [0,7];
axis_a.YLabel.String = 'F_{x}(x)';

% Plot CDF of y 
fig_b = figure('Name','CDF of y');
fig_b.Units = 'Centimeters';
stairs([0 y 20],[0 cdf_y 1],'r', 'LineWidth', 1.7);
title('CDF of y');
set(gca,'FontSize',12);
axis_b = gca;
axis_b.XLabel.String = 'y';
axis_b.XLim = [0,20];
axis_b.YLabel.String = 'F_{y}(y)';