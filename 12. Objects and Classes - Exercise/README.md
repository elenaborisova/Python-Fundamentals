## **01.	Storage** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/12.%20Objects%20and%20Classes%20-%20Exercise/01_storage.py)
Create a class Storage. The __init__ method should accept one parameter: the capacity of the storage. The Storage class should also have an attribute called storage, where all the items will be stored. The class should have two additional methods:  
•	add_product(product) - adds the product in the storage if there is space for it  
•	get_products() - returns the storage list  


## **02.	Weapon** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/12.%20Objects%20and%20Classes%20-%20Exercise/02_weapon.py)
Create a class Weapon. The __init__ method should receive an amount of bullets (integer). Create an attribute called bullets, to store them. The class should also have the following methods:  
•	shoot() - if there are bullets in the weapon, reduce them by 1 and return a message "shooting…". If there are no bullets left, return: "no bullets left"  
You should also override the toString method, so that the following code: print(weapon) should work. To do that define a __repr__ method that returns "Remaining bullets: {amount_of_bullets}". You can read more about the __repr__ method here: link


## **03.	Catalogue** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/12.%20Objects%20and%20Classes%20-%20Exercise/03_catalogue.py)
Create a class Catalogue. The __init__ method should accept the name of the catalogue. Each catalogue should also have an attribute called products and it should be a list. The class should also have three more methods:  
•	add_product(product) - add the product to the product list  
•	get_by_letter(first_letter) - returns a list containing only the products that start with the given letter  
•	__repr__ - returns the catalogue info in the following format:   
"Items in the {name} catalogue:  
{item1}  
{item2}  
…"  
The items should be sorted alphabetically (default sorting)


## **04.	Town** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/12.%20Objects%20and%20Classes%20-%20Exercise/04_town.py)
Create a class Town. The __init__ method should receive the name of the town. It should also have 3 more methods:  
•	set_latitude(latitude) - set an attribute called latitude to the given one  
•	set_longitude(longitude) - set an attribute called longitude to the given one  
•	__repr__ - return representation of the object in the following string format:  
"Town: {name} | Latitude: {latitude} | Longitude: {longitude}"


## **05.	Class** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/12.%20Objects%20and%20Classes%20-%20Exercise/05_class.py)
Create a class Class. The __init__ method should receive the name of the class. It should also have 2 lists (students and grades). Create a class attribute __students_count equal to 22. The class should also have 3 additional methods:  
•	add_student(name, grade) - if there is space in the class, add the student and the grade in the two lists  
•	get_average_grade() - returns the average of all existing grades formatted to the second decimal point (as a number)  
•	__repr__ - returns the string (single line): "The students in {class_name}: {students}. Average grade: {get_average_grade()}". The students must be seperated by ", "


## **06.	Inventory** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/12.%20Objects%20and%20Classes%20-%20Exercise/06_inventory.py)
Create a class Inventory. The __init__ method should accept only the capacity of the inventory. The capacity should be a private attribute (__capacity). You can read more about private attributes here. Each inventory should also have an attribute called items, where all the items will be stored. The class should also have 3 methods:  
•	add_item(item) - adds the item in the inventory if there is space for it. Otherwise, returns   
"not enough room in the inventory"  
•	get_capacity() - returns the value of __capacity  
•	__repr__() - returns "Items: {items}.\nCapacity left: {left_capacity}". The items should be separated by ", "


## **07.	Articles** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/12.%20Objects%20and%20Classes%20-%20Exercise/07_articles.py)
Create a class Article. The __init__ method should accept 3 arguments: title, content, author. The class should also have 4 methods:  
•	edit(new_content) - changes the old content to the new one  
•	change_author(new_author) - changes the old author to with the new one  
•	rename(new_title) - changes the old title with the new one  
•	__repr__() - returns the following string "{title} - {content}: {author}"


## **08.	* Vehicle** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/12.%20Objects%20and%20Classes%20-%20Exercise/08_vehicle.py)
Create a class Vehicle. The __init__ method should receive: type, model, price. You should also set the owner to None. The class should have the following methods:  
•	buy(money, owner) - if the person has enough money and the vehicle has no owner, returns: "Successfully bought a {type}. Change: {change}" and sets the owner to the given one. If the money is not enough, return: "Sorry, not enough money". If the car already has an owner, return: "Car already sold"  
•	sell() - if the car has an owner, set it to None again. Otherwise, return: "Vehicle has no owner"  
•	__repr__() - returns "{model} {type} is owned by: {owner}" if the vehicle has an owner. Otherwise, return: "{model} {type} is on sale: {price}"


## **09.	* Movie** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/12.%20Objects%20and%20Classes%20-%20Exercise/09_movie.py)
Create a class Movie. The __init__ method should receive a name and director. It should also have default value of an attribute watched to be False. There should also be a class attribute __watched_movies which will keep track of all the watched movies. The class should have the following methods:  
•	change_name(new_name) - changes the name of the movie  
•	change_director(new_director) - changes the director of the movie  
•	watch() - change the watched attribute to True and increase the total watched movies class attribute (if the movie is not already watched)  
•	__repr__() - returns "Movie name: {name}; Movie director: {director}. Total watched movies: {__watched_movies}"


