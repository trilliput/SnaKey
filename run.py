#!/usr/bin/env python3
import argparse
from snakey.game import SnaKeyGUI


def parse_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--grid-width',
                        action='store', type=int, required=False, default=10,
                        help='Width and height of the square grid')
    return parser.parse_args()


if __name__ == '__main__':
    arguments = parse_cli_arguments()
    root = SnaKeyGUI(arguments.grid_width)
    root.mainloop()
