#Task1 Writing and Testing a Decorator:
import logging 
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__}")

        if args: 
            logger.info(f"positional parameters: {list(args)}")
        else: 
            logger.info("positional parameters: none")
        
        if kwargs: 
            logger.info(f"keyword parameters: {kwargs}")
        else: 
            logger.info("keyword parameters: none")
        
        logger.info(f"return: {result}")

        return result
    return wrapper

@logger_decorator
def hello():
    print("Hello everyone!")
hello()

@logger_decorator
def many_args(*args):
    return True
many_args(1,2,3)

@logger_decorator
def many_kwargs(**kwargs):
    return logger_decorator
many_kwargs(name="Kay", age=29)