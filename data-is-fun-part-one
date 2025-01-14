# Python Code Reusable Module
"""
Module: data-is-fun-part-(number).py

Purpose: Reusable Module for Analytics Projects for NWMSU CSIS
Description: This module provides a byline for my analytics projects. 
Author: Data-Git-Hub

TODO: Change the module name in this opening docstring
"""

#####################################
# Import Modules
#####################################

import statistics

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your boolean variable
free_shipping: bool = True
military_discount: bool = True

# declare an integer variable 
# TODO: Add or replace this with your integer variable
years_in_operation: int = 90

# declare a floating point variable
# TODO: Add or replace this with your floating point variable
average_client_satisfaction_reviews_io: float = 1.3
average_deliver_time_in_days: float = 7.6
military_precentage: float = 0.10

# declare a list of strings
# TODO: Add or replace this with your list  
product_type_offered: list = ["Hand Rolled Cigars", "Machine Made Cigars", "Sampler Cigars"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your numeric list  
client_rating_score_reviews_io: list = [1.0, 1.0, 1.5, 2.0, 1.5, 3.0, 1.0, 1.0, 1.0, 1.0, 5.0, 1.0, 1.0, 1.5, 1.5, 2.0, 1.0, 1.0, 1.0]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your numeric list
min_score: float = min(client_rating_score_reviews_io)  
max_score: float = max(client_rating_score_reviews_io)  
mean_score: float = statistics.mean(client_rating_score_reviews_io)  
stdev_score: float = statistics.stdev(client_rating_score_reviews_io)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Redacted Online Cigar Online Storefront Analytics: Delivering Professional Insights
---------------------------------------------------------
Free Shipping:                                              {free_shipping}
Military Discount:                                          {military_discount}
Military Discount Percentage:                               {military_precentage:.0%}
Years in Operation:                                         {years_in_operation} years
Products Offered:                                           {product_type_offered}
Client Satisfaction Scores Average Per http://review.io:    {average_client_satisfaction_reviews_io}
Average Delivery Time:                                      {average_deliver_time_in_days}
Minimum Satisfaction Score:                                 {min_score}
Maximum Satisfaction Score:                                 {max_score}
Mean Satisfaction Score:                                    {mean_score:.2f}
Standard Deviation of Satisfaction Scores:                  {stdev_score:.2f}
"""

#####################################
# Define global functions (reusable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing required inside the parentheses.
    Everything after the colon must be indented consistently (usually four spaces)
    '''
    return byline


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
