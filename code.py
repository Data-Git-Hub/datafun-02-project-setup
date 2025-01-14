#code.py
''' 
This module provides functions for creating a series of project folders. 

Module: code.py
Purpose: Reusable Module for Analytics Projects for NWMSU CSIS
Description: This module provides a byline for my analytics projects. 
Author: Data-Git-Hub
'''

#####################################
# Import Modules
#####################################

# Import modules from standard library as need
import pathlib

# Import local modules
import data_is_fun_part_one

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

#####################################
# Declare Global Variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define global functions (reusable instructions)
#####################################

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
        # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

 # Check if start_year is less than or equal to end_year
    if start_year > end_year:
        print("ERROR: start_year must be less than or equal to end_year.")
        return

# Loop through the range of years and create a folder for each year
    for year in range(start_year, end_year + 1):
        year_folder = data_path.joinpath(str(year))
        try:
            year_folder.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
            print(f"Folder created: {year_folder}")
        except Exception as e:
            print(f"ERROR: Could not create folder {year_folder}. Reason: {e}")

#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list) -> None:
 '''
    Create folders from a list of folder names.

    Arguments:
    folder_list -- A list of folder names to be created.
    '''
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}")

    # Iterate through the folder list and create each folder
    for folder_name in folder_list:
        folder_path = data_path.joinpath(folder_name)
        try:
            folder_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
            print(f"Folder created: {folder_path}")
        except Exception as e:
            print(f"ERROR: Could not create folder {folder_path}. Reason: {e}")

#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
'''
    Create prefixed folders by combining a list of folder names with a specified prefix.

    Arguments:
    folder_list -- A list of folder names to be prefixed and created.
    prefix -- The prefix to prepend to each folder name.
    '''
    # Log the function call and its arguments
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")

    # Iterate through the folder list, apply the prefix, and create folders
    for folder_name in folder_list:
        prefixed_name = f"{prefix}{folder_name}"
        folder_path = data_path.joinpath(prefixed_name)
        try:
            folder_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
            print(f"Folder created: {folder_path}")
        except Exception as e:
            print(f"ERROR: Could not create folder {folder_path}. Reason: {e}")

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    # TODO: Implement this function professionally and remove the temporary pass
    pass

#####################################
# Define main() function for this module.
#####################################

def main() -> None:
    ''' Main function of module. '''

    # Start of main execution
    print("------------------------------------------------- ")
    print("            Starting........ Script")
    print("--------------------------------------------------")
    
    # Print get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    # print(f"Byline: {case_utils.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # TODO: Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = ["North America", "South America", "Europe", "Asia", "Africa", "Oceania", "Middle East"]
    # Uncomment this line after you've added your custom logic
    # create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)
    
        # End of main execution
    print("------------------------------------------------- ")
    print("            Ending........ Script")
    print("--------------------------------------------------")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script, then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
