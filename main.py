import time
import sys

def main ():
    """Loops forever with increasing count.

    Raises:

    """
    count = 0

    try:
        while True:
            count += 1
            print("I've been running for " + str(count) + " seconds.")
            time.sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(1)

