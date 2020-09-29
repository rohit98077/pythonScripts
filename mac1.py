import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--first',help='enter firstname')
parser.add_argument('--last',help='enter lastname')
args=parser.parse_args()
print(type(args))
f=args.first
l=args.last
print(f,l)