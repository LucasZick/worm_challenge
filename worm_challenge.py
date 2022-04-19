import os, time, sys

os.system('clear') or None

def worm_challenge(word, timing):
    array = list(word)
    while True:
        try:
            for i in range(len(array)):
                array[i] = array[i].upper()
                word = ''.join(array)
                print(word)
                array[i] = array[i].lower()

                time.sleep(timing)
                os.system('clear') or None
        except:
            print('Application stopped, please consider trying again.')
            sys.exit(0)

worm_challenge(word=input('Write the worm word here:  '),
               timing=float(input('Write the velocity to the changing in seconds: ')))