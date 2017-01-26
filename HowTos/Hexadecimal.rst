=============
Hexadecimal
=============
   Hexadecimal, also known as base 16 allows easy understanding bit representation but with 75% the length reduction. Each Hex character represents  an array of 4 bits. To denote the presence of a hex number, a notation is used before the beginning "0x".

Examples are::
     0x2220, 0x01, 0x0, 0xAB

Importance
===========
1. Hexadecimal is used in many CAN analyzation tools.
2. An object dictionary is built around the reference of Hexadecimal IDs
3. The routines and methods require the use of hex in interpreting Can-Open

Basis
=====
In base ten there are 10 symbols which represent our number system. In Hexadecimal there are 16 symbols.

These symbols are:
::

      0  1  2   3    4   5  6  7  8  9  a b  c  d  e  f

Notice that we run out of numbers to represent 11-15 and begin to use letters.

Constructing Hex Numbers
-------------------------

What if we have a number bigger then 15(F) we want to represent? Well lets look at our number system for comparison.
When we count up to 9, we simply start over and now add what we call the "tens digit"

therefore we get:
::

    9, *10* , 11 , 12 , 13 , 14... 99, *100*

The pattern is quite similar to the way we write hex bigger then F.

So for hex bigger then F:
::

    Hex : E,F, *10*, 11, 12

    Decimal: 14,15,16,17,18

Note: do not get confused with  11 hex and 11 decimal.

Now we can see that 26 in hex is 1A.

Conversions
-----------
It is important to understand simple hex to decimal and hex to binary conversions.

A hex symbol can represent 4 bits.

For example:
::

   1110 ---> E in Hex ---> 14 in decimal

Most of can notation is very byte manipulated intensive. Representing a byte is very easy as using two hex symbols

for example:
::

   1110 1111   --> 0xEF  --> 239 in decimal
   0000 0011  --> 0x03 ---> 3 in decimal


Tips
 * Group a binary string in 4 bit length segments to easily covert to hexadecimal

This is as far as we will go with hexadecimal conversion and construction.
