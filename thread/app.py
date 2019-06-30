from util import AsyncWrite
if __name__ == "__main__":
    message = input("Enter the string to be stored :")
    background = AsyncWrite(message, "out.txt")
    background.start()
    print("program continues while writing task is running")
    print(f"sum of 400+300={str(400+300)}")
    background.join() # waites till the thread finished
    print("waite till the writing task finished")
