import re

f = open("text.txt")
data = f.read()

emails = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+'
phoneNums = '[0-9+-]+-[0-9]+-[0-9+-]+'
urls = 'https?:\/\/[^\s]*'

listMail = re.findall(emails, data)
for email in listMail:
    index = f.tell()
    len = email.__len__()
    print ("Email: ", email, index, "Length: ",len)

listPhone = re.findall(phoneNums, data)
for phoneNum in listPhone:
    index = f.tell()
    len = phoneNum.__len__()
    print ("Phone number: ", phoneNum, index, "Length: ", len)

listUrl = re.findall(urls, data)
for url in listUrl:
    index = f.tell()
    len = url.__len__()
    print ("Website: ", url, index, "Length: ", len)

f.close()