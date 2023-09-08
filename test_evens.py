import unittest
from evens import even_number_of_evens


# We are now ready to create a test case and we'll do so by creating a class named TestEvens.
# To make use of Unittest’s functionality,  
# our class needs to inherit  from the unittest.TestCase class.
# I'll also add a pass statement and unittest.main. So we can run the file without specifying the unit test module.
# And when we run the code using the command python3  test_evens.py everything works fine, and we are  
class TestEvens(unittest.TestCase):

    """
    So let's create a basic test that tests  whether if our function returns True.   
    It will be a method and needs to start with the word test.  If we dont start the method name with the word test,
    it will be ignored and won't run, when we run the test file.    
    And as we are in a class we need to pass in the self keyword.
    """
    # def test_functions_returns_True(self):
    """
        In here, we can create either a  single assert or many asserts,  
        for now we will just create one  just to show you how things work.
        So I ll assertTrue that calling  the function even_number_of_evens  
        with an empty list returns True. 
        """
        # self.assertTrue(even_number_of_evens([]))
        
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)
        """
            Inside our test, we write our assert  and I will use the assertRaises method.
This will call the assertRaises method  from TestCase and when the test is run  
it checks to see if a TypeError is raised  when the function is called with the value  
4. This should fail, as our function  at the moment is set to return None.
        """
        
        
        """
        The next test should test our  function returns False if an  
empty list is passed in, so I’ll create  a new test named test_values_in_list,  
and will use this code block  for the next few assertions.
I need to write an assertion  that checks if an empty list  
has been passed in and should be expecting False.
For this test I will use the assertEqual  method passing in the function with an  
empty list as an argument, and  the expected return of False.
        """
    
    
    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)



if __name__ == "__main__":
    unittest.main()