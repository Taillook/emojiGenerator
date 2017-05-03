# -*- coding: utf-8 -*-

import argparse

from emoji_generator.generate import generate_emoji

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("character", type=str, help="target character")
    parser.add_argument("--font", default="Ricty-Bold.ttf")
    args = parser.parse_args()

    generate_emoji(args.character, args.font)
