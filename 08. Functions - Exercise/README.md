## **01. Smallest of Three Numbers**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/01_smallest_of_three_numbers.py)
Write a function which receives three integer numbers and returns the smallest. Use appropriate name for the function.


## **02. Add and Subtract**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/02_add_and_subtract.py)
You will receive three integer numbers.   
Write a function sum_numbers() to get the sum of the first two integers and subtract() function that subtracts the third integer from the result. Wrap the two functions in a function called add_and_subtract() which will receive the three numbers


## **03. Characters in Range**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/03_characters_in_range.py)
Write a function that receives two characters and returns a single string with all the characters in between them according to the ASCII code.


## **04. Odd and Even Sum**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/04_odd_and_even_sum.py)
You will receive a single number. You have to write a function that returns the sum of all even and all odd digits from that number as a single string like in the examples below. 


## **05. Palindrome Integers**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/05_palindrome_integers.py)
A palindrome is a number which reads the same backward as forward, such as 323 or 1001. Write a function which receives a list of positive integers and checks if each integer is a palindrome or not. Print the results on the console.  
The input will be a single string containing the numbers separated by comma and space ", "


## **06. Password Validator**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/06_password_validator.py)
Write a function that checks if a given password is valid. Password validations are:  
•	The length should be 6 - 10 characters (inclusive)  
•	It should consists only letters and digits  
•	It should have at least 2 digits   
If a password is valid print "Password is valid".  
If it is NOT valid, for every unfulfilled rule print a message:  
•	"Password must be between 6 and 10 characters"  
•	"Password must consist only of letters and digits"  
•	"Password must have at least 2 digits"  


## **07. Perfect Number**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/07_perfect_number.py)
Write a function that receives an integer number and returns if this number is perfect or NOT.  
A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its positive divisors excluding the number itself (also known as its aliquot sum).


## **08. * Loading Bar**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/08_loading_bar.py)
You will receive a single integer number between 0 and 100 which is divided with 10 without residue (0, 10, 20, 30...).  
Your task is to create a function that visualizes a loading bar depending on that number you have received in the input.


## **09. * Factorial Division**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/09_factorial_division.py)
Write a function that receives two integer numbers. Calculate factorial of each number. Divide the first result by the second and print the division formatted to the second decimal point.


## **10. *Array Manipulator**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/10_array_manipulation.py)
Trifon has finally become a junior developer and has received his first task. It's about manipulating an array of integers. He is not quite happy about it, since he hates manipulating arrays. They are going to pay him a lot of money, though, and he is willing to give somebody half of it if to help him do his job. You, on the other hand, love arrays (and money) so you decide to try your luck.  
The array may be manipulated by one of the following commands  
•	exchange {index} – splits the array after the given index, and exchanges the places of the two resulting sub-arrays. E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]  
o	If the index is outside the boundaries of the array, print "Invalid index" (negative indexation must be considered as invalid)  
•	max even/odd– returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4  
•	min even/odd – returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3  
o	If there are two or more equal min/max elements, return the index of the rightmost one  
o	If a min/max even/odd element cannot be found, print "No matches"  
•	first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]  
•	last {count} even/odd – returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]  
o	If the count is greater than the array length, print "Invalid count"  
o	If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty array "[]"  
•	end – stop taking input and print the final state of the array  
*Input*  
•	The input data should be read from the console.  
•	On the first line, the initial array is received as a line of integers, separated by a single space  
•	On the next lines, until the command "end" is received, you will receive the array manipulation commands   
•	The input data will always be valid and in the format described. There is no need to check it explicitly.  
*Output*  
•	The output should be printed on the console.  
•	On a separate line, print the output of the corresponding command  
•	On the last line, print the final array in square brackets with its elements separated by a comma and a space    
•	See the examples below to get a better understanding of your task  
*Constraints*  
•	The number of input lines will be in the range [2 … 50].   
•	The array elements will be integers in the range [0 … 1000].  
•	The number of elements will be in the range [1 .. 50]  
•	The split index will be an integer in the range [-231 … 231 – 1]  
•	first/last count will be an integer in the range [1 … 231 – 1]  
•	There will not be redundant whitespace anywhere in the input  
•	Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.


## **01. More Exercises - Data Types**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/more_ex_01_data_types.py)
Write a program that, depending on the first line of the input, reads an int, double or string.  
•	If the data type is int, multiply the number by 2.  
•	If the data type is real, multiply the number by 1.5 and format it to the second decimal point.  
•	If the data type is string, surround the input with "$".  
Print the result on the console.


## **02. More Exercises -	Center Point**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/more_ex_02_center_point.py)
You are given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2 and Y2. Create a method that prints the point that is closest to the center of the coordinate system (0, 0) in the format (X, Y). If the points are on a same distance from the center, print only the first one. The resulting coordinates must be formated to the lowest integer


## **03. More Exercises -	Longer Line**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/more_ex_03_longer_line.py)
You are given the coordinates of four points in the 2D plane. The first and the second pair of points form two different lines. Print the longer line in format "(X1, Y1)(X2, Y2)" starting with the point that is closer to the center of the coordinate system (0, 0) (You can reuse the method that you wrote for the previous problem). If the lines are of equal length, print only the first one. The resulting coordinates must be formated to the lowest integer.


## **04. More Exercises - Tribonacci Sequene**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/more_ex_04_tribonacci_sequence.py)
In the "Tribonacci" sequence, every number is formed by the sum of the previous 3.  
You are given a number num. Write a program that prints num numbers from the Tribonacci sequence, each on a new line, starting from 1. The input comes as a parameter named num. The value num will always be positive integer.


## **05.More Exercises - Multiplication Sign**  [Solution](https://github.com/elenaborisova/Python-Fundamentals/blob/main/08.%20Functions%20-%20Exercise/more_ex_05_multiplication_sign.py)
You are given a number num1, num2 and num3. Write a program that finds if num1 * num2 * num3 (the product) is negative, positive or zero. Try to do this WITHOUT multiplying the 3 numbers.
