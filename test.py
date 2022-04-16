import utils
import datetime
from time import strftime
from time import gmtime

sql = "select update_time from details order by id desc limit 1"
data_update_time = utils.mysql_query(sql)
aa = data_update_time[0][0]
print(str(aa)[0:-3])