import sys
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-find", type=str)
    parser.add_argument("-spn", default="0.005", type=float)
    args = parser.parse_args()
    return [args.find, str(args.spn)]
