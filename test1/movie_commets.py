# -*- coding: utf-8 -*-

import requests
import re
#import pandas as pd
url_start = 'https://movie.douban.com/subject/26883064/comments?status=P'
r = requests.get(url_start)
# r = r.text
# r = r.encode('ascii', 'ignore').decode('ascii')
print(r.cookies)