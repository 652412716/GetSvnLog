# -*- coding: utf8 -*-'
import os
import os.path
import time
import pysvn
from log import *


client = pysvn.Client()


# 排除相同日志
def rep(str, samestr):
    strs = str.split('\&')
    if len(strs) <= 0:
        return False
    for s in strs:
        if s == samestr:
            return True
    return False


# 排除过滤
def repignore(str):
    str1 = "ignore"
    for i in ignores:
        pos = str.rfind(i)
        if pos >= 0:
            return False
    return True


ignores = {"ignore", "commit", "testcode"}


def writeAppSvnInfo(d):
    cfg = GetSvnConfig(basedir + "/" + pf + "_apprev.log")

    info = client.info(d + "/main")
    cfg["prev"] = cfg.get("rev") or 0
    cfg["rev"] = info.revision.number
    writeIni(cfg, basedir + "/" + pf + "_apprev.log")


def writeIni(cfg, fn):
    cfgf = open(fn, "w")
    print cfg
    for k in cfg:
        cfgf.write(k + "=" + str(cfg[k]) + "\n")
    cfgf.close()


def fmtDateTime(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))


def GetSvnLog_Style1(svn_path, y, m, d, ty, tm, td):
    start_date = time.mktime((int(y), int(m), int(d), 0, 0, 0, 0, 0, 0))
    print 'start_data:', start_date
    end_date = time.mktime((int(ty), int(tm), int(td), 0, 0, 0, 0, 0, 0))
    print 'end_date = ', end_date
    revision_start = pysvn.Revision(pysvn.opt_revision_kind.date, start_date)
    revision_end1 = pysvn.Revision(pysvn.opt_revision_kind.date, end_date)
    LogList = client.log(svn_path, revision_start, revision_end1)
    dic = {}
    for LogInfo in LogList:
        LogInfo.message = LogInfo.message.replace("\n", "")
        if LogInfo.message != "":
            if repignore(LogInfo.message) == True:
                if dic.has_key(LogInfo.author) == False:
                    dic[LogInfo.author] = {"msg": "", "name": LogInfo.author, "date": "", "showmsg": ""}
                # else:
                if rep(dic[LogInfo.author]["msg"], LogInfo.message) == False:
                    dic[LogInfo.author]["msg"] += LogInfo.message + "\&"
                    dic[LogInfo.author]["date"] += fmtDateTime(LogInfo.date)
                    dic[LogInfo.author]["showmsg"] += LogInfo.message + "  " + fmtDateTime(LogInfo.date) + "\n"
    s1 = "start log content\n"
    for key, value in dic.items():
        s1 += "\n\n\n\n------------------ " + key + " ---------------------------\n" + value["showmsg"]
    f = open("svnLog_style1.txt", "w")
    f.write(s1)
    f.close()


def GetSvnLog_Style2(svn_path, y, m, d, ty, tm, td):
    start_date = time.mktime((int(y), int(m), int(d), 0, 0, 0, 0, 0, 0))
    end_date = time.mktime((int(ty), int(tm), int(td), 0, 0, 0, 0, 0, 0))
    revision_start = pysvn.Revision(pysvn.opt_revision_kind.date, start_date)
    revision_end1 = pysvn.Revision(pysvn.opt_revision_kind.date, end_date)
    LogList = client.log(svn_path, revision_start, revision_end1)
    dic = {}
    for LogInfo in LogList:
        LogInfo.message = LogInfo.message.replace("\n", "")
        if LogInfo.message != "":
            if repignore(LogInfo.message) == True:
                if dic.has_key(LogInfo.author) == False:
                    dic[LogInfo.author] = {"msg": "", "name": LogInfo.author, "date": "", "showmsg": ""}
                # else:
                if rep(dic[LogInfo.author]["msg"], LogInfo.message) == False:
                    dic[LogInfo.author]["msg"] += LogInfo.message + "\&"
                    dic[LogInfo.author]["date"] += fmtDateTime(LogInfo.date)
                    # dic[LogInfo.author]["showmsg"]+=LogInfo.message+","+LogInfo.author+", tm="+fmtDateTime(LogInfo.date)+"\n"
                    dic[LogInfo.author]["showmsg"] += "tm=" + fmtDateTime(
                        LogInfo.date) + "," + LogInfo.message + "," + LogInfo.author + "\n"

    s1 = "start log content\n"
    for key, value in dic.items():
        s1 += value["showmsg"] + "\n"
    f = open("svnLog_style2.csv", "w")
    f.write(s1)
    f.close()


def GetSvnConfig(file_name):
    if not os.path.exists(file_name):
        print "config file not exists >>>", file_name
        return {}

    print "read config file :", file_name
    config_file = open(file_name)
    config_msg = {}

    print "get svn config message:"
    for svnConfigMsg in config_file.readlines():
        split_msg = svnConfigMsg.strip().split("=")
        print svnConfigMsg
        if len(split_msg) == 2:
            config_msg[split_msg[0]] = split_msg[1]

    return config_msg


def get_login(realm, username, may_save):
    print "111111111"
    print realm, username
    global cfg
    id = realm.split(" ")[1]
    print "id=", id
    return (True, cfg["SVN_USERNAME"], cfg["SVN_PASSWORD"], True)


def GetTimestamp(data_time):
    print("aimingChen")


config_msg = GetSvnConfig("svnLogConfig.txt")
print config_msg, "aimingChen 1111111"
# client.callback_get_login = get_login

start_date = config_msg["SVN_START_DATE"].split(',')


LogDebug(start_date, "aimingChen 1111111")



end_date = config_msg["SVN_END_DATE"].split(',')
svn_path = config_msg["SVN_PATH"]


a = "Sat Mar 28 22:24:24 2016"
print "5151515", time.strptime(a, "%a %b %d %H:%M:%S %Y")
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

print start_date[0]
print start_date[1]
print start_date[2]

print end_date[0]
print end_date[1]
print end_date[2]




GetSvnLog_Style1(svn_path, start_date[0], start_date[1], start_date[2], end_date[0], end_date[1], end_date[2])
GetSvnLog_Style2(svn_path, start_date[0], start_date[1], start_date[2], end_date[0], end_date[1], end_date[2])
