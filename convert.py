import datetime
import pytz

def updateTimezone (toConvert):
  datetimeUTC = datetime.datetime.strptime(toConvert, "%Y-%m-%dT%H:%M:%SZ")
  datetimeEST = datetimeUTC.astimezone(pytz.timezone("US/Eastern")).strftime('%m/%d/%Y %I:%M %p')
  output = datetimeEST
  
  print (output)

updateTimezone('2019-07-01T00:00:00Z')