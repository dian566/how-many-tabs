"""Entry for the make.fun bounty "How Many Tabs Do You Have Open?".

Writes a single number in digits and nothing else to /output/entry.txt.
Gate: UTF-8 text of 1 to 5 characters, not only white space.
"""

import os

NUMBER = "47"

assert NUMBER.isdigit(), "entry must be digits only"
assert 1 <= len(NUMBER) <= 5, "entry must be 1 to 5 characters"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(NUMBER)

if __name__ == "__main__":
    main()
