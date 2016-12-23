# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", type=str,
                    help="assign the goods url. ex: http://buy.mi.com/tw/accessories/117")
parser.add_argument("-g", "--goods", nargs='+', type=str,
                    help=u"assign goods item name to be noticed. ex: '小米手環 石墨黑' '小米手環炫彩腕帶 螢光橘'")
parser.add_argument(
    "-o", "--output", type=argparse.FileType('w'), help='assign output file name')
# parser.add_argument("-m", "--mails", nargs='+', type=str,
#                    help="assign email address. ex: someone@gmail.com")

args = parser.parse_args()

CANBUY = "立即購買".encode('utf-8')
CANNOTBUY = "暫時缺貨".encode('utf-8')

page = requests.get(args.url)

soup = BeautifulSoup(page.content, "html.parser")

goods = soup.select("div.goods-item-info")

wants = []

try:
    # the goods want to notice
    for want in args.goods:
        # the products in this web page
        for product in goods:
            if product.text.encode('utf-8').find(want) >= 0:
                if product.text.encode('utf-8').find(CANBUY) >= 0:
                    wants.append(want)

    if len(wants) > 0:
        if args.output is not None:
            for want in wants:
                args.output.write(want+'\n'.encode('big5'))
            args.output.close()
        else:
            for want in wants:
                print ("Hurry!!! " + want + " is available now!!!")

except Exception as err:
    parser.print_help()
    print('ERROR!!! ' + err.message)
