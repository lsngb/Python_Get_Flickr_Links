import os
import urllib.request
import shutil

def main():
    while True:
        try:
            get_set()
        except:
            print("Error! Try again!\n")
def get_set():
    Aset=input("Input a flickr set address: \n")
    if Aset[12:18]=="flickr":
        string=os.path.dirname(os.path.abspath(__file__))
        string=string+"/garbage"
        if not os.path.exists(string):
            os.makedirs(string)
        web_set=urllib.request.urlopen(Aset)
        f=open(string+"/set.txt","w",encoding="utf8")
        data=web_set.read().decode("utf8")
        web_set.close()
        f.write(data)
        f.close
        f=open(string+"/set.txt","r",encoding="utf8")
        r=open("result_mid800.html","w",encoding="utf8")
        r.write("<!DOCTYPE html>\n")
        while True:
            Aline=f.readline()
            if Aline=="":
                break
            elif '	<div class="title"><a data-track="photo-click" href="' in Aline:
                x=Aline.find("/photos/nycosi/")
                y=Aline.find("/in/set")
                pic_id=Aline[x+15:y]
                Apage="https://www.flickr.com/photos/nycosi/"+pic_id+"/sizes/c/"
                web_page=urllib.request.urlopen(Apage)
                page_file=open(string+"/web_page.txt","w",encoding="utf8")
                data=web_page.read().decode("utf8")
                #web_page.close()
                page_file.write(data)
                page_file.close()
                page_file=open(string+"/web_page.txt","r",encoding="utf8")
                while True:
                    Asubline=page_file.readline()
                    if Asubline=="":
                        page_file.close()
                        break
                    elif '<div id="allsizes-photo">' in Asubline:
                        Asubline=page_file.readline()
                        x=Asubline.find('="')
                        y=Asubline.find('">')
                        print(".",end="")
                        pic_url=Asubline[x+2:y]
                        r.write('<a href="'+pic_url+'">'+pic_url+'</a></br>\n')
        print("\nDone!\n")
        f.close()
        r.close()
        shutil.rmtree(string)
    else:
        print("Error! Try again!\n")

main()
