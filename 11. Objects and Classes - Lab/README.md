## **01.	Comment** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/11.%20Objects%20and%20Classes%20-%20Lab/01_comment.py)
Create a class with name "Comment". The __init__ method should accept 3 parameters  
•	username  
•	content  
•	likes (optional, 0 by default)  
Use the exact names for your variables  
*Note:* there is no input/output for this problem. Test the class yourself and submit only the class


## **02.	Party** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/11.%20Objects%20and%20Classes%20-%20Lab/02_party.py)
Create a class Party that only has an attribute called people. The __init__ method should not accept any parameters. You will be given names of people (on separate lines) until you receive the command "End". Use the created class to solve this problem. After you receive the end command print 2 lines:  
•	"Going: {people}" - the people should be separated by comma and space ", "  
•	"Total: {total_people_going}"  
*Note:* submit all of your code including the class


## **03.	Email** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/11.%20Objects%20and%20Classes%20-%20Lab/03_email.py)
Create class Email. The __init__ method should receive sender, receiver and a content. It should also have a default set to False attribute called is_sent. The class should have two additional methods:  
•	send() - sets the is_sent attribute to True  
•	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"  
You will receive some emails until you receive "Stop" (separated by single space). The first will be the sender, the second one – the receiver and the third one – the content  
On the final line you will be given the indices of the sent emails separated by comma and space. Call the send() method for the given emails. For each email call the get_info() method  
*Note:* submit all of your code including the class


## **04.	Zoo** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/11.%20Objects%20and%20Classes%20-%20Lab/04_zoo.py)
Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in the zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists (mammals, fishes, birds). The class should also have 2 more methods:  
•	add_animal(species, name) - based on the species adds the name to the corresponding list  
•	get_info(species) - based on the species returns a string in the following format: "{Species} in {zoo_name}: {names}" and on another line "Total animals: {total_animals}"   
On the first line you will receive the name of the zoo. On the second line you will receive number n. On the next n lines you will receive animal info in the format: "{species} {name}". Add the animal to the zoo to the corresponding list. The "species" command will be mammal, fish or bird. On the final line you will receive a spеcies. At the end, print all the info for that species and the total count of animals.


## **05.	Circle** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/11.%20Objects%20and%20Classes%20-%20Lab/05_circle.py)
Create a class Circle. In the __init__ method the circle should only receive one parameter (its diameter). Create a class attribute called __pi that is equal to 3.14. The class should also have the following methods:  
•	calculate_circumference() - returns the circumference of the circle  
•	calculate_area() - returns the area of the circle  
•	calculate_area_of_sector(angle) - given the central angle in degrees, returns the area that fills the sector  
*Notes:* Search the formulas in the internet. Name your methods and variables exactly as in the description! Submit only the class. Test your class before submitting!


