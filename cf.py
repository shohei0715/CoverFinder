from subprocess import Popen, PIPE
from Tkinter import *
import webbrowser


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

    c0.create_text(75, 75, text = res["artist"], font = ('FixedSys', 14))
    c0.create_text(75, 89, text = res["title"], font = ('FixedSys', 14))
    c0.create_text(75, 103, text = res["album"], font = ('FixedSys', 14))

    root.after(1000,get_iTunes)

def open_browser():
    url = 'http://www.python.org/'
    webbrowser.open_new(url)
    


#print artist
#print title
#print album

root = Tk()
c0 = Canvas(root, width = 150, height = 150)

info_dic = get_iTunes()

#c0.create_text(75, 75, text = info_dic["artist"], font = ('FixedSys', 14))
#c0.create_text(75, 89, text = info_dic["title"], font = ('FixedSys', 14))
#c0.create_text(75, 103, text = info_dic["album"], font = ('FixedSys', 14))

button=Button(root, text="Get Info from iTunes", command = open_browser())
button.pack()

c0.pack()

root.mainloop()
