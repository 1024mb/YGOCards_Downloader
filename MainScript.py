import Download
import time

def Start():
        Download.CreatePath()
        t = open("CardsDB.txt")
        ln = 0
        for ch in t:
            start = time.time()
            ln=ln+1

            ch = ch.rstrip('\n')
            if ch != "":
                size = Download.Download(ch+".jpg")

            end = time.time()
            elapsedtime = end - start

            linevar = 10699 - ln
            speed = 0
            if type(size) != type(None):
                try:
                    speed = ((int(size)/1024)/elapsedtime)
                except ZeroDivisionError:
                    pass
            percentage = 100 - round((linevar*50)/5349.5)
            if percentage > 99 and linevar !=0:
                    percentage = 99
            if ch != "":
                if speed == 0:
                    progr = "Skipping "+ch+".jpg"+"! Already Exists..."
                    print(progr)
                else:
                    progr = "Downloading "+ch+".jpg"+" @"+str(round(speed))+"kb/s "+str(linevar)+" cards left..."
                    print(progr)
                #self.progressBar.setValue(percentage)
        print("Task Completed ! Check you pics folder.")
        t.close()

Start()