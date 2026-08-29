import argparse
from html import parser


def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user
    when they run the program.

    Command Line Arguments:
      1. --dir  : path to the folder of pet images
      2. --arch : CNN model architecture
      3. --dogfile : path to the file containing valid dog names

    Returns:
      in_args - parsed command line arguments
    """

    # Creates Argument Parser object
    parser = argparse.ArgumentParser()

    # Argument 1: Path to the folder of pet images
    parser.add_argument('--dir',
                    type=str,
                    default='pet_images/',
                    help='path to the folder of pet images')

    parser.add_argument('--arch',
                    type=str,
                    default='vgg',
                    choices=['resnet', 'alexnet', 'vgg'],
                    help='CNN model architecture to use')

    parser.add_argument('--dogfile',
                    type=str,
                    default='dognames.txt',
                    help='text file containing valid dog names')

    # Retrieves command line arguments
    in_args = parser.parse_args()

    return in_args
