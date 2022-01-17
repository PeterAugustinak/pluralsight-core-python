class LoggingContextManager:

    def __enter__(self):
        print("LoggingContextManager.__enter__()")
        return "You are in a with-block!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("LoggingContextManager.__exit__(): Normal exit detected.")
        else:
            print("LoggingContextManager.__exit__(): Exception detected!\n"
                  f"type={exc_type}, value={exc_val}, trraceback={exc_tb} ")


cm = LoggingContextManager()

# normal exit
with cm:
    pass

# exceptional exit
with cm:
    raise ValueError()


