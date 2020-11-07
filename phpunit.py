import argparse


#Menu
#Single Domain
#Read from file
#Number of Threads




argparser = argparse.ArgumentParser()
argparser.add_argument('-d',"--domain",help="Check Single Domain",type=str)
argparser.add_argument('-i',"--inputfile",help="Read from file",type=str)
argparser.add_argument('-t',"--threads",help="Number of Threads(Default 20",type=int)


args=argparser.parse_args()

if args.domain:
    print(args.domain)

urllist = []
if args.inputfile:
    urlfile = open(args.inputfile,"r")
    for url in urlfile.read().split('\n'):
        urllist.append(url)

print(urllist)
