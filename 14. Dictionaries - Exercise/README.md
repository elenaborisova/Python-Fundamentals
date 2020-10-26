## **01.	Count Chars in a String** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/01_count_chars_in_a_string.py)
Write a program that counts all characters in a string except for space (' ').   
Print all the occurrences in the following format:  
{char} -> {occurrences}


## **02.	A Miner Task** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/02_a_miner_task.py)
You will be given a sequence of strings, each on a new line. Every odd line on the console is representing a resource (e.g. Gold, Silver, Copper, and so on) and every even – quantity. Your task is to collect the resources and print them each on a new line.  
Print the resources and their quantities in the following format:  
{resource} –> {quantity}  
The quantities will be in the range [1 … 2 000 000 000]


## **03.	Legendary Farming** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/03_legendary_farming.py)
You've done all the work and the last thing left to accomplish is to own a legendary item. However, it's a tedious process and it requires quite a bit of farming. Anyway, you are not too pretentious – any legendary item will do. The possible items are:  
•	Shadowmourne – requires 250 Shards;  
•	Valanyr – requires 250 Fragments;  
•	Dragonwrath – requires 250 Motes;  
Shards, Fragments and Motes are the key materials and everything else is junk. You will be given lines of input, in the format:   
2 motes 3 ores 15 stones  
Keep track of the key materials - the first one that reaches the 250 mark, wins the race. At that point you have to print that the corresponding legendary item is obtained. Then, print the remaining shards, fragments, motes, ordered by quantity in descending order, then by name in ascending order, each on a new line. Finally, print the collected junk items in alphabetical order.  
*Input*   
•	Each line comes in the following format: {quantity} {material} {quantity} {material} … {quantity} {material}  
*Output*  
•	On the first line, print the obtained item in the format: {Legendary item} obtained!  
•	On the next three lines, print the remaining key materials in descending order by quantity  
o	If two key materials have the same quantity, print them in alphabetical order  
•	On the final several lines, print the junk items in alphabetical order  
o	All materials are printed in format {material}: {quantity}  
o	The output should be lowercase, except for the first letter of the legendary


## **04.	Orders** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/04_orders.py)
Write a program that keeps information about products and their prices. Each product has a name, a price and a quantity. If the product doesn't exist yet, add it with its starting quantity.  
If you receive a product, which already exists, increase its quantity by the input quantity and if its price is different, replace the price as well.  
You will receive products' names, prices and quantities on new lines. Until you receive the command "buy", keep adding items. When you do receive the command "buy", print the items with their names and total price of all the products with that name.   
*Input*  
•	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".  
•	The product data is always delimited by a single space.  
*Output*  
•	Print information about each product in the following format:   
"{productName} -> {totalPrice}"  
•	Format the average grade to the 2nd digit after the decimal separator.


## **05.	SoftUni Parking** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/05_softuni_parking.py)
SoftUni just got a new parking lot. It's so fancy, it even has online parking validation. Except the online service doesn't work. It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?  
Write a program, which validates a parking place for an online service. Users can register to park and unregister to leave.  
The program receives 2 types of commands:	 
•	"register {username} {licensePlateNumber}":  
o	The system only supports one car per user at the moment, so if a user tries to register another license plate, using the same username, the system should print:  
"ERROR: already registered with plate number {licensePlateNumber}"  
o	If the aforementioned checks passes successfully, the plate can be registered, so the system should print:  
 "{username} registered {licensePlateNumber} successfully"  
•	"unregister {username}":  
o	If the user is not present in the database, the system should print:  
"ERROR: user {username} not found"  
o	If the aforementioned check passes successfully, the system should print:  
"{username} unregistered successfully"  
After you execute all of the commands, print all the currently registered users and their license plates in the format:  
•	"{username} => {licensePlateNumber}"  
*Input*  
•	First line: n – number of commands – integer    
•	Next n lines: commands in one of the two possible formats:  
o	Register: "register {username} {licensePlateNumber}"  
o	Unregister: "unregister {username}"  
The input will always be valid and you do not need to check it explicitly.


## **06.	Courses** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/06_courses.py)
Write a program that keeps information about courses. Each course has a name and registered students.  
You will be receiving a course name and a student name, until you receive the command "end". Check if such course already exists, and if not, add the course. Register the user into the course. When you receive the command "end", print the courses with their names and total registered users, ordered by the count of registered users in descending order. For each contest print the registered users ordered by name in ascending order.  
*Input*  
•	Until the "end" command is received, you will be receiving input in the format: "{courseName} : {studentName}".  
•	The product data is always delimited by " : ".  
*Output*  
•	Print the information about each course in the following the format:  
"{courseName}: {registeredStudents}"  
•	Print the information about each student, in the following the format:  
"-- {studentName}"


## **07. Student Academy** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/07_student_academy.py)
Write a program that keeps information about students and their grades.   
You will receive n pair of rows. First you will receive the student's name, after that you will receive his grade. Check if the student already exists and if not, add him. Keep track of all grades for each student.  
When you finish reading the data, keep the students with average grade higher than or equal to 4.50. Order the filtered students by average grade in descending order.  
Print the students and their average grade in the following format:  
{name} –> {averageGrade}  
Format the average grade to the 2nd decimal place.


## **08.	Company Users** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/08_company_users.py)
Write a program that keeps information about companies and their employees.   
You will be receiving a company name and an employee's id, until you receive the command "End" command. Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.  
When you finish reading the data, order the companies by the name in ascending order.   
Print the company name and each employee's id in the following format:  
{companyName}  
-- {id1}  
-- {id2}  
-- {idN}  
*Input / Constraints*   
•	Until you receive the "End" command, you will be receiving input in the format: "{companyName} -> {employeeId}".  
•	The input always will be valid.


## **09.	* ForceBook** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/09_forcebook.py)
The force users are struggling to remember which side are the different forceUsers from, because they switch them too often. So you are tasked to create a web application to manage their profiles. You should store an information for every unique forceUser, registered in the application.  
You will receive several input lines in one of the following formats:  
{forceSide} | {forceUser}  
{forceUser} -> {forceSide}  
The forceUser and forceSide are strings, containing any character.  
If you receive forceSide | forceUser, you should check if such forceUser already exists, and if not, add him/her to the corresponding side.   
If you receive a forceUser -> forceSide, you should check if there is such a forceUser already and if so, change his/her side. If there is no such forceUser, add him/her to the corresponding forceSide, treating the command as a new registered forceUser.  
Then you should print on the console: "{forceUser} joins the {forceSide} side!"   
You should end your program when you receive the command "Lumpawaroo". At that point you should print each force side, ordered descending by forceUsers count, than ordered by name. For each side print the forceUsers, ordered by name.  
In case there are no forceUsers in a side, you shouldn't print the side information.   
*Input / Constraints*   
•	The input comes in the form of commands in one of the formats specified above.  
•	The input ends, when you receive the command "Lumpawaroo".  
*Output*  
•	As output for each forceSide, ordered descending by forceUsers count, then by name,  you must print all the forceUsers, ordered by name alphabetically.  
•	The output format is:  
Side: {forceSide}, Members: {forceUsers.Count}  
! {forceUser}  
! {forceUser}  
! {forceUser}  
•	In case there are NO forceUsers, don't print this side. 


## **10.	* SoftUni Exam Results** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/10_softuni_exam_results.py)
Judge statistics on the last Programing Fundamentals exam was not working correctly, so you have the task to take all the submissions and analyze them properly. You should collect all the submissions and print the final results and statistics about each language that the participants submitted their solutions in.  
You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and his submissions and points.   
You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest, but preserve his submissions in the total count of submissions for each language.  
After receiving "exam finished" print each of the participants, ordered descending by their max points, then by username, in the following format:  
Results:  
{username} | {points}  
…  
After that print each language, used in the exam, ordered descending by total submission count and then by language name, in the following format:  
Submissions:  
{language} – {submissionsCount}  
…  
*Input / Constraints*  
Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}".  
You can receive a ban command -> "{username}-banned"  
The points of the participant will always be a valid integer in the range [0-100];  
*Output*  
•	Print the exam results for each participant, ordered descending by max points and then by username, in the following format:   
Results:  
{username} | {points}  
…  
•	After that print each language, ordered descending by total submissions and then by language name, in the following format:  
Submissions:  
{language} – {submissionsCount}  
…  
•	Allowed working time / memory: 100ms / 16MB.


## **01. More Exercises - Ranking** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/more_ex_01_ranking.py)
Here comes the final and the most interesting part – the Final ranking of the candidate-interns. The final ranking is determined by the points of the interview tasks and from the exams in SoftUni. Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". Save that data because you will need it later. After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". Here is what you need to do.   
•	Check if the contest is valid (if you received it in the first type of input)  
•	Check if the password is correct for the given contest  
•	Save the user with the contest they take part in (a user can take part in many contests) and the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.  
At the end you have to print the info for the user with the most points in the format "Best candidate is {user} with total {total points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.  
*Input*    
•	strings in format "{contest}:{password for contest}" until the "end of contests" command. There will be no case with two equal contests  
•	strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.  
•	There will be no case with 2 or more users with same total points!  
*Output*    
•	On the first line print the best user in format "Best candidate is {user} with total {total points} points.".   
•	Then print all students ordered as mentioned above in format:  
{user1 name}  
{contest1} -> {points}  
{contest2} -> {points}  
*Constraints*  
•	the strings may contain any ASCII character except from (:, =, >)  
•	the numbers will be in range [0 - 10000]  
•	second input is always valid


## **02. More Exercises - Judge** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/more_ex_02_judge.py)
You know the jude system, right?! Your job is to create a program similar to the Judge system.  
You will receive several input lines in one of the following formats:  
{username} -> {contest} -> {points}  
The constestName and username are strings, the given points will be an integer number. You need to keep track of every contest and individual statistics of every user. You should check if such contest already exists, and if not, add it, otherwise check if the current user Is participating in the contest, if he is participating take the higher score, otherwise just add it.  
Also you need to keep individual statistics for each user - the total points of all constests.   
You should end your program when you receive the command "no more time". At that point you should print each contest in order of input, for each contest print the participants ordered by points in desecending order, than ordered by name in ascending order.  After that, you should print individual statistics for every participant ordered by total points in desecnding order, and then by alphabetical order.  
*Input / Constraints*    
•	The input comes in the form of commands in one of the formats specified above.  
•	Username and contest name always will be one word.  
•	Points will be an integer will be an integer in range [0, 1000].  
•	There will be no invalid input lines.  
•	If all sorting criteria fail, the order should be by order of input.  
•	The input ends when you receive the command "no more time".  
*Output*  
•	The output format for the contests is:   
{constestName}: {participants.Count} participants  
{position}. {username} <::> {points}  
•	After you print all contests, print the individual statistics for every participant.  
•	The output format is:  
Individual standings:  
{position}. {username} -> {totalPoints}


## **03. More Exercises - MOBA Challenger** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/more_ex_03_moba_challenger.py)
Pesho is a pro MOBA player, he is struggling to become а master of the Challenger tier. So he watches carefully the statistics in the tier.  
You will receive several input lines in one of the following formats:  
"{player} -> {position} -> {skill}"  
"{player} vs {player}"  
The player and position are strings, the given skill will be an integer number. You need to keep track of every player.  
When you receive a player and his position and skill, add him to the player pool, if he isn't present, else add his position and skill or update his skill, only if the current position skill is lower than the new value.  
If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:  
Compare their positions, if they got at least one in common, the player with better total skill points wins and the other is demoted from the tier -> remove him. If they have same total skill points, the duel is tie and they both continue in the Season.  
If they don't have positions in common, the duel isn't happening and both continue in the Season.  
You should end your program when you receive the command "Season end". At that point you should print the players, ordered by total skill in desecending order, then ordered by player name in ascending order. Foreach player print their position and skill, ordered desecending by skill, then ordered by position name in ascending order.  
*Input / Constraints*  
•	The input comes in the form of commands in one of the formats specified above.  
•	Player and position will always be one word string, containing no whitespaces.  
•	Skill will be an integer in the range [0, 1000].  
•	There will be no invalid input lines.  
•	The programm ends when you receive the command "Season end".  
*Output*  
•	The output format for each player is:  
"{player}: {totalSkill} skill"  
"- {position} <::> {skill}"


## **04. More Exercises - Snowwhite** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/more_ex_04_snowwhite.py)
Snow White loves her dwarfs, but there are so many and she doesn't know how to order them. Does she order them by name? Or by color of their hat? Or by physics? She can't decide, so its up to you to write a program that does it for her.  
You will be receiving several input lines which contain data about dwarfs in the following format:  
{dwarfName} <:> {dwarfHatColor} <:> {dwarfPhysics}  
The dwarfName and the dwarfHatColor are strings. The dwarfPhysics is an integer.  
You must store the dwarfs in your program. There are several rules though:  
•	If 2 dwarfs have the same name but different color, they should be considered different dwarfs, and you should store both of them.  
•	If 2 dwarfs have the same name and the same color, store the one with the higher physics.  
When you receive the command "Once upon a time", the input ends. You must order the dwarfs by physics in descending order and then by total count of dwarfs with the same hat color in descending order.   
Then you must print them all.   
*Input*    
•	The input will consists of several input lines, containing dwarf data in the format, specified above.  
•	The input ends when you receive the command "Once upon a time".   
*Output*  
•	As output you must print the dwarfs, ordered in the way , specified above.  
•	The output format is: ({hatColor}) {name} <-> {physics}  
*Constraints*  
•	The dwarfName will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.  
•	The dwarfHatColor will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.  
•	The dwarfPhysics will be an integer in range [0, 231 – 1].  
•	There will be no invalid input lines.  
•	If all sorting criteria fail, the order should be by order of input.  
•	Allowed working time / memory: 100ms / 16MB.


## **05. More Exercises - Dragon Army** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/14.%20Dictionaries%20-%20Exercise/more_ex_05_dragon_army.py)
Heroes III is the best game ever. Everyone loves it and everyone plays it all the time. Stamat is no exclusion to this rule. His favorite units in the game are all types of dragons – black, red, gold, azure etc… He likes them so much that he gives them names and keeps logs of their stats: damage, health and armor. The process of aggregating all the data is quite tedious, so he would like to have a program doing it. Since he is no programmer, it's your task to help him.  
You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats. Type is preserved as in the order of input, but dragons are sorted alphabetically by name. For each type, you should also print the average damage, health and armor of the dragons. For each dragon, print his own stats.   
There may be missing stats in the input, though. If a stat is missing you should assign it default values. Default values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by null.  
The input is in the following format {type} {name} {damage} {health} {armor}. Any of the integers may be assigned null value. See the examples below for better understanding of your task.  
If the same dragon is added a second time, the new stats should overwrite the previous ones. Two dragons are considered equal if they match by both name and type.  
*Input*    
•	On the first line, you are given number N -> the number of dragons to follow  
•	On the next N lines, you are given input in the above described format. There will be single space separating each element.  
*Output*   
•	Print the aggregated data on the console  
•	For each type, print average stats of its dragons in format {Type}::({damage}/{health}/{armor})  
•	Damage, health and armor should be rounded to two digits after the decimal separator  
•	For each dragon, print its stats in format -{Name} -> damage: {damage}, health: {health}, armor: {armor}  
*Constraints*  
•	N is in range [1…100]  
•	The dragon type and name are one word only, starting with capital letter.  
•	Damage health and armor are integers in range [0 … 100000] or null
