#code.py
''' 
This module provides functions for creating a series of project folders. 

Purpose: Reusable Module for Analytics Projects for NWMSU CSIS
Description: This module provides a byline for my analytics projects. 
Author: Data-Git-Hub
Module: datafun-02-project-setup/code.py

TODO: Change the module name in this opening docstring
'''

#####################################
# Import Modules
#####################################

import pathlib
import stellar_analytics_utils
# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

#####################################
# Declare Global Variables
#####################################


#####################################
# Define global functions (reusable instructions)
#####################################


#####################################
# Define main() function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually four spaces)

    This is used in best practices when coding.
    '''
    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script, then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
