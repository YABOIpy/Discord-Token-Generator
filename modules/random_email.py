import random,os,sys,string,names



def getemail():
    return ''.join(random.choice(string.ascii_letters) for x in range(16)) + "@yaboi" + ".com"#+ ''.join(random.choice(string.ascii_letters) for x in range(7))  