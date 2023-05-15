
import requests
import json
import pandas as pd

import argparse

parser = argparse.ArgumentParser(description='StackOverflow.')

parser.add_argument("-order_by", default="desc")
parser.add_argument("-sort_by", default="popular")
parser.add_argument("-from_date", default="")
parser.add_argument("-to_date", default="")

args = parser.parse_args()



base_url = 'https://api.stackexchange.com/2.3/tags?'
order_by= args.order_by
sort_by = args.sort_by
from_date= args.from_date
to_date= args.to_date
site = 'stackoverflow'

url = '{}order={}&sort={}&site={}&fromdate={}&todate={}'.format(base_url, order_by, sort_by,site, from_date, to_date)
str_data = requests.get(url)


json_data = json.loads(str_data.text)
df= pd.DataFrame(json_data['items'])
print(df)

