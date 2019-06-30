import threading
import time
"""
custom made thread class
"""


class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        with open(self.out, "a") as f:
            f.write(self.text)
        time.sleep(3)
        print(f"finsih background task write to file {self.out}")
