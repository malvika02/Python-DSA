PYTHON

1. Python is a general purpose,high level and interpreted programming language.
2. It is an interactive programming language.
3. Simple syntax
4. Python was developed by Guido Van Rossum in 1991 at The National Research Institute for Mathematics and Computer Science in the Netherlands.

Execution


(Python Program)first.py---->(Python compiled)first.pyc---->10101010---->COMPUTER
                                                                    
   Source Code ----> Byte Code ----> Machine Code ----> Computer    

                        STEPS OF EXECUTION OF A PYTHON PROGRAM

NOTE:
When we compile a python program, we cannot see .pyc file produced by python compiler and the machine code generated by Pyhton Virtual Machine(PVM). This is done internally in the memory.

We can use python compiler to compile the program as:
~python first.py
(python is the command to call the python compiler)

Also, to create .pyc file separately from the source code, we can use the following code: 
~python -m py_compile first.py

To interpret the .pyc file using PVM, the python compiler can be called using:
~python first.cpython-38.pyc
