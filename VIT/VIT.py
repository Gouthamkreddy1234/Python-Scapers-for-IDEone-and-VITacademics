import requests
import urllib
from CaptchaParser import *  # from the file import all functions
from PIL import Image  # file from a folder
from bs4 import BeautifulSoup


# session based captcha,retreives the same captcha while in the same session and passing in the same set cookies of the session
# cookies and session


class scrape:
    string = ""

    def loadimage(self):
        print "check"
        img = Image.open("D:\output.bmp")  # pass file contents and not the file
        parser = CaptchaParser()
        captcha = parser.getCaptcha(img)
        self.string = str(captcha)
        print str(captcha)

    def req(self):

        print "hello"

        '''session.get("https://academics.vit.ac.in");

        session.get("https://academics.vit.ac.in/student/stud_login.asp",cookies=session.cookies);
        print session.cookies'''
        session = requests.Session()  # most

        # urllib.urlretrieve("https://academics.vit.ac.in/student/captcha.asp", "temp.bmp")
        r = session.get("https://academics.vit.ac.in/student/captcha.asp", stream=True)
        try:
            with open("D:\output.bmp", 'w') as f:
                for chunk in r.iter_content():
                    f.write(chunk)
            self.loadimage()
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            print "error"
        d = {"regno": "13BCE0459", "passwd": "123456boigoutha", "vrfcd": self.string, "message": ""}

        session.post('https://academics.vit.ac.in/student/stud_login_submit.asp',
                     data=d)  # validate with a captacha in the form
        # this captcha is the same as the one that we have beacuse os the mainteained session and the session cookies
        r = session.get("https://academics.vit.ac.in/student/stud_riviera_home.asp");

        r = session.get("https://academics.vit.ac.in/student/content.asp")

        r = session.get("https://academics.vit.ac.in/student/stud_home.asp")
        da = {"perdetcmd": "Skip Now"}
        r = session.post("https://academics.vit.ac.in/student/stud_riviera_home_submit.asp", data=da)

        r = session.get("https://academics.vit.ac.in/student/stud_menu.asp")
        r = session.get("https://academics.vit.ac.in/student/timetable_ws.asp")
        print r.content
        return r.content
        # parse this entire response properly and convert to json
