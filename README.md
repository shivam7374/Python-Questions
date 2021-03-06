# Python-Questions
Various collection of questions from different topics in PYTHON 
-------------------------------------------------------------------------------------------------------------

Assignment 1 
<br>
Q1) Python Program to find GCD of Two Numbers
<br>
Q2) Python program to check if the number provided by the user is an Armstrong number or not
<br>
Q3) SUM OF SERIES OF N/N+1
<br>
Q4) CREATE A LIST OF AUTO PARTS ALONG WITH NAME AND PRICE

-------------------------------------------------------------------------------------------------------------

Assignment 2
<br>1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.
<br>Sample String : 'a1resource'
<br>Expected Result : 'a1ce'
<br>Sample String : 'a1'
<br>Expected Result : 'a1a1'
<br>Sample String : ' a'
<br>Expected Result : Empty String
<br>2. Write a Python program to get a string from a given string where all occurrences of its first char have
been changed to '$', except the first char itself.
<br>Sample String : 'restart'
<br>Expected Result : 'resta$t'
<br>3. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given
string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
resulting string.
<br>Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
<br>Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
<br>4. Write a Python function to insert a string in the middle of a string.
<br>Sample function and result :
<br>insert_sting_middle('[[]]', 'Python') -> [[Python]]
<br>insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
<br>5. Write a Python program to sort a string lexicographically.
<br>6. Write a Python program to count repeated characters in a string.
<br>Sample string: 'thequickbrownfoxjumpsoverthelazydog'
<br>Expected output :
<br>o 4
<br>e 3
<br>u 2
<br>h 2
<br>r 2
<br>t 2
<br>7. Write a Python function that prints out the first ‘n’ rows of Pascal's triangle. ‘n’ is user input.
<br>8. Write a Python function that accepts a hyphen-separated sequence of words as input and prints the
words in a hyphen-separated sequence after sorting them alphabetically.
<br>Sample Items : green-red-yellow-black-white
<br>Expected Result : black-green-red-white-yellow
<br>9. Write a Python function to merge two sorted arrays.
<br>Sample Items :
<br>m=[1, 4, 8]
<br>n=[2, 3, 7]
<br>Expected Output: mn=[1, 2, 3, 4, 7, 8]
<br>10. Write a Python function that accepts a string and calculate the number of upper case letters and
lower case letters.
<br>Sample String : 'The quick Brow Fox'
<br>Expected Output :
<br>No. of Upper case characters : 3
<br>No. of Lower case Characters : 12
<br>11. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as
its input and print the numbers that are divisible by 5 in a comma separated sequence.
<br>Sample Data : 0100,0011,1010,1001,1100,1001
<br>Expected Output : 1010
<br>12. Write a Python program to insert a new item before the second element in an existing array.
<br>13. Write a Python program to print alphabet pattern 'R'.
<br>Expected Output:
<br>****
<br>*   *
<br>*   *
<br>****
<br>**
<br>* *
<br>*  *
<br>14. Write a Python program to get the number of occurrences of a specified element in an array.
<br>15. Write a Python program to remove a specified item using the index from an array.
<br>16. Write a Python program to convert an array to an ordinary list with the same items.
<br>17. Write a Python program to remove duplicates from a list of lists.
<br>Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
<br>New List : [[10, 20], [30, 56, 25], [33], [40]]
<br>18. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
<br>Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
<br>Expected Output: [10, 11, 12]
<br>19. Write a Python program to insert a given string at the beginning of all items in a list.
<br>Sample list : [1,2,3,4], string : emp
<br>Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
<br>20. Write a Python program to compute the similarity between two lists.
<br>Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
<br>Expected Output:
<br>Color1-Color2: ['white', 'orange', 'red']
<br>Color2-Color1: ['black', 'yellow']
<br>21. Write a Python program to split a list every Nth element.
<br>Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
<br>Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
<br>22. Write a Python program to convert a list of multiple integers into a single integer.
<br>Sample list: [11, 33, 50]
<br>Expected Output: 113350
<br>23. Write a Python program to iterate over two lists simultaneously.
<br>24. Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
<br>Sample list : ['p', 'q']
<br>n =5
<br>Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

-------------------------------------------------------------------------------------------------------------

Assignment 3
<br>1. Write a Python program to match key values in two dictionaries.
<br>Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
<br>Expected output: key1: 1 is present in both x and y.
<br>2. Write a Python program to create a dictionary from two lists without losing duplicate values. 
<br>Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
<br>Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 
'Class-V': {1}})
<br>3. Write a Python program to replace dictionary values with their sum.
<br>Example: Input: {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI': 82},
 {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
 {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
 <br>Output: [{'subject': 'math', 'id': 1, 'V+VI': 76.0}, 
 {'subject': 'math', 'id': 2, 'V+VI': 73.5} 
 {'subject': 'math', 'id': 3, 'V+VI': 80.5}]
<br>4. Write a Python program to sort a tuple by its float element. 
<br>Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
<br>Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] 
<br>5. Write a Python program to remove an empty tuple(s) from a list of tuples.
<br>Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
<br>Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd'] 
<br>6. Write a Python program to convert a list of tuples into a dictionary.
<br>Example: Input: ((2, "w"),(3, "r"))
<br> Output: {'w': 2, 'r': 3}
<br>7. Write a Python program to count the elements in a list until an element is a tuple.
<br>Example: Input: [10,20,30,(10,20),40]
<br> Output: 3
<br>8. Write a Python program to find maximum and the minimum value in a set.
<br>Example: Input: ([5, 10, 3, 15, 2, 20])
<br>Output: Maximum value: 20, Minimum value: 2
<br>9. Write a Python program to create set difference, union, and intersection of sets.
<br>Example: Input: set(["green", "blue"]), set(["blue", "yellow"])
 <br>Output: Difference: {'blue'}, {'green'}, Union: {'yellow', 'green', 'blue'} 
 Intersection: {'blue'}
<br>10. Write a Python program to make a chain of function decorators (bold, italic, underline etc.).
<br>Example: Input: hello world 
<br>Output: hello world
<br>12. Write a Python program of recursion list sum. 
<br>Test Data: [1, 2, [3,4], [5,6]]
<br>Expected Result: 21
<br>13. Write a Python program for binary search.
<br>Example: Enter the sorted list of numbers: 3 5 10 12 15 20
<br> The number to search for: 12
 <br>12 was found at index 3.
<br>14. Write a Python program to sort a list of elements using the bubble sort algorithm.
<br>Example: Sample Data: [14, 46, 43, 27, 57, 41, 45, 21, 70]
<br>Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]
<br>15. Write a Python program to sort a list of elements using the selection sort algorithm.
<br>Example: Sample Data: [14, 46, 43, 27, 57, 41, 45, 21, 70]
<br>Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]
<br>16. Write a Python program to sort a list of elements using the merge sort algorithm.
<br>Example: Split Sample Data: [14, 46, 43, 27, 57, 41, 45, 21, 70]
<br>Merge and Sort(Expected Result): [14, 21, 27, 41, 43, 45, 46, 57, 70] 
<br>17. Write a Python program using functions that asks the user for a long string containing multiple 
words. Print back to the user the same string, except with the words in backwards order. 
<br>For example, say I type the string: My name is Michele; 
<br>Then I would see the string: Michele is 
name My; shown back to me.
<br>18. Define a function reverse() that computes the reversal of a string. 
<br>For example, reverse(“I am testing”) should return the string ”gnitset ma I”.
<br>19. Write a Python program to find the available built-in modules. 
<br>Example: math, random, uuid, sys, syslog etc. 
<br>20. 12Write a Python program to get the size of an object in bytes by using module “sys”.
<br>Example: Memory size of 'one' = 52 bytes
<br> Memory size of 'four' = 53 bytes
<br> Memory size of 'three' = 54 bytes
<br>21. Using the module random and time in python generate a random date between given start and end 
dates.
<br>Example: Printing random date between 1/1/2016 and 3/23/2018
<br> Random Date = 02/25/2016
<br>22. Generate three random password string of length 10 with special characters, letters, and digits by 
using python modules (random and string).
<br>Example: First Random String: yrjmcyi^VS
<br> Second Random String: |}Hd]!^>~l
<br> Third Random String: 3^a93@x=|Z
<br>23. Write a python code using module “uuid” to generate universally unique secure randon string id of 
length 8.
<br>Example: random string using a UUID module is: 9C8E13FF
<br> random string using a UUID module is: 9cb3561d
<br>24. Write a python code using module “random” to generate a 100 Lottery tickets and pick two lucky 
tickets from it as a winner.
<br>Note: You must adhere to the following conditions:
<br> 1. Lottery number must be 10 digits long.
 <br>2. All 100 ticket number must be unique.
<br>Example: Creating 100 random lottery tickets
 <br>Lucky 2 lottery tickets are [7184805696, 7380986204]
<br>

-------------------------------------------------------------------------------------------------------------

