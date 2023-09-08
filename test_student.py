import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):

# Fortunately,  Unittest provides another method we can use for  
# this particular use case called setUpClass.  We can also use the tearDownClass method  
# to destroy a test database, for instance, and this  method will be run once at the end of our tests.
# As we don’t have a particular use for  it in our test, I’ll simply show you  
# how to set up these methods and add print  statements so we can see when they are run.
#         At the top of our test_student file, I’ll go  ahead and add setUpClass with a parameter of ‘cls’  
# instead of ‘self’. I do this as setUpClass is  a class method that affects the class itself  
# instead of only an instance of the  class as the ‘self’ parameter would.  
# Let’s add a print statement inside our method that  will print “setUpClass” to the terminal when run.  
# There is one more thing we need to  add to make this a class method,  
# and that is the @classmethod  decorator. Just to reiterate,  
# adding the @classmethod decorator to a method  and passing ‘cls’ as a method parameter  
# will make it a class method which acts on the  class instead of an instance of the class.
    @classmethod
    def setUpClass(cls):
        print("set up class")

#         Since the setUp method runs before each test  method, it would save us code repetition if we  
# could define our student instance there so it can  be available in each test method when it’s run.
# Let’s go ahead and create the setUp method  at the beginning of our TestStudent class  
# and add a reference to “self”. Next, I’ll create  a student instance as an instance variable,  
# so it needs to be prepended with the “self”  keyword
    def setUp(self):
        print("setup")
        self.student = Student("John", "Doe")

    @classmethod
    def tearDownClass(cls):
        print("tear down Class")


#         Whereas the setUp method can be used to  create temporary files and folders or set up  
# a database connection during tests, the tearDown  method would be used to remove temporary files  
# or folders or close a connection to a database. As  we don’t need any of that functionality, adding a  
# simple statement to print “tearDown” will allow  us to see when it is called behind the scenes.
    def tearDown(self):
        print("tear down")

    
    def test_full_name(self):
#         As mentioned earlier, we need to  create an instance of the Student class  
# in order to test it. I’ll name  the instance student and make  
# sure to pass in the first_name and last_name  arguments of ‘John’ and ‘Doe’ respectively.
        # student = Student("John", "Doe")
#         We can now use an assertEqual on the  student instance to see whether calling  
# the full_name method on it returns  the expected value.   
# In our case, the first_name and last_name  properties separated by a space.
# If we now run our test, we can see that it  passes. Great! That’s our first test done,  
# so we’re well on our way towards extending  the scope of our tests and Student class.
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")
    
#     In this video, we’ll start using Test-Driven Development and create a test for a function
# called alert_santa that  will change the naughty_list property to True.
    def test_alert_santa(self):
        # student = Student("John", "Doe")
        print("test_alert_santa")
#         We’ve been using assertEqual methods up till now,  
# but we’ll use a different assert  for this test called assertTrue.
# The reason being that we know that  we want the alert_santa method to set  
# the value of the naughty_list  property to True when called.
        self.student.alert_santa()

#         Note that we don’t pass a second  argument to assertTrue as it’s not  
# comparing two values but simply checking  whether an expression or value is True.
        self.assertTrue(self.student.naughty_list)


    def test_email(self):
        # student = Student("John", "Doe")
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")



# I’ll store the current value for  the student instance in a variable  
# called old_end_date. The variable name here isn’t  important, but I name it this way for clarity.
# Next, I’ll call the apply_extention method on  student and pass in an argument of five for  
# the number of days required. With that in place,  I’ll call assertEqual and test whether student’s  
# end_date is equal to the old date plus a timedelta  of five days.
    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))
        """
        The method below is also great!  But keep in mid that  it will
        only be correct if a student has received 1 extenstion.  If 
        they receive a second - it would return false

        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, self.student._start_date + timedelta(days=370))
        """
    
    def test_course_schedule_success(self):
#         We know that we want to mock a  get request in the student module,  
# so we can write with patch(‘student.requests.get’)  as mocked_get: to set our context manager.   
# This creates an object called ‘mocked_get’ which we  can use to test the get request functionality. 
# Note that we’re importing the student class  at the top of the file and that’s why we use  
# student.requests.get to access it. 
        with patch("student.requests.get") as mocked_get:
#             Since we’re testing a successful request,  which values are we interested in if we  
# look at the course_schedule method? Pause the  video and think about it before continuing.  
# Well, we are interested in whether the  response is ‘ok’ and the response text.  
# We can set these values in our mocked_get  object as if it were a successful request.  
# In order to do so, I’ll use  mocked_get.return_value.ok equals True  
# as well as setting the response text to mock  something being returned from the API.   
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

# With that in place, let’s get  the student’s course schedule  
# and store it in a variable called schedule.
# We can now use assertEqual to  compare the variable “schedule”,  
# which should hold the returned response text for  a successful call, with the string “Success”.
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")
        

    def test_course_schedule_failed(self):
        """
        In the path "student" comes from the name of the file student.py
        If you have named the file something else - it will need to match
        eg, students.py would need "students.requests.get"
        """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")





if __name__ == "__main__":
    unittest.main()