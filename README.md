# LSEG-Coding
Pre-Interview Coding Challenge
This program is like a dictionary explorer:

First, it asks you to type a dictionary (like a map of boxes inside boxes).
Example:

{"a":{"b":{"c":"d"}}}


Then, it asks you for a path (like directions) using slashes /.
Example:

a/b/c


The program then follows the path step by step:

Look inside "a"

Then inside "b"

Then inside "c"

Finds "d"

Finally, it prints the value it found.

If the path is wrong or empty, it shows a friendly error message instead of giving you None.