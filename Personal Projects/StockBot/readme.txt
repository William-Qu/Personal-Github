---ReadMe Description Oct 25, 2026---
This program was built to test a variety of different trading bots on the actual stock market for personal interest and experimentation.
Some of these bots use traditional trading strategies, some linear regression, some learning networks.
Since this has been built to be able to run many bots simultaneously, different bots may be added later.  Currently there are 9 models.
The program saves its trading predictions and the bot rankings over time so that these can be compared.
These files are saved in \Saved_Dictionaries\ and are saved with the current date
This program uses Alpacas UI to get its trading data and make the trades.
The main function to be run is BotManager.py which handles the running of each different model.
The program will be first run on Oct 26 2026, and is currently configured to be manually run every ~2 weeks.
Each time the program is run the models will make trades up to 75% of their current cash.
Sell functionality is determined by model, but generally is when the predicted returns are less than the current returns or loss > 2%.
If you have any questions, please feel free to reach out at 789william@hotmail.ca, and thank you for taking the time to read through my project

Thanks, William 
Oct 25, 2026



---Change Log Nov 03, 2026---
I have reconfigured the BotManager to be function based now (split into BotManagerFunctions and MainBotManager) to be more readable and usable
The functionality remains the same, just split into functions
One major difference of note is that the Trad functions have been moved into the loops now and Trad has been added to the models
Another is that all stock candles are downloaded and saved at the beginning of the program instead of individually as that ticker is predicted
Many small ease of use and QOL changes have been made for readability of the log
A new model has been added called LrgLSTM
This is an LSTM model that is trained over all stocks and times 
The model is similar to MultLSTM, however the actual model is larger due to the much larger data set it works with
Both LSTM models will now be saving their model weights now to allow for faster running of the program
The LrgLSTM has already been trained and model saved, however it will start when I run the full program again on the two week mark 
    ->(IT WILL BE TWO WEEKS BEHIND THE OTHER MODELS)
BotManager.py has been renamed to BotManager_Retired.py

Thanks, William
Nov 3, 2026


---Change Log Nov 09, 2026---
I have run the program for the second time and fixed a variety of issues that came up
These are the larger ones below:
    -Fixed an issue with selling stocks that was not caught due to dictionary referencing
    -Fixed an issue with saving failed requests due to the error handling in functions
    -Fixed Trad stocks accidentally being able to sell stock
    -Fixed saving of the rankings dictionary
    -Manually remade some BUY requests and removed SDNK due to no longer available
One thing to note is due to the delay between buying and selling stocks the models would only buy with the money before stocks were sold
In order to change this to use money from newly sold stocks, I have split the BUYSELL function into 2; a BUY and a SELL
This is to add enough delay for the SELL requests to be in effect
Due to this I have rerun the BUY requests for the models so that the cash was not so high

Thanks, William
Nov 9, 2026