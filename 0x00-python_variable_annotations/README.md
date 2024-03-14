# 0x00. Python - Variable Annotations
## Learning Objectives
1) Type annotations in Python 3
2) How you can use type annotations to specify function signatures and variable types
3) Duck typing
4) How to validate your code with mypy

## Learning
Type annotations are comments in python 3 that provide extra information about data types and the return types of functions. They are optional but could improve code readability. 
```
from typing import List

def calculate_average(numbers: List[float]) -> float:
    """Calculates the average of a list of numbers."""
    total = sum(numbers)
    return total / len(numbers)
```
The common type annotations are:
***
***
int: integer data type
float: floating-point number
str: string
bool: boolean (true or false)
list: list data type
tuple: tuple data type
dict: dictionary data type
None: absence of value
***
***

## Requirements
1) Allowed editors: vi, vim, emacs
2) All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3
3) All your files should end with a new line
4) The first line of all your files should be exactly ‘#!/usr/bin/env python3’
5) A readme.md file, at the root of the folder of the project, is mandatory
6) Your code should use the pycodestyle style
7) All your files must be executable
8) The length of your files will be tested using wc
9) All your modules should have a documentation
10) All your classes should have a documentation
11) All your functions (inside and outside a class) should have documentation.
12 A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks
### 0. Basic annotations - add
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

### 1. Basic annotations - concat
Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string

### 2. Basic annotations - floor
Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.

### 3. Basic annotations - to string
Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.

### 4. Define variables
Define and annotate the following variables with the specified values:
a, an integer with a value of 1
pi, a float with a value of 3.14
i_understand_annotations, a boolean with a value of True
school, a string with a value of ‘Holberton’

### 5. Complex types - list of floats
Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.

### 6. Complex types - mixed list
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.

### 7. Complex types - string and int/float to tuple
Write a type-annotated function to_kv that takes as string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.

### 8. Complex types - functions
Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

### 9. Let's duck type an iterable object
Annotate the below function’s parameters and return values with the appropriate types
```
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

### 10. Duck typing - first element of a sequence
Augment the following code with the correct duck-typed annotations:
```
# The types of the elements of the input are not known
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
```

### 11. More involved type annotations
Given the parameters and the return values, add type annotations to the function
Hint: look into TypeVar
```
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
```

### 12. Type Checking
Use mypy to validate the following piece of code and apply any necessary changes.
```
def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
```
