## **01. Which Are In?** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/01_which_are_in.py)
Given two lists of strings print a new list of the strings that contains words from the first list which are substrings of any of the strings in the second list (only unique values)  
*Input*  
There will be 2 lines of input: the two lists separated by ", "  
*Output*  
Print the resulting list on the console


## **02. Big Numbers Lover** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/02_big_numbers_lover.py)
You really like big numbers, so you always find a way to form one from numbers given to you  
You will receive a single line containing numbers separated by a single space. Form the biggest number possible from them by sorting them as strings.


## **03. Next Version** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/03_next_version.py)
You're fed up about changing the version of your software manually. Instead, you will create a little script that will make it for you.  
You will be given a version as in this example: "1.3.4". You have to find the next version and print it ("1.3.5" from the example). The only rule is that the numbers cannot be greater than 9. If that happens, set the current number to 0 and increase the number before it. For more clarification, see the examples. Note: there will be no case where the first number will get greater than 9


## **04. Office Chairs** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/04_office_chairs.py)
So you've found a meeting room - phew! You arrive there ready to present, and find that someone has taken one or more of the chairs!! You need to find some quick.... check all the other meeting rooms to see if all of the chairs are in use.  
You will be given a number n representing how many rooms there are. On the next n lines for each room you will get how many chairs there are and how many of them will be taken. The chairs will be represented by "X"s, then there will be a space " " and a number representing the taken places. Example: "XXXXX 4" (5 chairs and 1 of them is left free). Keep track of the free chairs, you will need them later. However if you get to a room where there are more people than chairs, print the following message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". If there is enough chairs in each room print: "Game On, {total_free_chairs} free chairs left"


## **05. Electron Distribution** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/05_electron_distribution.py)
You are a mad scientist and you decided to play with electron distribution among atom's shells. You know that basic idea of electron distribution is that electrons should fill a shell until it's holding the maximum number of electrons.  
The rules for electron distribution are as follows:  
•	Maximum number of electrons in a shell is distributed with a rule of 2n^2 (n being position of a shell a.k.a. the list index + 1).  
•	For example, maximum number of electrons in 3rd shield is 2 * 3^2 = 18.  
•	Electrons should fill the lowest level shell first.  
•	If the electrons have completely filled the lowest level shell, the other unoccupied electrons will fill the higher level shell and so on.


## **06. Group of 10's** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/06_group_of_tens.py)
Write a program that receives a list of numbers (string containing integers separated by ", ") and prints lists with the numbers them into lists of 10's.  
*Examples:*  
•	The numbers 2 8 4 3 fall into the group under 10  
•	The numbers 13 19 14 15 fall into the group under 20  


## ** 07. Decipher This!** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/07_decipher_this.py)
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:  
For each word:  
•	the second and the last letter are switched (e.g. Hello becomes Holle)  
•	the first letter is replaced by its character code (e.g. H becomes 72)


## **08. * Moving Target** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/08_moving_target.py)
You are at the shooting gallery again and you need a program that helps you keep track of moving targets. On the first line, you will receive a sequence of targets with their integer values, split by a single space. Then, you will start receiving commands for manipulating the targets, until the "End" command. The commands are the following:  
•	Shoot {index} {power}  
o	Shoot the target at the index, if it exists by reducing its value by the given power (integer value).A target is considered shot when its value reaches 0.  
o	Remove the target, if it is shot.  
•	Add {index} {value}  
o	Insert a target with the received value at the received index, if it exist. If not, print: "Invalid placement!"  
•	Strike {index} {radius}  
o	Remove the target at the given index and the ones before and after it depending on the radius, if such exist. If any of the indices in the range is invalid print:  
"Strike missed!" and skip this command.  
 Example:  Strike 2 2  
	{radius}	{radius}	{strikeIndex}	{radius}	{radius}		 
•	End  
o	Print the sequence with targets in the following format:  
{target1}|{target2}…|{targetn}  
*Input / Constraints*  
•	On the first line you will receive the sequence of targets – integer values [1-10000].  
•	On the next lines, until the "End" will be receiving the command described above – strings.  
•	There will never be a case when "Strike" command would empty the whole sequence.  
*Output*  
•	Print the appropriate message in case of "Strike" command if necessary.  
•	In the end, print the sequence of targets in the format described above.



## **09. * Heart Delivery** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/09_heart_delivery.py)
You will receive a string with even integers, separated by a "@". This is our neighborhood. After that a series of Jump commands will follow, until you receive "Love!" Every house in the neighborhood needs a certain number of hearts delivered by Cupid, in order to be able to celebrate Valentine’s Day. Those needed hearts are indicated by the integers in the neighborhood.  
Cupid starts at the position of the first house (index 0) and must jump by a given length. The jump commands will be in this format: "Jump {length}".   
Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2. If the needed hearts for a certain house become equal to 0 , print on the console "Place {houseIndex} has Valentine's day." If Cupid jumps to a house where the needed hearts are already 0, print on the console "Place {houseIndex} already had Valentine's day.".  
Keep in mind that Cupid can have a bigger jump length than the size of the neighborhood and if he does jump outside of it, he should start from the first house again.   
For example, we are given this neighborhood: 6@6@6. Cupid is at the start and jumps with a length of 2. He will end up at index 2 and decrease the needed hearts there by 2: [6, 6, 4]. Next he jumps again with a length of 2 and goes outside the neighborhood, so he goes back to the first house (index 0) and again decreases the needed hearts there: [4, 6, 4].  
*Input*   
•	On the first line you will receive a string with even integers separated by "@" – the neighborhood and the number of hearts for each house.  
•	On the next lines, until "Love!" is received, you will be getting jump commands in this format: "Jump {length}".  
*Output*  
At the end print Cupid's last position and whether his mission was successful or not:  
•	"Cupid's last position was {lastPositionIndex}."  
•	If each house has had a Valentine's day, print:  
o	"Mission was successful."  
•	If not, print the count of all houses that didn`t celebrate a Valentine's Day:  
o	"Cupid has failed {houseCount} places."  
*Constraints*  
•	The neighborhood`s size will be in the range [1…20]  
•	Each house will need an even number of hearts in the range [2 … 10]  
•	Each jump length will be an integer in the range [1 … 20]


## **10. * Inventory** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/10_inventory.py)
*Input / Constraints*  
You will receive a journal with some Collecting items, separated with ', ' (comma and space). After that, until receiving "Craft!" you will be receiving different commands.   
Commands (split by " - "):  
•	"Collect - {item}" – Receiving this command, you should add the given item in your inventory. If the item already exists, you should skip this line.  
•	"Drop - {item}" – You should remove the item from your inventory, if it exists.  
•	"Combine Items - {oldItem}:{newItem}" – You should check if the old item exists, if so, add the new item after the old one. Otherwise, ignore the command.  
•	"Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.  
*Output*  
After receiving "Craft!" print the items in your inventory, separated by ", " (comma and space).


## **10. ** Man O War** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/10_man_o_war.py)
Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the first line you will receive the status of the pirate ship, which is a string representing integer sections separated by '>'. On the second line you will receive the same type of status, but for the warship:  
"{section1}>{section2}>{section3}… {sectionn}"  
On the third line you will receive the maximum health capacity a section of the ship can reach.  
The following lines represent commands until "Retire":  
•	Fire {index} {damage} – the pirate ship attacks the warship with the given damage at that section. Check if the index is valid and if not skip the command. If the section breaks (health <= 0) the warship sinks, print the following and stop the program:  
"You won! The enemy ship has sunken."  
•	Defend {startIndex} {endIndex} {damage} - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:  
"You lost! The pirate ship has sunken."  
•	Repair {index} {health} - the crew repairs a section of the pirate ship with the given health. Check if the index is valid and if not skip the command. The health of the section cannot exceed the maximum health capacity.  
•	Status – prints the count of all sections of the pirate ship that need repair soon, which are all sections that are lower than 20% of the maximum health capacity. Print the following:  
"{count} sections need repair."  
In the end if a stalemate occurs print the status of both ships, which is the sum of their individual sections in the following format:  
"Pirate ship status: {pirateShipSum}"  
"Warship status: {warshipSum}"  
*Input*    
•	On the 1st line you are going to receive the status of the pirate ship (integers separated by '>')  
•	On the 2nd line you are going to receive the status of the warship  
•	On the 3rd line you are going receive the maximum health a section of a ship can reach.  
•	On the next lines, until "Retire", you will be receiving commands.  
*Output*  
•	Print the output in the format described above.  
*Constraints*  
•	The section numbers will be integers in the range [1….1000]  
•	The indexes will be integers [-200….200]  
•	The damage will be an integer in the range [1….1000]  
•	The health will be an integer in the range [1….1000]


## **01. More Exercises - Messaging** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/more_ex_01_messaging.py)
You will be given a list of numbers and a string. For each element of the list you have to calculate the sum of its digits and take the element, corresponding to that index from the text. If the index is greater than the length of the text, start counting from the beginning (so that you always have a valid index). Then you get that element from the text, you must remove the character you have taken from it (so for the next index, the text will be with one character less).


## **02. More Exercises - Car Race** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/more_ex_02_car_race.py)
Write a program to calculate the winner of a car race. You will receive a list of numbers. Each element of the list represents the time needed to pass through that step (the index). There are going to be two cars. One of them starts from the left side and the other one starts from the right side. The middle index of the list is the finish line. The number of elements in the list will always be odd. Calculate the total time for each racer to reach the finish, which is the middle of the list, and print the winner with his total time (the racer with less time). If you have a zero in the list, you have to reduce the time of the racer that reached it by 20% (from his current time).  
Print the result in the following format "The winner is {left/right} with total time: {total time}".


## **03. More Exercises - Take/Skip Rope** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/more_ex_03_take_skip_rope.py)
Write a program, which reads a string and skips through it, extracting a hidden message. The algorithm you have to implement is as follows:  
Let’s take the string “skipTest_String044170” as an example.  
Take every digit from the string and store it somewhere. After that, remove all the digits from the string. After this operation, you should have two lists of items: the numbers list and the non-numbers list:  
•	Numbers list: [0, 4, 4, 1, 7, 0]  
•	Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]  
After that, take every digit in the numbers list and split it up into a take list and a skip list, depending on whether the digit is in an even or an odd index:  
•	Numbers list: [0, 4, 4, 1, 7, 0]  
•	Take list: [0, 4, 7]  
•	Skip list: [4, 1, 0]  
Afterwards, iterate over both of the lists and skip {skipCount} characters from the non-numbers list, then take {takeCount} characters and store it in a result string. Note that the skipped characters are summed up as they go. The process would look like this on the aforementioned non-numbers list:  
1.	Take 0 characters  Taken: "", skip 4 characters (total 0)  Skipped: "skipTest_String" Result: ""  
2.	Take 4 characters Taken: "Test", skip 1 characters (total 4)  Skipped: "skip"  Result: "Test"  
3.	Take 7 characters Taken: "String", skip 0 characters (total 9) Skipped: ""  Result: "TestString"  
After that, just print the result string on the console.  
*Input*  
•	First line: The encrypted message as a string  
*Output*  
•	First line: The decrypted message as a string  
*Constraints*  
•	The count of digits in the input string will always be even.  
•	The encrypted message will contain any printable ASCII character.


## **04. More Exercises - Social Distribution** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/10.%20Lists%20Advanced%20-%20Exercise/more_ex_04_social_distribution.py)
A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what and that is exactly what you are called to do for this problem.
On the first line you will be given the population (numbers separated by comma and space ", "). On the second line you will be given the minimum wealth. You have to distribute the wealth, so that there is no part of the population that has less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population. There will be cases, where the distribution will not be possible. In that case, print "No equal distribution possible" 




