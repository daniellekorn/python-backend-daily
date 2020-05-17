from datetime import datetime, timedelta
import random


# function to generate random recent date for realistic post creation time
def created_at():
    end = datetime.now()
    start = end - timedelta(weeks=30)
    random_date = start + (end - start) * random.random()
    str_date = random_date.strftime('%m/%d/%Y %H:%M:%S')
    return str_date
