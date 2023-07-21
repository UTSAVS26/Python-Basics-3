# Program 7

def filecopy():
    ifile=open("quotes.txt","r")
    ofile=open("newquotes.txt","w")
    l=ifile.readline()
    while l:
        ofile.write(l)
        l=ifile.readline()
    ifile.close()
    ofile.close()

filecopy()
