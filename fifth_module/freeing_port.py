import os
import signal
import subprocess
import re

from second_module.max_number import app


def check_port():
    result = subprocess.run(["lsof", "-i", ":5000"], capture_output=True, text=True).stdout
    pattern = r"\s+\d+\s+"

    try:
        pid = int(re.search(pattern, result[1:]).group())
    except AttributeError:
        return "Порт не занят"

    if result:
        os.kill(pid, signal.SIGTERM)



if __name__ == '__main__':
    check_port()
    app.run(debug=True)
