## **01. Invert Values** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/01_invert_values.py)
Write a program that receives a single string containing numbers separated by a single space. Print a list containing the opposite of each number


## **02. Multiples List**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/02_multiples_list.py)
Write a program that receives two numbers (factor and count) and creates a list with length of the given count and contains only elements that are multiples of the given factor


## **03.	Football Cards** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/03_football_cards.py)
Most football fans love it for the goals and excitement. Well, this problem doesn't. You are to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.  
The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11. Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining, the game is stopped immediately by the referee, and the team with less than 7 players loses.  

A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number. e.g. the card 'B-7' means player #7 from team B received a card. (index 6 of the list)  
The task: Given a list of cards (could be empty), return the number of remaining players on each team at the end of the game in the format: "Team A - {players_count}; Team B - {players_count}". If the game was terminated print an additional line: "Game was terminated"  
Note for the random tests: If a player that has already been sent off receives another card - ignore it.  
*Input*  
The input (the cards) will come on a single line separated by a single space  
*Output*  
Print the remaining players as described above and add another line (as shown above) if the game was terminated


## **04. Number Beggars** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/04_number_beggars.py)
Your task here is pretty simple: given a list of numbers and an amount of beggars, you are supposed to return a list with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.  
For example: [1,2,3,4,5] for 2 beggars will return a result of 9 and 6, as the first one takes [1,3,5], the second collects [2,4].  
The same list with 3 beggars would have in turn have produced a better outcome for the second beggar: 5, 7 and 3, as they will respectively take [1, 4], [2, 5] and [3].  
Also note that not all beggars have to take the same amount of "offers", meaning that the length of the list is not necessarily a multiple of n; length can be even shorter, in which case the last beggars will of course take nothing (0).  
*Input*  
You will receive 2 lines of input: a single string containing the numbers separated by a comma and a space ", ". On the second line you will receive the number of beggars  
*Output*  
Print a list of all the sums that each beggar made


## **05. Faro Shuffle**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/05_faro_shuffle.py)
A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards in the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original top card is still on top.  
For example, faro shuffling the list  
['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six' ]  
Write a program that receives a single string (cards separated by a space) and on the second line receives a number of faro shuffles that have to be made. Print the state of the deck after the shuffle  
*Note:* The length of the deck of cards will always be an even number  


## **06. Survival of the Biggest**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/06_survival_of_the_biggest.py)
Write a program that receives a list of integer numbers and a number n. The number n represents the amount of numbers to remove from the list. You should remove the smallest ones  
*Input*  
On the first line you will receive a string (numbers separated by a space), on the second line you will receive a number n (count of numbers to remove)  
*Output*  
Print all the numbers that are left in the list  


## **07. * Easter Gifts**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/07_easter_gifts.py)
As a good friend, you decide to buy presents for your friends.  
Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:  
"{gift1} {gift2} {gift3}… {giftn}"  
Then you will start receiving commands until you read the "No Money" message. There are three possible commands:  
•	"OutOfStock {gift}"  
o	Find the gifts with this name in your collection, if there are any, and change their values to "None".   
•	"Required {gift} {index}"  
o	Replace the value of the current gift on the given index with this gift, if the index is valid.  
•	"JustInCase {gift}"  
o	Replace the value of your last gift with this one.  
In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:  
"{gift1} {gift2} {gift3}… {giftn}"  
*Input / Constraints*  
•	On the 1st line you are going to receive the names of the gifts, separated by a single space.  
•	On the next lines, until the "No Money" command is received, you will be receiving commands.  
•	The input will always be valid.  
*Output*  
•	Print the gifts in the format described above.


## **08.* Seize the Fire**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/08_seize_the_fire.py)
The group of adventurists have gone on their first task. Now they have to walk through fire - literally. They have to use all of the water they have left. Your task is to help them survive.   
Create a program that calculates the water that is needed to put out a "fire cell", based on the given information about its "fire level" and how much it gets affected by water.   
First, you will be given the level of fire inside the cell with the integer value of the cell, which represents the needed water to put out the fire.  They will be given in the following format:  
"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"  
Afterwards you will receive the amount of water you have for putting out the fires. There is a range of fire for each of the fire types, and if a cell’s value is below or exceeds it, it is invalid and you don’t need to put it out.  
Type of Fire	Range  
High	81 - 125  
Medium	51 - 80  
Low	1 - 50  
If a cell is valid, you have to put it out by reducing the water with its value. Putting out fire also takes effort and you need to calculate it. Its value is equal to 25% of the cell’s value. In the end you will have to print the total effort. Keep putting out cells until you run out of water. If you don’t have enough water to put out a given cell – skip it and try the next one. In the end, print the cells you have put out in the following format:  
"Cells:  
 - {cell1}  
 - {cell2}  
 - {cell3}  
……  
 - {cellN}"  
"Effort: {effort}"  
In the end, print the total fire you have put out from all of the cells in the following format: "Total Fire: {totalFire}"  
*Input / Constraints*   
•	On the 1st line you are going to receive the fires with their cells in the format described above – integer numbers in the range [1…500]  
•	On the 2nd line, you are going to be given the water – an integer number in the range [0….100000]  
*Output*  
•	Print the cells, which you have put out in the following format:  
"Cells:  
 - {cell}  
 - {cell2}  
 - {cell3}  
 - {cell5}  
……  
 - {cellN}"  
•	Print the effort, rounded 2 digits after the decimal separator in the following format:  
"Effort: {effort}"  
•	Print the total fire put out  
"Total Fire: {totalFire}"  


## **09. * Hello, France**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/09_hello_france.py)
The budget was enough to get them to Frankfurt and they have some money left, but their final aim is to go to France, which means that they will need more finances. They’ve decided to make profit by buying items on discount from the Thrift Shop and selling them for a higher price. You must help them.  
Create a program that calculates the profit after buying some items and selling them on a higher price. In order to fulfil that, you are going to need certain data - you will receive a collection of items and a budget in the following format:  
{type->price|type->price|type->price……|type->price}  
{budget}  
The prices for each of the types cannot exceed a certain price, which is given bellow:  
Type	Maximum Price  
Clothes	50.00  
Shoes	35.00  
Accessories	20.50  
If a price for a certain item is higher than the maximum price, don’t buy it. Every time you buy an item, you have to reduce the budget with the value of its price. If you don’t have enough money for it, you can’t buy it. Buy as much items as you can.  
You have to increase the price of each of the items you have successfully bought with 40%. Print the list with the new prices and the profit you will gain from selling the items. They need exactly 150$ for tickets for the train, so if their budget after selling the products is enough – print – "Hello, France!" and if not – "Time to go."  
*Input / Constraints*  
•	On the 1st line you are going to receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]  
•	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]  
*Output*  
•	Print the list with the bought item’s new prices, rounded 2 digits after the decimal separator in the following format:  
"{price1} {price2} {price3} {price5}………{priceN}"  
•	Print the profit, rounded 2 digits after the decimal separator in the following format:  
"Profit: {profit}"  
•	If the money for tickets are enough, print: "Hello, France!" and if not – "Time to go."  


## **10. * Bread Factory**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/10_bread_factory.py)
As a young baker, you are baking the bread out of the bakery.  
You have initial energy 100 and initial coins 100. You will be given a string, representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2|event3…"  
Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}")  
•	If the event is "rest": you gain energy, the number in the second part. But your energy cannot exceed your initial energy (100). Print: "You gained {0} energy.".  
After that, print your current energy: "Current energy: {0}.".  
•	If the event is "order": You've earned some coins, the number in the second part. Each time you get an order, your energy decreases with 30 points.  
o	If you have energy to complete the order, print: "You earned {0} coins.".  
o	If your energy drops below 0, you skip the order and gain 50 energy points. Print: "You had to rest!".  
•	In any other case you are having an ingredient, you have to buy. The second part of the event, contains the coins you have to spent and remove from your coins.  
o	If you are not bankrupt (coins <= 0) you've bought the ingredient successfully, and you should print ("You bought {ingredient}.")  
o	If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.  
If you managed to handle all events through the day, print on the next three lines:  
"Day completed!", "Coins: {coins}", "Energy: {energy}".  
*Input / Constraints*  
You receive a string, representing the working day events, separated with '|' (vertical bar): " event1|event2|event3…".  
Each event contains event name or ingredient and a number, separated by dash("{event/ingredient}-{number}")  
*Output*  
Print the corresponding messages, described above.


## **01. More Exercises - Zeros to Back** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/more_ex_01_zeros_to_back.py)
Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros and moves them to the back without messing up the other elements. Print the resulting integer list


## **02. More Exercises - Tic-Tac-Toe**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/more_ex_02_tic_tac_toe.py)
You will receive a field of a tic-tac-toe game in three lines containing numbers separated by a single space.  
Legend:  
•	0 - empty space  
•	1 - first player move  
•	2 - second player move  
Find out who the winner is. If the first player wins print "First player won", otherwise if the second player wins print "Second player won", otherwise print "Draw!"


## **03. More Exercises - Josephus Permutation** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/more_ex_03_josephus_permutation.py)
This problem takes its name by arguably the most important event in the life of the ancient historian Josephus: according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege. Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded to kill one man every three, until one last man was left (and that it was supposed to kill himself to end the act). Well, Josephus and another man were the last two and, as we now know every detail of the story, you may have correctly guessed that they didn't exactly follow through the original idea.  
You are now to create a program that prints a Josephus permutation, receiving two lines of code (the list itself (string with elements separated by a single space) and a number k) as if they were in a circle and counted out every k places until none remained.


## **04. More Exercises - Battle Ships**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/06.%20List%20Basics%20-%20Exercise/more_ex_04_battle_ships.py)
You will be given a number n representing the number of rows of the field. On the next n lines you will receive each row of the field as a string with numbers separated by a space. Each number greater than zero represents a ship with a health equal to the number value. After that you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}". Each time a square is being attacked, if there is a ship there (number greater than 0) you should reduce its value. After the attacks have ended, print how many ships were destroyed (if its value has reached zero)


