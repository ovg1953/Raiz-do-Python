# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:29:55 2020
@author: ovgalva

Iniciando com o Tutorial da Python.org

Tópico s Vistos:
   > Using the Python Interpreter <
   > An Informal Itroduction to Python <
   
1) In interactive mode, the last printed expression is assigned to
   the variable _. This means that when you are using Python as a desk
   calculator, it is somewhat easier to continue calculations
   
   tax = 12.5 / 100
   price = 100.50
   price * tax
   price + _
   round(_, 2)

2) If you don’t want characters prefaced by \ to be interpreted as special
   characters, you can use raw strings by adding an r before the first quote:
    
   print('C:\some\name')  # here \n means newline!
   print(r'C:\some\name')  # note the r before the quote
   
3) String literals can span multiple lines. One way is using 
   triple-quotes: """...""" or '''...'''. End of lines are automatically
   included in the string, but it’s possible to prevent this by adding
   a \ at the end of the line. The following example:   
       
   print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

4) Strings can be concatenated (glued together) with the + operator, 
   and repeated with *:
       
   >>> # 3 times 'un', followed by 'ium'
   >>> 3 * 'un' + 'ium'
   'unununium'
   
   Two or more string literals (i.e. the ones enclosed between quotes)
   next to each other are automatically concatenated.
   
   'Py' 'thon'
   
   This feature is particularly useful when you want to break long strings:
       
   text = ('Put several strings within parentheses '
...         'to have them joined together.')
   (ATENÇÂO; só funciona com literais!!!)
   
5) Strings can be indexed (subscripted), with the first character
   having index 0. There is no separate character type; a character is
   simply a string of size one:
       
   Note that since -0 is the same as 0, negative indices start from -1.

   In addition to indexing, slicing is also supported. While indexing is used
   to obtain individual characters, slicing allows you to obtain substring.
   Exemplos: 
       
   word = 'Python'
   word[0]  # character in position 0
   word[5]  # character in position 5
   word[-1] # last character
   word[-2] # second-last character
   word[-6] # First character
   word[0:2]  # characters from position 0 (included) to 2 (excluded)
   word[2:5]  # characters from position 2 (included) to 5 (excluded)

See also
Text Sequence Type — str
Strings are examples of sequence types, and support the common operations supported
by such types.

String Methods
Strings support a large number of methods for basic transformations and searching.

Formatted string literals
String literals that have embedded expressions.

Format String Syntax
Information about string formatting with str.format().

printf-style String Formatting
The old formatting operations invoked when strings are the left operand of
the % operator are described in more detail here.
   
   
"""

