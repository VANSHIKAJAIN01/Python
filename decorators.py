def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the functon...")
    return wrapper
#the above is the decorator as it is a function that takes a function that takes a function and modify it by add some additional capabilities

@announce
#to add the decorator to hello()
def hello():
    print("Hello World!!!")

hello()