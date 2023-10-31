import re

dates = ["01-01-2022", "31-12-2022", "2022-01-01"]
pattern = r'\d{2}-\d{2}-\d{4}'
for date in dates:
    if re.match(pattern, date):
        print(date, "is a valid date in DD-MM-YYYY format.")
    else:
        print(date, "is not a valid date.")
