## **01.	Bakery** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/13.%20Dictionaries%20-%20Lab/01_bakery.py)
This is your first task in your new job. You were tasked to create a list of the stock in a bakery and you really don't want to fail at you first day at work.  
You will receive a single line containing some food (keys) and quantities (values). They will be separated by a single space (the first element is the key, the second – the value and so on). Create a dictionary with all the keys and values and print it on the console


## **02.	Stock** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/13.%20Dictionaries%20-%20Lab/02_stock.py)
After you have successfully completed your first task, your boss decides to give you another one right away. Now not only you have to keep track of the stock, but also you have to answer customers if you have some products in stock or not.  
You will be given key-value pairs of products and quantities (on a single line separated by space). On the next line you will be given products to search for. Check for each product, you have 2 possibilities:  
•	If you have the product, print "We have {quantity} of {product} left"  
•	Otherwise, print "Sorry, we don't have {product}"  


## **03.	Statistics** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/13.%20Dictionaries%20-%20Lab/03_statistics.py)
You seem to be doing great at your first job. You have now successfully completed the first 2 of your tasks and your boss decides to give you as your next task something more challenging. You have to accept all the new products coming in the bakery and finally gather some statistics.  
You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics". Sometimes you may receive a product more than once. In that case you have to add the new quantity to the existing one. When you receive the "statistics" command, print the following:  
"Products in stock:  
- {product1}: {quantity1}  
- {product2}: {quantity2}  
…  
Total Products: {count_all_products}  
Total Quantity: {sum_all_quantities}"


## **04.	Odd Occurrences** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/13.%20Dictionaries%20-%20Lab/04_odd_occurrences.py)
Write a program that extracts all elements from a given sequence of words that are present in it an odd number of times (case-insensitive).  
•	Words are given on a single line, space separated.  
•	Print the result elements in lowercase, in their order of appearance.


## **05.	Word Synonyms** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/13.%20Dictionaries%20-%20Lab/05_word_synonyms.py)
Write a program, which keeps a dictionary with synonyms. The key of the dictionary will be the word. The value will be a list of all the synonyms of that word. You will be given a number n – the count of the words. After each word, you will be given a synonym, so the count of lines you have to read from the console is 2 * n. You will be receiving a word and a synonym each on a separate line like this:  
•	{word}  
•	{synonym}  
If you get the same word twice, just add the new synonym to the list.   
Print the words in the following format:  
{word} - {synonym1, synonym2… synonymN}  


