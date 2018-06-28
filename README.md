# wechat-personal-bot

開發「個人」微信機械人的紀錄

## 注意事項

-   個人微信如果是新辦的帳號，無法使用 wexin web api

## 資料特性分析

-   Rooms
-   Friends

### Rooms property

```
====Start 底下是 Room 所具備的屬性和其值====
MemberList : <class 'itchat.storage.templates.ContactList'>
Uin : <class 'int'>
UserName : <class 'str'>
NickName : <class 'str'>
HeadImgUrl : <class 'str'>
ContactFlag : <class 'int'>
MemberCount : <class 'int'>
RemarkName : <class 'str'>
HideInputBarFlag : <class 'int'>
Sex : <class 'int'>
Signature : <class 'str'>
VerifyFlag : <class 'int'>
OwnerUin : <class 'int'>
PYInitial : <class 'str'>
PYQuanPin : <class 'str'>
RemarkPYInitial : <class 'str'>
RemarkPYQuanPin : <class 'str'>
StarFriend : <class 'int'>
AppAccountFlag : <class 'int'>
Statues : <class 'int'>
AttrStatus : <class 'int'>
Province : <class 'str'>
City : <class 'str'>
Alias : <class 'str'>
SnsFlag : <class 'int'>
UniFriend : <class 'int'>
DisplayName : <class 'str'>
ChatRoomId : <class 'int'>
KeyWord : <class 'str'>
EncryChatRoomId : <class 'str'>
IsOwner : <class 'int'>
IsAdmin : <class 'NoneType'>
Self : <class 'itchat.storage.templates.User'>
====END 以上是 Room 所具備的屬性和其值====
```

### Friends property

```
====Start 底下是 Friend 所具備的屬性和其值====
MemberList : <class 'itchat.storage.templates.ContactList'>
UserName : <class 'str'>
City : <class 'str'>
DisplayName : <class 'str'>
PYQuanPin : <class 'str'>
RemarkPYInitial : <class 'str'>
Province : <class 'str'>
KeyWord : <class 'str'>
RemarkName : <class 'str'>
PYInitial : <class 'str'>
EncryChatRoomId : <class 'str'>
Alias : <class 'str'>
Signature : <class 'str'>
NickName : <class 'str'>
RemarkPYQuanPin : <class 'str'>
HeadImgUrl : <class 'str'>
UniFriend : <class 'int'>
Sex : <class 'int'>
AppAccountFlag : <class 'int'>
VerifyFlag : <class 'int'>
ChatRoomId : <class 'int'>
HideInputBarFlag : <class 'int'>
AttrStatus : <class 'int'>
SnsFlag : <class 'int'>
MemberCount : <class 'int'>
OwnerUin : <class 'int'>
ContactFlag : <class 'int'>
Uin : <class 'int'>
StarFriend : <class 'int'>
Statues : <class 'int'>
WebWxPluginSwitch : <class 'int'>
HeadImgFlag : <class 'int'>
====END 以上是 Friend 所具備的屬性和其值====
```
