# -*- coding: utf-8 -*-

import itchat
from itchat.content import *

def listRoomProps():
    print("====Start 底下是 Room 所具備的屬性和其值====")
    for room in itchat.get_chatrooms(update=True):
        for prop in room:
            print("%s : %s" % (prop,type(room[prop])))
        break
    print("====END 以上是 Room 所具備的屬性和其值====")

def listFriendProps():
    print("====Start 底下是 Friend 所具備的屬性和其值====")
    for room in itchat.get_friends(update=True):
        for prop in room:
            print("%s : %s" % (prop,type(room[prop])))
        break
    print("====END 以上是 Friend 所具備的屬性和其值====")

if __name__=="__main__":

    itchat.auto_login(hotReload=True, enableCmdQR=2)
    listRoomProps()
    listFriendProps()
    
