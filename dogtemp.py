
# What will users want to know when opening app? ---> Date, Weather (Temp/Precip), your saved pets
# What factors affect time dog can be outside? ---> Weather (Temp/Precip), dog size, dog fur type

def dogtime():
    # opening statement
    print('How long can your dog be outside?')
    print('Answer the questions below to find out!')
    print('----------------------------------------------')

    # define input for dog size
    dogsize = input('What size is your dog?\nSmall, Medium or Large?')

    if dogsize == 'Small':
        print('Your dog is snack size.')
    elif dogsize == 'Medium':
        print('Your dog is medium size.')
    elif dogsize == 'Large':
        print('Your dog is a tank.')
    else:
        print('Incorrect entry.')
        return

    # define input for dog coat type
    coattype = input('What is your dogs coat type?\nShort, Medium, Long, Double, Curly, Silky, Rough, Wire, Smooth or '
                     'Hairless?\nNot sure? Enter "More info" and we can tell you what breeds are commonly associated '
                     'each coat.')
    # figure out how to implement coat type answers below

    # define input for outside temperature
    temp = int(input('What is the temperature outside? (F)'))

    # create answers for user depending on dog size, dog coat type, and outside temperature
    if dogsize == 'Small' or dogsize == 'Medium':
        if 20 < temp < 32:
            print('10 to 15 minutes.')
        elif 70 < temp < 90:
            print('A few hours will be fine.')
        elif 33 < temp < 59:
            print('About an hour.')
        elif 90 < temp < 99:
            print('5 minutes or less.')
        elif 1 < temp < 19:
            print('5 minutes or less.')
        elif 100 < temp < 0:
            print('Probably not a good idea to be outside til temperature changes.')
        else:
            print('Incorrect entry.')
            return

    elif dogsize == 'Large':
        if temp < 32 or temp > 90:
            print('10 to 15 minutes.')
        elif 60 < temp < 90:
            print('About an hour.')
        elif 33 < temp < 59:
            print('A couple hours will be fine.')
        else:
            print('Incorrect entry.')
            return

    # print coat examples if user enters "More info"
    elif dogsize == 'More info':
        print('Short: Pointers, Doberman, and Boxers\n'
              'Medium: Germain Shepherds, Golden Retrievers, and Belgian Tervurens\n'
              'Long: Afghan Hounds, Old English Sheepdogs, and Bearded \n'
              'Double: Bernese Mountain Dog, Beagle, Newfoundland, Husky\n'
              'Curly: Portuguese Water Dogs, Airedale Terriers and Poodles\n'
              'Silky: Silky Terrier, Yorkshire Terrier, Afghan Hound and Irish Setter\n'
              'Rough: Rough Collie\n'
              'Wire: German Wirehaired Pointer, the Airedale Terrier, and the Wire Fox Terrier\n'
              'Smooth: Bloodhounds, Dalmatians, Great Danes, and French Bulldogs\n'
              'Hairless: Chinese Crested, the Xoloitzcuintli, and American Hairless Terrier')

    # error message printed if anything but 3 dog size options is entered by user
    else:
        print('Incorrect entry.')
        return

dogtime()
