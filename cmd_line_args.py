import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--firstname',help='enter firstname',default='abc')
parser.add_argument('--lastname',help='enter lastname',default='xyz')
args=parser.parse_args()
print(args)

f=args.firstname
l=args.lastname
print("Hi "+f+' '+ l)