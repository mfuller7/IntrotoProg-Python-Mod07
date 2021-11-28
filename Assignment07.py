import pickle

# Data

pickleFile = 'ilovepickles.dat'
pickle_ratings = []
pickleName = ''
pickleTaste = ''
pickleColor = ''
pickleSmell = ''


# Processing

# Example of pickling 1 (read from binary file), error handling 1 (Try-Except)
def pickle_reader(file_name):
    data = []

    with open(file_name, 'rb') as file:
        while True:
            try:
                # It will TRY to run the code in the TRY block...
                data.append(pickle.load(file))
                # pickle.load() function loads one line data from file
            except:
                # EXCEPT when it reaches the end of the file, with nothing left to process, where it will
                # raise an "EOFError" exception and perform the code in the EXCEPT block
                break

    print('Pickle files loaded!')
    return data

def pickle_saver(file_name, list_of_data):
    with open(file_name, 'ab') as file:
        for each in list_of_data:
            pickle.dump(each, file)


def pickle_rater():
    try:
        pickleName = input('Enter pickle variety: ')
        pickleTaste = input('Taste rating (1-10): ')
        pickleColor = input('Color rating (1-10): ')
        pickleSmell = input('Smell rating (1-10): ')

        # CUSTOM EXCEPTIONS
        if pickleTaste.isalpha() or pickleTaste.isalpha() or pickleTaste.isalpha():
            # Checking that entered values are numeric, raise exception if not
            raise Exception('ERROR! Please enter numeric pickle rating (1-10). No rating recorded.')
        elif ((int(pickleSmell) + int(pickleColor) + int(pickleTaste)) / 3) != 10 :
            # Check to see that user fully appreciates pickles, raises custom exception if not
            raise PerfectPickleError()
        else:
            overallPickleScore = (int(pickleSmell) + int(pickleColor) + int(pickleTaste)) / 3
            print('Success! Rating added.\n')
            return [pickleName, overallPickleScore]
    except Exception as e:
        print(e)


class PerfectPickleError(Exception):
    def __str__(self):
        return 'ERROR! Pickles are perfect. Overall score less than 10/10. Try again...'


# Processing

print('Let\'s rate some pickles! (Data saved to \'%s\')\n' % pickleFile)

userInput = 'y'
while userInput.lower() != 'n':
    pickle_ratings.append(pickle_rater())

    userInput = input('Continue rating pickles? (y/n)')
    while userInput.lower() != 'y' and userInput.lower() != 'n':
        userInput = (input('Incorrect choice. Please select either \'y\' or \'n\')'))


pickle_saver(pickleFile, pickle_ratings)
new_pickleRatings = pickle_reader(pickleFile)
print(new_pickleRatings)