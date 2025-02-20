class BlockExceptions:

    def __init__(self, *name_ex):
        self.name_ex = name_ex

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.name_ex)


with BlockExceptions(ZeroDivisionError, TypeError):
    a = 1 / "3"

print("OK")