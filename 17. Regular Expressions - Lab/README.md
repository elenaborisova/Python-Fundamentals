## **01.	Match Full Name** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/17.%20Regular%20Expressions%20-%20Lab/01_match_full_name.py)
Write a program to match full names from a list of names and print them on the console.  
Writing the Regular Expression  
First, write a regular expression to match a valid full name, according to these conditions:  
•	A valid full name has the following characteristics:  
o	It consists of two words.  
o	Each word starts with a capital letter.  
o	After the first letter, it only contains lowercase letters afterwards.  
o	Each of the two words should be at least two letters long.  
o	The two words are separated by a single space.  
To help you out, we've outlined several steps:  
1.	Use the online regex tester like https://pythex.org/  
2.	Check out how to use character sets (denoted with square brackets - "[]")   
3.	Specify that you want two words with a space between them (the space character ' ', and not any whitespace symbol)  
4.	For each word, specify that it should begin with an uppercase letter using a character set. The desired characters are in a range – from 'A' to 'Z'.  
5.	For each word, specify that what follows the first letter are only lowercase letters, one or more – use another character set and the correct quantifier.  
6.	To prevent capturing of letters across new lines, put "\b" at the beginning and at the end of your regex. This will ensure that what precedes and what follows the match is a word boundary (like a new line).



## **02.	Match Phone Number** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/17.%20Regular%20Expressions%20-%20Lab/02_match_phone_number.py)
Write a regular expression to match a valid phone number from Sofia. After you find all valid phones, print them on the console, separated by a comma and a space ", ".  
Compose the Regular Expression  
A valid number has the following characteristics:  
•	It starts with "+359"  
•	Then, it is followed by the area code (always 2)    
•	After that, it's followed by the number itself:  
o	The number consists of 7 digits (separated in two groups of 3 and 4 digits respectively).  
•	The different parts are separated by either a space or a hyphen ('-').  
You can use the following RegEx properties to help with the matching:  
•	Use quantifiers to match a specific number of digits  
•	Use a capturing group to make sure the delimiter is only one of the allowed characters (space or hyphen) and not a combination of both (e.g. +359 2-111 111 has mixed delimiters, it is invalid). Use a group backreference to achieve this.  
•	Add a word boundary at the end of the match to avoid partial matches (the last example on the right-hand side).  
•	Ensure that before the '+' sign there is either a space or the beginning of the string. 


## **03.	Match Dates** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/17.%20Regular%20Expressions%20-%20Lab/03_match_dates.py)
Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". Use capturing groups in your regular expression.  
Compose the Regular Expression  
Every valid date has the following characteristics:   
•	Always starts with two digits, followed by a separator  
•	After that, it has one uppercase and two lowercase letters (e.g. Jan, Mar).  
•	After that, it has a separator and exactly 4 digits (for the year).  
•	The separator could be either of three things: a period ("."), a hyphen ("-") or a forward slash ("/")  
•	The separator needs to be the same for the whole date (e.g. 13.03.2016 is valid, 13.03/2016 is NOT). Use a group backreference to check for this.


## **04.	Match Numbers** [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/17.%20Regular%20Expressions%20-%20Lab/04_match_numbers.py)
Write a program, which finds all integer and floating-point numbers in a string.  
Compose the Regular Expression 
A number has the following characteristics:  
•	Has either whitespace before it or the start of the string (match either ^ or what's called a positive lookbehind). The entire syntax for the beginning of your RegEx might look something like "(^|(?<=\s))".  
•	The number might or might not be negative, so it might have a hyphen on its left side ("-").  
•	Consists of one or more digits.  
•	Might or might not have digits after the decimal point  
•	The decimal part (if it exists) consists of a period (".") and one or more digits after it. Use a capturing group.  
•	Has either whitespace before it or the end of the string (match either $ or what's called a positive lookahead). The syntax for the end of the RegEx might look something like "($|(?=\s))".  
Let's see how we would translate the above rules into a regular expression:  
•	First off, we need to establish what needs to exist before our number. We can't use \b here, since it includes "-", which we need to match negative numbers.  
Instead, we'll use a positive lookbehind, which matches if there's something immediately behind it. We'll match if we're either at the start of the string (^), or if there's any whitespace behind the string:


