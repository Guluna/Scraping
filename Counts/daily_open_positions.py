import re
import time
import pandas as pd
from job_count_fns import *
from bs4 import BeautifulSoup
from zoneinfo import ZoneInfo
from datetime import datetime as dt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():   
    df = pd.DataFrame(columns = ["automaker", "open_positions", "timestamp"])  
    current_date = dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles")).date()
    
    # calling each fn via list
    my_fns = [get_audi, get_bmw, get_bosch, get_catl, get_continental, 
             get_cruise, get_denso, get_faurecia, get_ford, get_gatik,
             get_genmotors, get_hella, get_honda, get_hyundai, get_kia,
             get_lear, get_magna, get_maymobility, get_merc_benz, get_mobileye,
             get_motional, get_nissan, get_porshe, get_rivian, get_stellantis,
             get_tesla, get_toyota, get_valeo, get_volkswagen, get_waymo,
             get_zf]
    
    # save errors log
    with open(f"errorslog_{current_date}.txt", "w") as f:
        for fn in my_fns:
            try:    
                df.loc[len(df)] = fn()
                print(fn, "done")
            except Exception as error:
                print(fn, "Error occured: \n", error)
                f.write(f"\nFailed to scrape {fn}\n {str(error)} \n *************** \n")
  
    df.to_csv(f"daily_open_postions_{current_date}.csv", index=False, mode='a')
    print("complete!")

    print(df)


main()