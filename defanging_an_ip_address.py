"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Constraints:

The given address is a valid IPv4 address.
"""


def defangIPaddr(address: str) -> str:
    defanged = address.replace('.','[.]')
    return defanged


if __name__ == '__main__':
    print(defangIPaddr('255.100.50.0'))
    print(defangIPaddr('1.1.1.1'))

