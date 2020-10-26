## **01. Jenny's Secret Message**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/01_jennys_secret_message.py)
Jenny studies programming with python and wants to create a program that greets a user when he/she gives his/her name. Jenny however is in love with Johnny, and would like to greet him differently. Can you help her?


## **02. Drink Something**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/02_drink_something.py)
Kids drink toddy, Teens drink coke, Young adults drink beer, Adults drink whisky.  
Make a program that receives an age, and returns what they drink.  
Rules:  
Kids under 14 years old.  
Teens under 18 years old.  
Young adults under 21 years old.  
Adults above 21.  
Note: All the values except the last one are inclusive!  


## **03. Leonardo DiCaprio Oscars**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/03_leonardo_dicaprio_oscars.py)
Write a program that receives a single integer number and prints different messages depending on the number:  
-	If Oscar is 88 - "Leo finally won the Oscar! Leo is happy".  
-	If Oscar is 86 - "Not even for Wolf of Wall Street?!"  
-	If Oscar is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?"  
-	If Oscar is over 88 - "Leo got one already!"  


## **04. Double Char**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/04_double_char.py)
Given a string, you have to print a string in which each character (case-sensitive) is repeated.


## **05. Can't Sleep? Count Sheep**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/05_cant_sleep_count_sheep.py)
If you can't sleep, just count sheep! Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep..."   
Input will always be valid, i.e. no negative integers.


## **06. Next Happy Year**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/06_happy_next_year.py)
You're saying good-bye your best friend, "See you next happy year". Happy Year is the year with only distinct digits, (e.g) 2018.   
Write a program that receives an integer number and finds the next happy year.


## **07. Maximum Multiple**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/07_maximum_multiple.py)
Given a Divisor and a Bound, find the largest integer N, such that:  
N is divisible by divisor  
N is less than or equal to bound  
N is greater than 0.  
*Notes:* The divisor and bound are only positive values. It's guaranteed that a divisor is found


## **08. * Mutate Strings**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/08_mutate_strings.py)
You will be given two strings. Transform the first string into the second one, one letter at a time and print it. Print only the unique strings  
*Note:* the strings will have the same lengths


## **09. * Easter Cozonacs**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/09_easter_cozunacs.py)
Since it’s Easter you have decided to make some cozonacs and exchange them for eggs.  
Create a program that calculates how much cozonacs you can make with the budget you have. First, you will receive your budget. Then, you will receive the price for 1 kg flour.   Here is the recipe for one cozonac:   
Eggs - 1 pack, Flour - 1kg, Milk - 0.250l  
The price for 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1l milk is 25% more than price for 1 kg flour. Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.  
Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:  
•	For every cozonac that you make, you will receive 3 colored eggs. 
•	For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received the usual 3 colored eggs for your cozonac. The count of eggs you will lose is calculated when you subtract 2 from your current count of cozonacs – ({currentCozonacsCount} – 2)  
In the end, print the cozonacs you made, the eggs you have gathered and the money you have left, formatted to the 2nd decimal place, in the following format:  
"You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."  
*Input / Constraints*  
•	On the 1st line you will receive the budget – a real number in the range [0.0…100000.0]  
•	On the 2nd line you will receive the price for 1 kg flour – a real number in the range [0.0…100000.0]  
•	The input will always be in the right format.   
•	You will always have a remaining budget.  
•	There will not be a case in which the eggs become a negative count.  
*Output*  
•	In the end print the count of cozonacs you have made, the colored eggs you have gathered and the money formatted to the 2nd decimal place in the format described above.


## **10. * Christmas Spirit** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/10_christmas_spirit.py)
It's time to get in a Christmas mood. You have to decorate the house in time for the big event, but you have limited days to do so.  
You will receive allowed quantity for one type of decoration and days left until Christmas day to decorate the house.  
There are 4 types of decorations and each piece costs a price  
•	Ornament Set – 2$ a piece  
•	Tree Skirt – 5$ a piece  
•	Tree Garlands – 3$ a piece  
•	Tree Lights – 15$ a piece  
Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.  
Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.  
Every fifth day you buy Tree Lights quantity of times and increase your Christmas spirit by 17. If you have bought Tree Skirts and Tree Garlands at the same day you additionally increase your spirit by 30.  
Every tenth day you lose 20 spirit, because your cat ruins all tree decorations and you have to rebuild the tree and buy one piece of tree skirt, garlands and lights. That is why you are forced to increase the allowed quantity with 2 at the beginning of every eleventh day.  
Also if the last day is a tenth day the cat decides to demolish even more and ruins the Christmas turkey and you lose additional 30 spirit.  
At the end you must print the total cost and the gained spirit.  
*Input / Constraints*  
The input will consist of exactly 2 lines:  
•	quantity – integer in range [1…100]  
•	days – integer in range [1…100]  
*Output*  
At the end print the total cost and the total gained spirit in the following format:  
•	"Total cost: {budget}"  
•	"Total spirit: {totalSpirit}"  


## **01. More Exercises - Find the Largest**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/more_ex_01_find_the_largest.py)
Given a number, print the largest number that can be formed from the digits of the number given.


## **02. More Exercises -	Find the Capitals**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax,%20Conditional%20Statements%20and%20Loops%20-%20Exercise/more_ex_02_find_the_capitals.py)
Write a program that takes a single string and prints a list of all the indices of all the capital letters


## **03. More Exercises	- Wolf in Sheep's Clothing**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax,%20Conditional%20Statements%20and%20Loops%20-%20Exercise/more_ex_03_wolf_in_sheeps_clothing.py)
Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.  
Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array: 
[sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)  
   4      3            2      1  
If the wolf is the closest animal to you, print "Please go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.  
*Note:* there will always be exactly one wolf in the array.  
*Input*  
The input will be a single string containing the animals separated by comma and a single space ", "  


## **04. More Exercies - Sum of a Beach**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/more_ex_04_sum_of_a_beach.py)
Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (regardless of the case).


## **05. More Exercises - How Much Coffee Do You Need?**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/02.%20Basic%20Syntax%2C%20Conditional%20Statements%20and%20Loops%20-%20Exercise/more_ex_05_how_much_coffee_do_you_need.py)
Everybody know that you passed to much time awake during night time...  
Your task here is to define how much coffee you need to stay awake after your night. Until you receive the command "END", you need to read a single command, according to this command you will print the number of coffee you need to stay awake during day time.   
Note: If the count exceed 5 please return 'You need extra sleep'.  
The list of events can contain the following:    
•	You have homework to do ('coding').  
•	You have a dog or a cat that just decide to wake up too early ('dog' or 'cat').  
•	You just watch a movie ('movie').  
•	Other events can be present and it will be represent by arbitrary string, just ignore this one.  
Each event can be lowercase, or uppercase. If it is lowercase you need 1 coffee by events and if it is uppercase you need 2 coffees.


