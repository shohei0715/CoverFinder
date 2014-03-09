#!/usr/bin/python
# -*- coding:utf-8 -*-


from subprocess import Popen, PIPE
from Tkinter import *
import webbrowser
import urllib


AS = '''
tell application "iTunes"
    %s of current track
end tell
'''
args = []



def get_element(val):
    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(AS % val)
    return stdout.rstrip()

def get_iTunes():

    res = {"artist":"","title":"","album":""}
    res["artist"] = get_element('artist')
    res["title"] = get_element('name')
    res["album"] = get_element('album')


    #c0.create_text(75, 75, text = res["artist"] , font = ('FixedSys', 14))
    #c0.create_text(75, 89, text = res["title"], font = ('FixedSys', 14))
    #c0.create_text(75, 103, text = res["album"], font = ('FixedSys', 14))
    #c0.pack()


#    root.after(1000,get_iTunes)
    return res

def iTunes_update():


    info_dic = get_iTunes()
    artist.configure(text=info_dic["artist"])
    title.configure(text=info_dic["title"])
    album.configure(text=info_dic["album"])

    root.after(1000,iTunes_update)


def open_browser():


    info_dic = get_iTunes()
    keyword_title = info_dic["title"].decode('utf-8') + " "
    keyword_artist = info_dic["artist"].decode('utf-8') + " "
    keyword_album = info_dic["album"].decode('utf-8') + " "
    
    url = 'http://www.amazon.co.jp/gp/search/?__mk_ja_JP=%83J%83%5E%83J%83i&field-keywords='+urllib.quote(keyword_album.encode('shift-jis'))+urllib.quote(keyword_artist.encode('shift-jis'))
    webbrowser.open_new(url)
    


#print artist
#print title
#print album

root = Tk()
c0 = Canvas(root, width = 150, height = 150)


info_dic = get_iTunes()
artist = Label(None, text=info_dic["artist"])
title = Label(None, text=info_dic["title"])
album =Label(None, text=info_dic["album"])
artist.pack()
title.pack()
album.pack()

iTunes_update()

#c0.create_text(75, 75, text = info_dic["artist"], font = ('FixedSys', 14))
#c0.create_text(75, 89, text = info_dic["title"], font = ('FixedSys', 14))
#c0.create_text(75, 103, text = info_dic["album"], font = ('FixedSys', 14))

button=Button(root, text="Get Info from iTunes", command = open_browser)
button.pack()



root.mainloop()
