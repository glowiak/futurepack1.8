import Tkinter
import subprocess
win = Tkinter.Tk()
win.title("pyLauncher 9.4")
win.geometry("400x400")

def vanilla():
    subprocess.call([r'vanilla.bat'])

def mw():
    subprocess.call([r'modloader.bat'])

def forge():
    subprocess.call([r'forge.bat'])

def defualt():
    subprocess.call([r'defualt.bat'])


def java():
    subprocess.call([r'java.bat'])

def mods():
    subprocess.call([r'mods.bat'])

def update():
    subprocess.call([r'update.bat'])

def about():
    about = Tkinter.Tk()
    about.title("About pyLauncher")
    la1 = Tkinter.Label(about,text="Maked by glowiak; github.com/glowiak")
    la1.pack()

def version():
    subprocess.call([r'version.bat'])

def gameDir():
    subprocess.call([r'gameDir.bat'])

def oif():
    subprocess.call([r'instancesf.bat'])

def modsf():
    subprocess.call([r'omods.bat'])

def reinstalljava():
    subprocess.call([r'reinstalljava.bat'])

def adoptions():
    options = Tkinter.Tk()
    options.title("Advanced Options")
    options.geometry("300x300")
    bue1 = Tkinter.Button(options,text="Reinstall Java",command=reinstalljava)
    bue1.pack()
    options.mainloop()

def irm():
    subprocess.call([r'installIndustrial.bat'])

def futurePackPlay():
    subprocess.call([r'game.bat'])
def instance():
    select = Tkinter.Tk()
    select.title("Select instance")
    select.geometry("300x300")
    label = Tkinter.Label(select,text="Select instance to play:")
    label.pack()
    de = Tkinter.Button(select,text="Defualt from .minecraft",command=defualt)
    de.pack()
    van = Tkinter.Button(select,text="Vanilla 1.2.5",command=vanilla)
    van.pack()
    modern = Tkinter.Button(select,text="Modloader 1.2.5",command=mw)
    modern.pack()
    fg = Tkinter.Button(select,text="Forge 1.2.5",command=forge)
    fg.pack()
    select.mainloop()

def gog():
    subprocess.call([r'gogr.bat'])

def main():
    l1 = Tkinter.Label(win,text="FuturePack1.8 Launcher powered by pyLauncher")
    l1.pack()
    l1 = Tkinter.Label(win,text="Mods:TomanyItems,IndustrialCraft2,SPC")
    l1.pack()
    b1 = Tkinter.Button(win,text="Play!",command=futurePackPlay)
    b1.pack()
    b6 = Tkinter.Button(win,text="Open game dir",command=gameDir)
    b6.pack()
    b8 = Tkinter.Button(win,text="Install request mods",command=irm)
    b8.pack()
    b9 = Tkinter.Button(win,text="glowiak on GitHub",command=gog)
    b9.pack()
    win.mainloop()

main()
    
