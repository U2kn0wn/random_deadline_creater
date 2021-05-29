from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
from quoters import Quote 
import random
import time


class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()



def rand():
    a=random.randint(2,100000)
    
    b=round(time.time()*1000)
    return a*b





def check(a):
    b=int(a)
    if(b<3):
        ran=rand()
        ran=ran%31
        return check(ran)

    return b



def display():
    

    with Loader("creating deadline...","done",0.05):
        ran=rand()
        ran=ran%31
        ran = check(ran)
        b=str(ran)
        for i in range(10):
            sleep(0.25) 



    with Loader("looking for quotes","done\n",0.05):
            a=Quote.print()

    print("\n\n")
    print("="*100)
    print("your deadline is "+b+" days")
    print("good Luck on your task")
    print("="*100)
    print(a)
    print("\n\n")


def main():
    display()
    
    exit()


if __name__=='__main__':
    main()

