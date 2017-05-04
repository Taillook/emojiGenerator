# -*- coding: utf-8 -*-

import argparse

from emoji_generator.generate import generate_emoji

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("character", type=str, help="target character")
    parser.add_argument("--font", type=str, default="Ricty-Bold.ttf")
    parser.add_argument("--color", type=str, default="#000000")
    args = parser.parse_args()
    print(args)
    generate_emoji(args.character, args.color, args.font)
