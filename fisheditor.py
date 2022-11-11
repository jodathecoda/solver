#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import time
import settings
import shutil

global cwd
cwd = os.getcwd()

def fisheditor():
    global cwd
    settings.printfishes(settings.allfishes)
    fish = input("enter fish name: ")
    if fish not in settings.allfishes:
        print("unknown fish")
        time.sleep(2)
        settings.print_logo()
    elif fish in settings.referencefishes:
        print("reference fish - can not be modified")
        time.sleep(2)
        settings.print_logo()
    else:
        oldsea = ""
        newsea = ""
        newseafile = ""
        paggression = ""
        faggression = ""
        taggression = ""
        raggression = ""
        seacode = ""
        raisingrangetype = ""
        rangecode = ""
        success = 1
        reset_ranges = 1

        filerangetype = cwd + "/fishes/" + fish + "/rt.dat" #range type 0=merged 1=polarized
        range_type_as_digit = 2
        try:
            with open(filerangetype, "r") as f:
                range_type_as_digit = int(f.read())
            f.close()
        except IOError:
            print("no such file " + fileaggression)
            dumb = input("]")
        if range_type_as_digit == 0:
            rangecode = '0'
            raisingrangetype = "merged"
        elif range_type_as_digit == 1:
            rangecode = '1'
            raisingrangetype = "polarized"
        else:
            print("unknown raising rangetype")
            dumb = input("]")

        fileaggression = cwd + "/fishes/" + fish + "/pa.dat" #first take preflop aggression
        try:
            with open(fileaggression, "r") as f:
                paggression = f.read()
            f.close()
        except IOError:
            print("no such fish: " + fish)
            dumb = input("]")
        fileaggression = cwd + "/fishes/" + fish + "/fa.dat" # take flop aggression
        try:
            with open(fileaggression, "r") as f:
                faggression = f.read()
            f.close()
        except IOError:
            print("no such fish: " + fish)
            dumb = input("]")
        fileaggression = cwd + "/fishes/" + fish + "/ta.dat" # take turn aggression
        try:
            with open(fileaggression, "r") as f:
                taggression = f.read()
            f.close()
        except IOError:
            print("no such fish: " + fish)
            dumb = input("]")
        fileaggression = cwd + "/fishes/" + fish + "/ra.dat" # take river aggression
        try:
            with open(fileaggression, "r") as f:
                raggression = f.read()
            f.close()
        except IOError:
            print("no such fish: " + fish)
            dumb = input("]")
        filesea = cwd + "/fishes/" + fish + "/sea.dat"
        try:
            with open(filesea, "r") as f:
                seacode = f.read()
                if seacode == '0':
                    oldsea = "white"
                elif seacode == '1':
                    oldsea = "yellow"
                elif seacode == '2':
                    oldsea = "red"
                elif seacode == '3':
                    oldsea = "black"
                else:
                    print("error in assigning sea")
                    dumb = input("]")
            f.close()
        except IOError:
            print("no such file " + filesea)
            dumb = input("]")
        if success:
                if oldsea == 'yellow':
                    print('yellow sea')
                elif oldsea == 'red':
                    print('red sea')
                elif oldsea == 'black':
                    print('black sea')
                else:
                    print('white sea')
                print("preflop aggression: " + str(paggression))
                print("flop aggression: " + str(faggression))
                print("turn aggression: " + str(taggression))
                print("river aggression: " + str(raggression))
                print("range type: " + raisingrangetype)
                print("Enter sea if you want to reset this bot ranges: ")
                print("w=white  y=yellow r=red b=black")
                choice = input("]")
                if choice == 'w':
                    print("white sea")
                    newsea = "white"
                    newseafile = "milkfish"
                    seacode = '0'
                elif choice == 'y':
                    print("yellow sea")
                    newsea = "yellow"
                    newseafile = "yellowfish"
                    seacode = '1'
                elif choice == 'r':
                    print("red sea")
                    newsea = "red"
                    newseafile = "redfish"
                    seacode = '2'
                elif choice == 'b':
                    print("black sea")
                    newsea = "black"
                    newseafile = "blackfish"
                    seacode = '3'
                else:
                    reset_ranges = 0

                f.close()
                if reset_ranges:
                    cwd = os.getcwd()
                    src = cwd + "/fishes/" + newseafile + "/ranges/"
                    dst = cwd + "/fishes/" + fish + "/ranges/"
                    try:
                        shutil.rmtree(dst)
                        shutil.copytree(src, dst)
                    except:
                        print("Error in copy sea ranges")
                        dumb = input("]")
                paggr = input("enter preflop aggression (20-40):")
                try:
                    dumbint = int(paggr)
                    if dumbint < 20 or dumbint > 40:
                        print("aggression not changed")
                    else:
                        paggression = str(dumbint)
                except:
                    print("aggression not changed")
                faggr = input("enter flop aggression (20-40):")
                try:
                    dumbint = int(faggr)
                    if dumbint < 20 or dumbint > 40:
                        print("aggression not changed")
                    else:
                        faggression = str(dumbint)
                except:
                    print("aggression not changed")
                taggr = input("enter turn aggression (20-40):")
                try:
                    dumbint = int(taggr)
                    if dumbint < 20 or dumbint > 40:
                        print("aggression not changed")
                    else:
                        taggression = str(dumbint)
                except:
                    print("aggression not changed")
                raggr = input("enter river aggression (20-40):")
                try:
                    dumbint = int(raggr)
                    if dumbint < 20 or dumbint > 40:
                        print("aggression not changed")
                    else:
                        raggression = str(dumbint)
                except:
                    print("aggression not changed")

                rstp = input("enter range type p=polarized m=merged: ")
                if rstp == 'p':
                    rangecode = '1'
                    print("polarized")
                elif rstp == 'm':
                    rangecode = '0'
                    print("merged")
                else:
                    print("raising range type not changed")
                time.sleep(2)

                filesea = "fishes/" + fish + "/sea.dat"
                try:
                    with open(filesea, "w+") as f:
                        f.write(seacode)
                    f.close()
                except IOError:
                    print("no such fish: " + fish)
                    dumb = input("]")
                filerangetype = "fishes/" + fish + "/rt.dat"
                try:
                    with open(filerangetype, "w+") as f:
                        f.write(rangecode)
                    f.close()
                except IOError:
                    print("no such fish: " + fish)
                    dumb = input("]")
                paggressionfile = "fishes/" + fish + "/pa.dat"
                try:
                    with open(paggressionfile, "w+") as f:
                        f.write(paggression)
                    f.close()
                except IOError:
                    print("no such fish: " + fish)
                    dumb = input("]")
                faggressionfile = "fishes/" + fish + "/fa.dat"
                try:
                    with open(faggressionfile, "w+") as f:
                        f.write(faggression)
                    f.close()
                except IOError:
                    print("no such fish: " + fish)
                    dumb = input("]")
                taggressionfile = "fishes/" + fish + "/ta.dat"
                try:
                    with open(taggressionfile, "w+") as f:
                        f.write(taggression)
                    f.close()
                except IOError:
                    print("no such fish: " + fish)
                    dumb = input("]")
                raggressionfile = "fishes/" + fish + "/ra.dat"
                try:
                    with open(raggressionfile, "w+") as f:
                        f.write(raggression)
                    f.close()
                except IOError:
                    print("no such fish: " + fish)
                    dumb = input("]")

                settings.pokerpool.update_all()