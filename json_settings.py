import json

json_settings = json.dumps([
    {
        "type": "numeric",
        "title": "Lower Limit",
        "desc": "Lowest number to be used when asking questions",
        "section": "General",
        "key": "lower_num"
    },
    {
        "type": "numeric",
        "title": "Upper Limit",
        "desc": "Highest number to be used when asking questions",
        "section": "General",
        "key": "upper_num"
    }
])
