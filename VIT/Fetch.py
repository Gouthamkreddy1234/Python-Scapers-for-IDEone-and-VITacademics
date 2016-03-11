import urllib

def save():
  urllib.urlretrieve("https://academics.vit.ac.in/student/captcha.asp", "temp.bmp")

if __name__ == '__main__':
    save()