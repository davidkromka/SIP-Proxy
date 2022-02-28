import datetime


# calls list
def call(origin, destination, message):
    f = open("calls.txt", "a")
    f.write(datetime.datetime.now().ctime() + '\t' + origin + message + destination + '\n')
    f.close()
