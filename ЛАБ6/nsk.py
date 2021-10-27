import urllib.request

webpage = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
with urllib.request.urlopen(webpage) as web_page:
    data = []
    for line in web_page.readlines():
        data.append(line.decode("utf-8"))
print(data)
