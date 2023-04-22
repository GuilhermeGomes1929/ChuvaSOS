import pandas as pd
from process.process_data import *

def process_data(data):
    local_tags = data[0]
    last_24hours_tags = data[1]
    date_time_tags = data[2]

    locals = list(map(get_tag_content, local_tags))
    last_24hours = list(map(get_tag_content, last_24hours_tags))
    date_time = concat_date_and_time(date_time_tags)

    psdf = pd.DataFrame.from_dict(
        {
            'Locals': locals,
            'Time-Date' : date_time,
            'Last-24-hours': last_24hours,
        }
    )

    return psdf