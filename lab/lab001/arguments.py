import argparse

parser = argparse.ArgumentParser(description="To jest opis")
parser.add_argument('file', help = 'name of file')
parser.add_argument('-n', '--number', help = 'some number', type=int, default = 44)
parser.add_argument('-bpar', '--bpar', help = 'some flag', action = 'store_true')
args = parser.parse_args()

print(f'{args.file = }')
print(f'{args.number = }')
print(f'{args.bpar = }')