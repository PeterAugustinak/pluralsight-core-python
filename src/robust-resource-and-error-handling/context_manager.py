# CONTEXT MANAGER DEFINED ON CLASS LEVEL

class LoggingContextManager:

    def __enter__(self):
        print("LoggingContextManager.__enter__()")
        return "You are in a with-block!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("LoggingContextManager.__exit__(): Normal exit detected.")
        else:
            print("LoggingContextManager.__exit__(): Exception detected!\n"
                  f"type={exc_type}, value={exc_val}, traceback={exc_tb} ")


cm = LoggingContextManager()

# normal exit
print(f"\nCLASS DEFINED CONTEXT MANAGER:")
with cm as x:
    print(x)

# exceptional exit
# with cm:
#     raise ValueError()


# CONTEXT MANAGER DEFINED ON FUNC LEVEL BY DECORATOR (above class implemented
# by decorator)
import contextlib
import sys

@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield "You are in the with-block!" # this is not working in console
        print('loging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exceptional exit', sys.exc_info())
        # raise

print(f"\nCFUNC BY DECORATOR DEFINED CONTEXT MANAGER:")
with logging_context_manager() as x:
    print(x)

with logging_context_manager() as x:
    raise ValueError("Something went wrong")

# NESTED CONTEXT MANAGERS
@contextlib.contextmanager
def nest_test(name):
    print("Entering", name)
    yield
    print("Existing", name)

print(f"\nMULTIPLE CONTEXT MANAGERS:")
with nest_test("outer"), nest_test("inner"):
    print("BODY")

print(f"\nMULTIPLE CONTEXT MANAGERS (NESTED):")
with nest_test("outer"):
    with nest_test("inner"):
        print("BODY")

