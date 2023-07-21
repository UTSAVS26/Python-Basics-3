import webbrowser
import urllib.request
url=input("Enter URL to display details: ")
x=urllib.request.urlopen(url)
print("URL READ:   ",x.geturl())
print("HEADERS:   ",x.headers)
print("INFO:   ",x.info())
print("CODE:   ",x.getcode())
print("\n\n")
myurl=input("Enter 'Text to Search Online': ")
webbrowser.open_new_tab("https://www.google.com?q="+myurl)
