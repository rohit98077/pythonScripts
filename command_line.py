import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--firstname',help='enter firstname')
parser.add_argument('--lastname',help='enter lastname')
args=parser.parse_args()
print(args)
f=args.firstname
l=args.lastname
print("HI "+f+l)