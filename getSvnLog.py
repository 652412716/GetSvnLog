# coding=UTF-8

from getSvnLogDef import *

config_msg = get_svn_config("svnLogConfig.txt")
client.callback_get_login = get_login

svn_path = config_msg["SVN_PATH"]
start_date = config_msg["SVN_START_DATE"]
end_date = config_msg["SVN_END_DATE"]
svn_keyword = config_msg["SVN_KEYWORD"]

start_timestamp = get_timestamp(start_date)
end_timestamp = get_timestamp(end_date)
keywords = get_keyword(svn_keyword)

log_debug(svn_path, "svn path is:")
log_debug(start_date, "start time is:")
log_debug(end_date, "end time is:")

get_svn_log_style1(svn_path, start_timestamp, end_timestamp, keywords)
get_svn_log_style2(svn_path, start_timestamp, end_timestamp)

# a = "Sat Mar 28 22:24:24 2016"
# print "5151515", time.strptime(a, "%a %b %d %H:%M:%S %Y")
# print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
