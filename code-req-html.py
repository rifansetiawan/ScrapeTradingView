from requests_html import HTMLSession
import datetime
import time
from datetime import datetime
datestring = datetime.strftime(datetime.now(), '(%Y-%m-%d)-(%H.%M.%S)')


out_filename = datestring+".csv"
headers = "Market_Open,Prev,Open,Server_Time,Local_Time \n"

f = open(out_filename, "w")
f.write(headers)
for i in range(15):
	import datetime
	url = 'https://www.tradingview.com/symbols/MYX-FCPO1%21/'
	session = HTMLSession()
	r = session.get(url)

	r.html.render()

	num_prev = 'div.tv-fundamental-block__value.js-symbol-prev-close'
	num_curr = 'div.tv-symbol-price-quote__value.js-symbol-last'
	num_open = 'div.tv-fundamental-block__value.js-symbol-open'
	trd_time = 'span.js-symbol-lp-time'

	result_server_time = r.html.find(trd_time, first=True).text
	result_curr = r.html.find(num_curr, first=True).text
	result_prev = r.html.find(num_prev, first=True).text
	result_open = r.html.find(num_open, first=True).text
	
	start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
	#print(datestring)
	print (result_server_time)
	print (start_time)
	print (result_curr)
	print (result_prev)
	print (result_open)
	
	f.write(result_curr + ", " + result_prev + ", " + result_open + ","+result_server_time+ ","+start_time+ "\n")
	time.sleep(60)

f.close()