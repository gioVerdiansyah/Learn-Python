from urllib.request import urlopen
import bs4
import argparse as arg

parser = arg.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="URL to search")
parser.add_argument('-f', '--find', required=True, help="What do you want to find")
parser.add_argument('-fl', '--find-all', action="store_true", help="It is will to findAll about you want to find")
parser.add_argument('-b', '--beauty', action="store_true", help="Make what you find to be beauty")
args = parser.parse_args()

url = args.url
page = urlopen(url)
html = page.read().decode('utf-8')

suop = bs4.BeautifulSoup(html, "html.parser")

if args.beauty:
    if not args.find_all:
        s_index = html.find(f"<{args.find}>") + len(f"<{args.find}>")
        e_index = html.find(f"</{args.find}>")

        print(html[s_index:e_index])
    else:
        raise ValueError("You must do not include -fl/--find-all")
else:
    if args.find_all :
        print(suop.findAll(args.find))
    else:
        print(suop.find(args.find))