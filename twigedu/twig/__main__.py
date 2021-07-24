import argparse
import sys
#import time

from twig.devide import chunks
from twig.devide import input_validation
from twig.devide import yes_or_no


def main(args=None):
    """
    This is going to take a list and a number from the user.
    And will return the grouped lists in a list.
    """

    # assume the list is comma seperated
    a_list = input("Enter your list.\n ex) [1,2,3,4,5,6]\n")
    a_list = a_list.replace(" ", "")
    your_list = a_list.strip('][').split(',')

    a_number = input("Enter a size with an integer.\n ex) 3\n")
    your_n = input_validation(a_number)

    output_list = list(chunks(your_list, your_n))
    print(output_list)

    reply = yes_or_no('Do you want to stop!')
    if reply:
        sys.exit()
    else:
        main()


# executes when your script is called from the command-line
if __name__ == "__main__":
    main(sys.argv)
