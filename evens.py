def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """

    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])
        
        return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("A list was not passed into the function")
    return None


# When the test was run this function call was also run.
# Let’s prevent that from happening by making  the following change.
# So what is this doing? To keep it  simple, when Python runs a file directly,  
# it names it __main__ and any code  beneath the if statement will only be run  
# if the name of the file is __main__.
# So when we run the test file it will have  the name __main__ and this code won't run.  
# But when we run this file it will have the  name __main__ and it will run this code.


if __name__ == "__main__":
    print(even_number_of_evens(5))