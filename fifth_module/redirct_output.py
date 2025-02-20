import sys


class RedirectStreams:
    def __init__(self, *, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr
        self._old_stdout = None
        self._old_stderr = None

    def __enter__(self):
        if self.stdout:
            self._old_stdout = sys.stdout
            sys.stdout = self.stdout
        if self.stderr:
            self._old_stderr = sys.stderr
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_value, traceback):
        if self._old_stdout:
            sys.stdout = self._old_stdout
        if self._old_stderr:
            sys.stderr = self._old_stderr


stdout = open("STDOUT.txt", "w")
stderr = open("STDR.txt", "w")

with RedirectStreams(stdout=stdout, stderr=stderr):
    print(3)
    raise Exception("Иди учись STDR.txt")

stderr.close()