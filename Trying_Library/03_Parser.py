import argparse as arg
import re

parser = arg.ArgumentParser()
parser.add_argument("-o", "--output", action="store_true", help="Output displays")
parser.add_argument("-n", "--name", required=True, help="Enter your name")
parser.add_argument("-a", "--age", required=True, help="Enter your age")
args = parser.parse_args()

if not re.match(r"\d{2}-\d{2}-\d{4}", args.age):
    print("Invalid date format for age. Please use the format dd-mm-yyyy.")
else:
    print(f"Hallo {args.name} and your age is {args.age}, Welcome")


if args.output:
    print("Hello ini adalah sebuah output!")
