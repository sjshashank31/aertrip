import re, dateparser
from datetime import datetime, timedelta

travel_dict = {
    "source": "",
    "destination": "",
    "date" : ""
}

return_dict = {
    "source": "",
    "destination": "",
    "date" : ""
}


def query_parser(query):
    patterns = [
                "from [A-Za-z]+ to [A-za-z]+ on [A-Za-z]+",
                "to [A-Za-z]+ from [A-za-z]+ on [A-Za-z]+",
                "to [A-Za-z]+ from [A-za-z]+ on [A-Za-z]+ and return on [A-Za-z]+",
                "to [A-Za-z]+ on [A-Za-z]+ and return on [A-Za-z]+",

    ]

    for pattern in patterns:
        a = re.findall(pattern, query)
        if a:
            print(a)
            a = a[0].split()

            if "from" in a:
                from_index = a.index("from")
                travel_dict["source"] = a[from_index + 1]

            if "to" in a:
                to_index = a.index("to")
                travel_dict["destination"] = a[to_index + 1]

            if "on" in a:
                on_index = a.index("on")
                travel_dict["date"] = dateparser.parse(a[on_index+1])
                if travel_dict["date"]< datetime.now():
                    travel_dict["date"] = travel_dict["date"] + timedelta(days=7)

            if "return" in a:
                return_dict["source"] = travel_dict['destination']
                return_dict["destination"] = travel_dict["source"]
                return_index = a.index("return")
                date = dateparser.parse(a[return_index+2])
                print(date)
                while date < travel_dict["date"]:
                    date = date+timedelta(days=7)
                return_dict["date"] = date

    return [travel_dict, return_dict]

