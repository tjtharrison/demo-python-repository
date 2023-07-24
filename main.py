"""A simple program that loops forever with increasing count."""
import sys
import time


def main():
    """Loops forever with increasing count.

    Raises:
        KeyboardInterrupt: If the user presses Ctrl+C.

    """
    count = 0

    try:
        while True:
            count += 1
            print("I've been running for " + str(count) + " seconds.")
            time.sleep(1)
    except KeyboardInterrupt as error_message:
        raise KeyboardInterrupt from error_message


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(1)
