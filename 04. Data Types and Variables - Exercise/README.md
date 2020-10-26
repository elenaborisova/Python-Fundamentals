## **01. Integer Operations**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/01_integers_operations.py)
Read four integer numbers. Add first to the second, divide (integer) the sum by the third number and multiply the result by the fourth number. Print the result.


## **02. Chars to String**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/02_chars_to_string.py)
Write a program that receives 3 characters. Combine all the characters into one string and print it on the console.


## **03. Elevator**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/03_elevator.py)
Calculate how many courses will be needed to elevate n persons by using an elevator of capacity of p persons. The input holds two lines: the number of people n and the capacity p of the elevator.


## **04. Sum of Chars**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/04_sum_of_chars.py)
Write a program, which sums the ASCII codes of n characters and prints the sum on the console.  
*Input*    
•	On the first line, you will receive n – the number of lines, which will follow  
•	On the next n lines – you will receive letters from the Latin alphabet  
*Output*  
Print the total sum in the following format:  
The sum equals: {total_sum}  
**Constraints**    
•	n will be in the interval [1…20].  
•	The characters will always be either upper or lower-case letters from the English alphabet  
•	You will always receive one letter per line  


## **05. Print Part of the ASCII Table**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/05_print_part_of_the_ascii_table.py)
Find online more information about ASCII (American Standard Code for Information Interchange) and write a program that prints part of the ASCII table of characters on the console.  On the first line of input you will receive the char index you should start with and on the second line - the index of the last character you should print.


## 06. Triples of Latin Letters**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/06_triples_of_latin_letters.py)
Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:


## **07. Water Overflow**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/07_water_overflow.py)
You have a water tank with capacity of 255 liters. On the next n lines, you will receive liters of water, which you have to pour in your tank. If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.  
*Input*  
The input will be on two lines:  
•	On the first line, you will receive n – the number of lines, which will follow    
•	On the next n lines – you receive quantities of water, which you have to pour in the tank  
*Output*  
Every time you do not have enough capacity in the tank to pour the given liters, print:  
Insufficient capacity!  
On the last line, print only the liters in the tank.  
*Constraints*  
•	n will be in the interval [1…20]  
•	liters will be in the interval [1…1000]  


## **08. * Party Profit**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/08_party_profit.py)
As a young adventurer, you travel with your party around the world, seeking for gold and glory. But you need to split the profit among your companions.  
You will receive a party size. After that you receive the days of the adventure.   
Every day, you are earning 50 coins, but you also spent 2 coin per companion for food.   
Every 3rd (third) day, you have a motivational party, spending 3 coins per companion for drinking water.   
Every 5th (fifth) day you slay a boss monster and you gain 20 coins per companion. But if you have a motivational party the same day, you spent additional 2 coins per companion.   
Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.  
You have to calculate how much coins gets each companion at the end of the adventure.  
*Input / Constraints*  
The input will consist of exactly 2 lines:  
•	party size – integer in range [1…100]  
•	days – integer in range [1…100]  
*Output*  
Print the following message: "{companions_count} companions received {coins} coins each."  
You cannot split a coin, so take the integral part (round down the coins to integer number)  


## **09. * Snowballs**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/09_snowballs.py)
Tony and Andi love playing in the snow and having snowball fights, but they always argue which makes the best snowballs. They have decided to involve you in their fray, by making you write a program, which calculates snowball data, and outputs the best snowball value.
You will receive N – an integer, the number of snowballs being made by Tony and Andi.  
For each snowball you will receive 3 input lines:  
•	On the first line you will get the snowballSnow – an integer.  
•	On the second line you will get the snowballTime – an integer.  
•	On the third line you will get the snowballQuality – an integer.  
For each snowball you must calculate its snowballValue by the following formula:  
(snowballSnow / snowballTime) ^ snowballQuality  
At the end you must print the highest calculated snowballValue.  
*Input*  
•	On the first input line you will receive N – the number of snowballs.  
•	On the next N * 3 input lines you will be receiving data about snowballs.   
*Output* 
•	As output you must print the highest calculated snowballValue, by the formula, specified above.  
•	The output format is:   
{snowballSnow} : {snowballTime} = {snowballValue} ({snowballQuality})  
*Constraints*  
•	The number of snowballs (N) will be an integer in range [0, 100].  
•	The snowballSnow is an integer in range [0, 1000].  
•	The snowballTime is an integer in range [1, 500].  
•	The snowballQuality is an integer in range [0, 100].  
•	Allowed working time / memory: 100ms / 16MB.


## **10. * Gladiator Expenses**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/10_gladiator_expenses.py)
As a gladiator, Petar has to repair his broken equipment when he loses a fight. His equipment consists of helmet, sword, shield and armor. You will receive the Petar's lost fights count.   
Every second lost game, his helmet is broken.  
Every third lost game, his sword is broken.  
When both his sword and helmet are broken in the same lost fight, his shield also brakes.  
Every second time, when his shield brakes, his armor also needs to be repaired.   
You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.  
*Input / Constraints*    
You will receive 5 parameters to your function:  
•	First parameter – lost fights count – integer in the range [0, 1000].  
•	Second parameter – helmet price - floating point number in range [0, 1000].   
•	Third parameter – sword price - floating point number in range [0, 1000].   
•	Fourth parameter – shield price - floating point number in range [0, 1000].  
•	Fifth parameter – armor price - floating point number in range [0, 1000].  
*Output*  
•	As output you must print Petar's total expenses for new equipment: "Gladiator expenses: {expenses} aureus"  
•	Allowed working time / memory: 100ms / 16MB.  


## **01. More Exercises - Biggest of 3 Numbers**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/more_exercises_01_biggest_of_3_numbers.py)
Write a program that finds the biggest of 3 numbers.  
The input comes as 3 integers.  
The output is the biggest from the input numbers.  


## **02. More Exercises - Exchange Integers**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/more_exercises_02_exchange_integers.py)
Read two integer numbers and after that exchange their values by using some programming logic. Print the variable values before and after the exchange.


## **03. More Exercises - Prime Number Checker** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/more_exercises_03_prime_number_checker.py)
Write a program to check if a number is prime (only wholly divisible by itself and one).  
The input comes as an integer number.  
The output should be true for prime number and false otherwise.


## **04. More Exercises - Decrypting Messages** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/more_exercises_04_decrypting_messages.py)
You will receive a key (integer) and n characters afterward. Add the key to each of the characters and append them to a message. At the end print the message, which you decrypted.   
*Input*  
•	On the first line, you will receive the key  
•	On the second line, you will receive n – the number of lines, which will follow    
•	On the next n lines – you will receive lower and uppercase characters from the Latin alphabet  
*Output*  
Print the decrypted message.  
*Constraints*  
•	The key will be in the interval [0…20]  
•	n will be in the interval [1…20]  
•	The characters will always be upper or lower-case letters from the English alphabet  
•	You will receive one letter per line  


## **05. More Exercises - Balanced Brackets**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/04.%20Data%20Types%20and%20Variables%20-%20Exercise/more_exercises_05_balanced_brackets.py)
You will receive n lines. On those lines, you will receive one of the following:  
•	Opening bracket – “(“,  
•	Closing bracket – “)” or  
•	Random string  
Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one. Nested parentheses are not valid, and if two consecutive opening brackets exist, the expression should be marked as unbalanced.   
*Input*  
•	On the first line, you will receive n – the number of lines, which will follow  
•	On the next n lines, you will receive “(”, “)” or another string  
*Output*  
You have to print “BALANCED”, if the parentheses are balanced and “UNBALANCED” otherwise.  
*Constraints*    
•	n will be in the interval [1…20]  
•	The length of the stings will be between [1…100] characters  

