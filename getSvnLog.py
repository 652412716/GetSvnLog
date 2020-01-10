# -*- coding: utf8 -*-'

from log import *
from getSvnLogDef import *

config_msg = GetSvnConfig("svnLogConfig.txt")

svn_path = config_msg["SVN_PATH"]
start_date = config_msg["SVN_START_DATE"]
end_date = config_msg["SVN_END_DATE"]

start_timestamp = GetTimestamp(start_date)
end_timestamp = GetTimestamp(end_date)

LogDebug(svn_path, "svn path is:")
LogDebug(start_date, "start time is:")
LogDebug(end_date, "end time is:")


GetSvnLog_Style1(svn_path, start_timestamp, end_timestamp)
GetSvnLog_Style2(svn_path, start_timestamp, end_timestamp)

# a = "Sat Mar 28 22:24:24 2016"
# print "5151515", time.strptime(a, "%a %b %d %H:%M:%S %Y")
# print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
