import contextlib


class Connection:

    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print("Starting transaction", self.xid)
        result = self.xid
        self.xid += 1
        return result

    def _commit_transaction(self, xid):
        print("Committing transaction", xid)

    def _rollback_transaction(self, xid):
        print("Rolling back transaction", xid)


class Transaction:

    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)

    try:
        yield
    except:
        tx.rollback()
        raise
    tx.commit()


conn = Connection()

# this block asure that transaction is automatically committed or roll-backed
# if there is a problem
try:
    with start_transaction(conn):
        x = 1 + 1
        raise ValueError()
        y = 2 + 2
        print(f"transaction => {x} {y}")
except ValueError:
    print("Operation failed!")

try:
    with start_transaction(conn):
        x = 1 + 1
        y = 2 + 2
        print(f"transaction => {x} {y}")
except ValueError:
    print("Operation failed!")