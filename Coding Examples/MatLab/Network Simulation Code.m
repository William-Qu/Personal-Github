%Set the values of Lamda (L) and Mu (M)
L = [0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745];
M = 0.75;
queueDelay = zeros(9, 1000000);

for i=1:1:length(L)
    %Calculate the probability of incrementing/decrementing the queue
    pForward = L(i) * (1 - M); %0.05
    pBackwards = M * (1 - L(i)); %0.6
    
    %Reset Variables
    queueLength = 0;
    randomNum = 0;
    queueDelayTemp = 0;

    %Run iterations for current Lamda
    for j=1:1:1000001
        %Use Littles Law to calculate the queue delay
        queueDelayTemp = queueLength / L(i);
        queueDelay(i, j) = queueDelayTemp;

        %Check the current queue length
        randomNum = rand;
        if (randomNum <= pForward)
            queueLength = queueLength + 1;
        elseif (randomNum > pForward && randomNum <= pBackwards && queueLength > 0)
            queueLength = queueLength - 1;
        end
    end
end

%Print the total queue delay
plot(1:1000000, queueDelay(1, 1:1000000), ...
     1:1000000, queueDelay(2, 1:1000000), ...
     1:1000000, queueDelay(3, 1:1000000), ...
     1:1000000, queueDelay(4, 1:1000000), ...
     1:1000000, queueDelay(5, 1:1000000), ...
     1:1000000, queueDelay(6, 1:1000000), ...
     1:1000000, queueDelay(7, 1:1000000), ...
     1:1000000, queueDelay(8, 1:1000000), ...
     1:1000000, queueDelay(9, 1:1000000));
