import sys

import urllib.request
import urllib.parse
import re

url = 'http://www.joinvillesquaregarden.com.br/eventos.html'
values = {'s':'basics',
          'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('latin1')

req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)

respData = resp.read()

logos = re.findall(r'" src="/images/(.*?)">',str(respData))
logos = ['{0}/images/{1}'.format("http://www.joinvillesquaregarden.com.br",logo) for logo in logos]

eventos = re.findall(r'img alt="(.*?)"',str(respData))

datas = re.findall(r'<div class="subtopic">(.*?)<a>',str(respData))
datas = ['{0}'.format(data.replace('\\r',"")) for data in datas]
datas = ['{0}'.format(data.replace('\\t',"")) for data in datas]
datas = ['{0}'.format(data.replace("\\n","")) for data in datas]

horarios = re.findall(r'<div class="hour">(.*?)</div>',str(respData))

nextEvents = (eventos,datas,horarios,logos)


for i in range(0,len(datas)):       
    print(nextEvents[0][i]+".\nData: "+nextEvents[1][i]+", às "+nextEvents[2][i]+"\nLogo: "+nextEvents[3][i]+"\n\n")
