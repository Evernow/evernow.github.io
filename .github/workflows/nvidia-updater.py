import urllib.request, json


uf = urllib.request.urlopen(r"https://raw.githubusercontent.com/24HourSupport/CommonSoftware/main/nvidia_gpu.json")
html = uf.read()

res = json.loads(html.decode('utf-8'))
print(res['consumer']['link'])
# with open('nvidia_gpu.json', 'r+') as f:
#     data = json.load(f)
#     for driver_in_repo in data:
#       if driver_in_repo != "Last_Checked":
#         if float(data[driver_in_repo]['version']) < updated_driver_details[driver_in_repo][0]:
#             data[driver_in_repo]['version'] = str(updated_driver_details[driver_in_repo][0])
#             data[driver_in_repo]['link'] = updated_driver_details[driver_in_repo][1]
#             f.seek(0)
#     f.seek(0)
#     data["Last_Checked"]["version"] = str(datetime.now())
#     json.dump(data, f, indent=4)
#     f.truncate()     # remove remaining part
#     print(data)
a_file = open("index.html", "r")

list_of_lines = a_file.readlines()

list_of_lines[0] = r'<meta HTTP-Equiv="Refresh" content="0; URL=' + res['consumer']['link'] + '">'

a_file = open("index.html", "w")

a_file.writelines(list_of_lines)

a_file.close()


