#copyright (c) 2019
#jodathecoda@yahoo.com

import os
import shutil
import settings
import time

def run():
        cwd = os.getcwd()
        for f in settings.allfishes:
                src = cwd + "/fishes/bankroll.dat"
                dst = cwd + "/fishes/" + f + "/"
                try:
                        shutil.copy(src, dst)
                except:
                        print("Error in resetting bots bankrolls")
                        dumb = input("]")
        print("reset bankrolls done")
        time.sleep(2)
