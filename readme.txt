Readme

Welcome to Meta Raffle Club code files.

In this folder you can find total of 5 files including this readme file for your perusal.

The file general_generator is for generating the general pool 50 weekly winners of our MRC weekly raffle.
Inside you can find multiple functions, mainly these functions are for the UI of the application but if you are here to review the transparency of our code, please focus at the function rand_gen() where the random number is generated.

The file general_winner_list.csv is a csv file to store all the weekly winners so that the number does not repeats itself the next week

The file winner_generator is essentially the same file as general_generator. This file is used to generate the winners pool 3 monthly winners. The difference include the UI coding and reading from both general_winner_list.csv and winners_winners_list.csv in the function rand_gen()

The file winners_winners_list.csv is a csv file to store all the monthly winners so that number does not repeats itself the next month.	

