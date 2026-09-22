"""
Topic: Decorators
"""

def logger(func):

    def wrapper():
        print("Starting execution")
        func()
        print("Execution completed")

    return wrapper


@logger
def login_test():
    print("Executing Login Test")


login_test()

# Starting execution
# Executing Login Test
# Execution completed