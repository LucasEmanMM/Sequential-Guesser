import sys
import time

def brute_force_string(target: str, charset: list[str], delay: float = 0.01):
    built = ""
    length = len(target)

    while len(built) < length:
        for ch in charset:
            attempt = built + ch
            print(attempt)
            sys.stdout.flush()
            time.sleep(delay)
            if attempt == target[:len(attempt)]:
                # this partial match is valid—lock in this character
                built += ch
                break
    return built

def main():
    # define the characters we’ll brute‑force through
    charset = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?-")
    target = input("Enter the target string: ")
    print("\nStarting brute-force...\n")
    result = brute_force_string(target, charset, delay=0.005)
    print(f"\nDone! Built string: {result}")

if __name__ == "__main__":
    main()
