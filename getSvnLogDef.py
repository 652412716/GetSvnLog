# coding=UTF-8
import os
import os.path
import time
import pysvn
# # import matplotlib
# import matplotlib.pyplot as plt
from log import *

client = pysvn.Client()
ignores = {"ignore", "commit", "testcode"}

svn_keyword = " "


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
def is_repeat(str):
    str1 = "ignore"
    for i in ignores:
        pos = str.rfind(i)
        if pos >= 0:
            return False
    return True


def writeAppSvnInfo(d):
    cfg = get_svn_config(basedir + "/" + pf + "_apprev.log")

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


def get_svn_log_style1(svn_path, start_timestamp, end_timestamp, keywords):
    log_debug(start_timestamp,"aimingChen start_timestamp")
    log_debug(end_timestamp,"aimingChen end_timestamp")
    revision_start = pysvn.Revision(pysvn.opt_revision_kind.date, start_timestamp)
    revision_end1 = pysvn.Revision(pysvn.opt_revision_kind.date, end_timestamp)

    log_list = client.log(svn_path, revision_start, revision_end1)

    dic = {}
    for log_info in log_list:

        log_info.message = log_info.message.replace("\n", "")

        if log_info.message != "":
            if is_repeat(log_info.message):
                if not (log_info.author in dic):
                    dic[log_info.author] = {"msg": "", "name": log_info.author, "date": "", "show_msg": ""}
                # else:
                if not rep(dic[log_info.author]["msg"], log_info.message):
                    dic[log_info.author]["msg"] += log_info.message
                    dic[log_info.author]["date"] += fmtDateTime(log_info.date)
                    dic[log_info.author]["show_msg"] += log_info.message + "  " + fmtDateTime(log_info.date) + "\n"

    log_text = "start log content\n"
    for key, value in dic.items():
        log_text += "\n\n\n\n------------------ " + key + " ---------------------------\n" + value["show_msg"]

        log_debug(key, "user name is:")
        count_log_msg_by_keyword(value["show_msg"], keywords)

    svn_text_log = open("svnLog_style1.txt", "w")
    svn_text_log.write(log_text)
    svn_text_log.close()


def count_log_msg_by_keyword(msg, keywords):

    for keyword in keywords:
        log_debug(keyword, "keyword is")
        lower_msg = msg.lower()
        keyword_count = lower_msg.count(keyword)
        log_debug(keyword_count, "count num:")
    print "\n"


def get_svn_log_style2(svn_path, start_timestamp, end_timestamp):
    revision_start = pysvn.Revision(pysvn.opt_revision_kind.date, start_timestamp)
    revision_end = pysvn.Revision(pysvn.opt_revision_kind.date, end_timestamp)
    log_list = client.log(svn_path, revision_start, revision_end)
    dic = {}
    for LogInfo in log_list:
        LogInfo.message = LogInfo.message.replace("\n", "")
        if LogInfo.message != "":
            if is_repeat(LogInfo.message) == True:
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


def get_svn_config(file_name):
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


def get_timestamp(data_time):
    split_data = data_time.split(',')
    timestamp = time.mktime((int(split_data[0]), int(split_data[1]), int(split_data[2]), 0, 0, 0, 0, 0, 0))
    return timestamp


def get_keyword(svn_keyword):
    keyword = svn_keyword.split(',')
    return keyword


#
# def draw_map():
#     print("draw_map!!!")
#     plt.plot([12, 34, 56, 78, 90])
#     plt.savefig('tmp.png')
#     plt.close('all')
