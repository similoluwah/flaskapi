import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta 

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

def generate_data(filename, nrows = 50):
    """
        Description : This script generates random data for testing the API (columns - phone_number (int), run_time (datetime))
    """

    network_prefix = [803,703, 903,806,706,813,810,814,816,805,705,905,807,815,811,905,809,909,817,818,802,902,701,808,708,812]
    phone_numbers = ["234"+ str(random.choice(network_prefix)) + "".join(map(str, random.sample(range(0,10),7))) for _ in range(nrows)]
    run_time = [random_date(datetime.strptime('1/1/2020 1:30 PM', '%m/%d/%Y %I:%M %p'), datetime.strptime('12/31/2020 4:50 AM', '%m/%d/%Y %I:%M %p')) for _ in range(nrows)]

    df = pd.DataFrame({"phone_number" : phone_numbers, "run_time" : map(str, run_time)})
    try:
        if filename.endswith(".xlsx"):
            df.to_excel(filename, engine = "xlsxwriter", index = False)
        else:
            df.to_csv(filename, index = False)
        print(f"Successfully generated and saved {filename}")
    except Exception as e:
        print(f"An Error occurred - {e}")


generate_data("test1.csv")
generate_data("test1.xlsx")