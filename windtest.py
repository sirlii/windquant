from WindPy import *
from datetime import *
import json
import io

w.start()

if not w.isconnected():
    print "can'stockdata connect to wind!"
    exit

SYMBOL_NAME = u"000300.SH"
stockdata = w.wsd(SYMBOL_NAME, "pe_ttm,pb_lf,close", "2016-01-01", "2016-05-08", "")
jsondata = [{u"symbol":SYMBOL_NAME}, []]
jsondata_2 = jsondata[1]
i=0
for date in stockdata.Times:
    jsondata_2.append({"date": date.date().isoformat(), u"pe": stockdata.Data[0][i],u"pb": stockdata.Data[1][i], u"close": stockdata.Data[2][i] })
    i+=1

f = io.open('c:\\test.json', 'wb')
s= json.dumps(jsondata)
f.write(s)
f.close()

w.stop()
