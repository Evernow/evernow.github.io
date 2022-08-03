import urllib.request, json


uf = urllib.request.urlopen(r"https://raw.githubusercontent.com/24HourSupport/CommonSoftware/main/nvidia_gpu.json")
html = uf.read()

res = json.loads(html.decode('utf-8'))
a_file = open("index.html", "r")

list_of_lines = a_file.readlines()
if list_of_lines[0] != r'<meta HTTP-Equiv="Refresh" content="0; URL=' + res['consumer']['link'] + '">':
  list_of_lines[0] = r'<meta HTTP-Equiv="Refresh" content="0; URL=' + res['consumer']['link'] + '">'

  a_file = open("index.html", "w")

  a_file.writelines(list_of_lines)

  a_file.close()


import datetime
if datetime.datetime.now().strftime("%d") == '30': # Cancels out stupid Github idle outs
  with open(".github/workflows/IdlerFaker.txt ", "a") as f:
      import datetime
      d = datetime.datetime.now()
      f.write(d.strftime("%d"))
