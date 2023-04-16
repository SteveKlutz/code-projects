
# What will users want to know when opening app? ---> Date, Weather (Temp/Precip), your saved pets
# What factors affect time dog can be outside? ---> Weather (Temp/Precip), dog size, dog fur type

coat_op = ['short', 'long']
size_op = ['small', 'medium', 'large']


def intro():
    # opening statement
    print('How long can your dog be outside?')
    print('Answer the questions below to find out!')
    print('----------------------------------------------')


def dog_size():
    # define input for dog size
    size = input('Enter the size of your dog.\nSmall, Medium or Large?\n')
    while size not in size_op:
        print('Incorrect entry. Try again.')
        size = input()
    print('Your dog is ' + size + ' sized.\n')
    return size


def dog_coat():
    # figure out how to implement coat type answers below
    # define input for dog coat type
    coat = input('What best describes your dogs coat type?\nShort or long?')
    while coat not in coat_op:
        # error message printed if anything but dog coat options is entered by user
        print('Incorrect entry. Try again.\n')
        coat = input()
    else:
        print('You selected a ' + coat + ' coat.\n')
    return coat


def dog_temp():
    # define input for outside temperature
    temp = int(input('What is the temperature outside? (F)\n'))
    return temp


def results():
    if (size == 'small' or 'medium' or 'large') and coat == 'short':
        if 1 < temp < 19:
            print('5 minutes or less.')
        elif 20 < temp < 32:
            print('10 to 15 minutes.')
        elif 33 < temp < 59:
            print('About 30 minutes.')
        elif 70 < temp < 90:
            print('About an hour should be fine. Try to keep them out of direct sunlight.')
        elif 90 < temp < 99:
            print('5 minutes or less.')
        else:
            print('Not a good idea to be outside til temperature changes.')
    elif (size == 'small' or 'medium' or 'large') and coat == 'long':
        if 1 < temp < 19:
            print('5 minutes or less.')
        elif 20 < temp < 32:
            print('10 to 15 minutes.')
        elif 33 < temp < 59:
            print('About an hour.')
        elif 70 < temp < 90:
            print('About 30 minutes. Try to keep them out of direct sunlight.')
        elif 90 < temp < 99:
            print('In and out.')
        else:
            print('Not a good idea to be outside til temperature changes.')
    return results


intro()
size = dog_size()
coat = dog_coat()
temp = dog_temp()

print('\n')
print('Summary:\nYour dog is ' + str(size) + ' sized with a ' + str(coat) + ' coat and the current temperature is '
      + str(temp) + '.\n')
print('Results:')
results()
