import logging, datetime
import random

logging.basicConfig(level=logging.INFO) # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file called log.txt in your project

def foo():
    print("I am foo.")
    bar(times=12)

def bar(times = 1):
    for i in range(times):
        print(f"bar-{i}")
    moo();

def moo():
    print("Now we moo.")
    for i in range(3):
        print("---------------")
        depth = random.randint(3,10);
        cow(depth)

def cow(depth_to_go):
    if depth_to_go > 0:
        print("\t"*depth_to_go,end=":")
        print("cow")
        cow(depth_to_go-1)
        print("\t" * depth_to_go+f"{depth_to_go}")

    else:
        print("Base case")

if __name__ == "__main__":
    foo()