11/28/21  
IT FDN 110 A 
Matt Fuller
# Assignment 07 Knowledge Document

## Introduction
I had never interacted with data in a binary file prior to this lesson. The concept of “obscurity” is interesting and I am curious about the practical application of using this type of file. It was also interesting making the mental shift from working with text file methods to pickle methods.


## Exception Handling
The first example of Exception Handling uses “Try-Except”. Our code is separated into what we would like to happen, the “Try” block, and what we want to happen if an exception occurs, the “Except” block. An example below is used when creating a loop to repeatedly load data from our binary file. The while loop will continually *try* to perform the code in the “Try” block until an *exception occurs*. At this point the code in the “Except” block is executed. We could even tell the “Except” block to only care about specific exceptions, for example only executing if the error type is the “EOFError”.

![EOFError](/../main/assets/images/EFError.png)
![ExceptionHandling1.png](/../main/assets/images/ExceptionHandling1.png)  

There are also other options to utilize this type of [exception handling](https://www.w3schools.in/python-tutorial/exception-handling/):

![Exception Handling Option](/../main/assets/images/TryExceptExamples.png)  

Here we are using `if`/`elif` statements to check if the user input is numeric and avoid errors when performing future math operations. If the input is not numeric we `raise` an `exception`, with optional message that is displayed to the user.

![ExceptionHadnling2.png](/../main/assets/images/ExceptionHadnling2.png)  

Similarly, we can `raise` an `exception` with a call to a custom error class that we created elsewhere, `PerfectPickleError()`. In this example the class takes in an `exception` as a argument and has one method that returns a string containing an error message we have written that makes it more clear to the user why the code did not execute as expected.  

![ExceptionHandling3.png](/../main/assets/images/ExceptionHandling3.png)
![ExceptionHandling4.png](/../main/assets/images/ExceptionHandling4.png)

## Pickling
According to the [official Python documentation](https://docs.python.org/3/library/pickle.html#data-stream-format),
> Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.
     
In our case this means that we are using the “Pickle” Python library to move data back and forth from string data (the “Python object hierarchy”) to a .dat binary file (the “byte stream”). Examples of this are seen in the following code.
`pickle.load()` takes in as an argument an open file object and loads one line of data from it, `pickle.dump()` reverses it and writes data to one line in the file. This is sometimes described as “serializing” and “deserializing”.
One advantage of serializing data is to make it more “obscure” as well as more easily transport it across a network. However, [one article](https://www.synopsys.com/blogs/software-security/python-pickling/) explains that this also presents a significant draw back in that the “pickled” data cannot be verified before it is “unpickled”, potentially being malicious if coming from an unverified source.3

## Summary
It was good practice to work with binary files and think more about error handling. Expanding one’s knowledge of file types and how they can be utilized effectively is likely a handy skill moving forward. Error handling is something I felt I needed more practice with as it seems like an important way to improve application usability and I after this exercise I feel more confident using it in different ways.
Links
https://www.w3schools.in/python-tutorial/exception-handling/ https://www.freecodecamp.org/news/exception-handling-python/
https://stackoverflow.com/questions/41600577/iterating-through-a-list-of-objects-which-is- loaded-by-pickle
https://www.synopsys.com/blogs/software-security/python-pickling/ https://docs.python.org/3/library/pickle.html#data-stream-format

## Execution Verification
![PyCharm Running Code.png](/../main/assets/images/PyCharmRunningCode.png)
![Terminal Running Code.png](/../main/assets/images/TerminalRunningCode.png)
