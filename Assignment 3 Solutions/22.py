import random
import string

def randomString(stringLength=10):

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random String is ", randomString() )
print ("Random String is ", randomString(10) )
print ("Random String is ", randomString(10) )