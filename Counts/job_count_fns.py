import re
import time
import pandas as pd
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



options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options,
                          service=ChromeService(
                                ChromeDriverManager().install()
                                ))


def get_audi():
    url = "https://karriere.audi.de/sap/bc/bsp/sap/z_hcmx_ui_ext/desktop.html?csref=dsp:Audi:bc:Audi_Career:a:Youtube:youtube.com:mt~o&#/SEARCH/RESULTS"
    driver.get(url)
    jobs_count = driver.find_element(By.XPATH, "/html/body/section/div/div[7]/div[2]/div[2]/div/section/div[3]/div[1]/div/div/section/div/div[2]/div/section/aside/div/section/h1/span[1]").get_attribute("innerHTML")

    return ["Audi", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_bmw():
    url = "https://www.bmwgroup.jobs/us/en.html"
    driver.get(url)
    jobs_count = driver.find_element(By.CLASS_NAME, "grp-jobfinder-counter").text
    jobs_count = list(map(int, re.findall('\d+', jobs_count)))
    
    return ["BMW", jobs_count[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_bosch():
    url = "https://www.bosch.de/en/career/job-offers/?sortBy=releasedDate"
    driver.get(url)
    time.sleep(10)
    jobs_count = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, 
                                    '/html/body/main/section[1]/div/o-job-search-dynamic-component/div/div[1]/div'))).get_attribute("innerHTML")

    return ["Bosch", jobs_count.split()[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_catl():
    url = "https://www.catl-career.com/search/?createNewAlert=false&q=&locationsearch="
    driver.get(url)
    jobs_count = driver.find_element(By.CLASS_NAME, "paginationLabel").text
    
    return ["CATL", jobs_count.split(" ")[-1], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_continental():
    url = "https://jobs.continental.com/en/?ac=search_result&search_criterion_language[]=EN&search_criterion_channel[]=12&language=2#/"
    driver.get(url)
    jobs_count = driver.find_element(By.XPATH, 
                    '/html/body/div[2]/main/app-root/index-page/div/div/div/app-result-list-header/div/div/div[1]/h3').text
    jobs_count = list(map(int, re.findall('\d+', jobs_count[-30:])))

    return ["Continental", jobs_count[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_cruise():
    url = "https://getcruise.com/careers/jobs/"
    driver.get(url)
    categories_div = driver.find_elements(By.CLASS_NAME, 'jobs-module--jobTableContent--03b94')
    jobs_count = 0
    for cat in categories_div:
        soup = BeautifulSoup(cat.get_attribute('outerHTML'), "html.parser")    
        for job in soup.find_all(class_ = "job-table-module--jobRow--3f4c2"):
            jobs_count +=1

    return ["Cruise", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_denso():
    url = "https://hcwt.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/requisitions"
    driver.get(url)
    time.sleep(10)
    jobs_count = driver.find_element(By.XPATH, 
        '/html/body/div[3]/div[1]/div/div[1]/div[2]/div/div/div/section/div/div[2]/div/div/div/div/search-filters-panel-horizontal/div/div/div/div/h1').get_attribute("innerHTML")

    return ["Denso", jobs_count.split()[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_faurecia():  
    url = "https://jobs.faurecia.com/careers"
    driver.get(url)
    text = driver.page_source

    pattern = r"(\d+)\s+open jobs."
    jobs_count = re.findall(pattern, text)

    return ["Faurecia", int(jobs_count[0]), dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_ford():
    url = "https://efds.fa.em5.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1"
    driver.get(url)
    jobs_count = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li.categories-list__group:nth-child(1)"))).text
    jobs_count = jobs_count.split(" ")[-1].replace("(", "").replace(")", "")

    return ["Ford", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_gatik():
    url = "https://boards.greenhouse.io/gatikaiinc"
    driver.get(url)
    categories_div = driver.find_elements(By.CLASS_NAME, "level-0")
    jobs_count = 0
    for cat in categories_div:
        soup = BeautifulSoup(cat.get_attribute('outerHTML'), "html.parser")    
        for job in soup.find_all(class_ = "opening"):
            jobs_count +=1

    return ["Gatik", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_genmotors():
    url = "https://generalmotors.wd5.myworkdayjobs.com/Careers_GM"
    driver.get(url)
    time.sleep(10)
    jobs_count = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, 
                                    '/html/body/div/div/div/div[3]/div/div/div[2]/section/p'))).get_attribute("innerHTML")

    return ["General Motors", jobs_count.split()[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_hella():
    url = "https://hella.csod.com/ux/ats/careersite/3/home?c=hella"
    driver.get(url)
    driver.find_element(By.XPATH, 
        '/html/body/div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div[2]/div/div/div/div[4]').click()
    time.sleep(10)
    jobs_count = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div/h3').text

    return["Hella", jobs_count.split()[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_honda():
    url = "https://hondana.taleo.net/careersection/ah_ext/jobsearch.ftl"
    driver.get(url)
    time.sleep(10)
    jobs_count = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, 
                '//*[@id="hidDivForAccessInfoPanel"]'))).get_attribute("innerHTML")

    return ["Honda", jobs_count.split()[-1], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_hyundai():
    url = "https://careersautomotive.com/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_department=&optionsFacetsDD_facility=&optionsFacetsDD_state="
    driver.get(url)
    jobs_count = driver.find_element(By.XPATH, 
        '/html/body/div/div[2]/div/div/div[3]/div/div/div/span[1]/b[2]').get_attribute("innerHTML")

    return ["Hyundai", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_kia():
    url = "https://careers.kiausa.com/search/?createNewAlert=false&q=&locationsearch="
    driver.get(url)
    jobs_count = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[3]/div/div/div/span[1]/b[2]").get_attribute("innerHTML")
    return ["Kia", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_lear():
    url = "https://jobs.lear.com/search/?createNewAlert=false&q=&locationsearch="
    driver.get(url)
    jobs_count = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div/div/div/span[1]').text

    return ["Lear", jobs_count.split()[-1], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_magna():
    url = "https://jobs.magna.com/search/?createNewAlert=false&q=&locationsearch="
    driver.get(url)
    jobs_count = driver.find_element(By.XPATH, '//*[@id="caption"]').get_attribute("innerHTML")
    return ["Magna", jobs_count.split(";")[-1].strip(), dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_maymobility():
    url = "https://maymobility.com/careers#greenhouse"
    driver.get(url)
    cat_iframe = driver.find_elements(By.XPATH, "/html/body/div[1]/main/div[2]/div/iframe")
    driver.switch_to.frame(cat_iframe[0])

    categories_div = driver.find_elements(By.CLASS_NAME, "level-0")
    jobs_count = 0
    for cat in categories_div:
        soup = BeautifulSoup(cat.get_attribute('outerHTML'), "html.parser")    
        for job in soup.find_all(class_ = "opening"):
            jobs_count +=1

    return ["May Mobility", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_merc_benz():
    url = "https://group.mercedes-benz.com/careers/job-search/?r=dai"
    driver.get(url)
    time.sleep(10)
    jobs_count = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, 
                                                                               '/html/body/section/div[2]/div[2]/div[1]/div[1]/h1/span'))).text
    return ["Mercedes-Benz", int(jobs_count.split(" ")[0].replace(',', '')), dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_mobileye():
    url = "https://careers.mobileye.com/jobs"
    driver.get(url)
    categories_div = driver.find_elements(By.CLASS_NAME, 'dep_box')
    card_counter = 0
    for cat in categories_div:
        soup = BeautifulSoup(cat.get_attribute('outerHTML'), "html.parser")    
        for card in soup.find_all(class_ = "card"):
            card_counter +=1

    return ["Mobileye", card_counter, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_motional():
    url = "https://motional.com/open-positions#/"
    driver.get(url)
    time.sleep(10)
    jobs_count = driver.find_element(By.XPATH, 
        '/html/body/div/div/div/main/div/div/article/div/div/div[1]/div/div/div/div[2]/div/section[2]/div/p').get_attribute("innerHTML")

    return ["Motional", int(re.findall(r'>(.+?)<', jobs_count)[-1]), dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_nissan():
    url = "https://alliance.wd3.myworkdayjobs.com/nissanjobs"
    driver.get(url)
    time.sleep(10)
    jobs_count = driver.find_element(By.XPATH, 
        '/html/body/div/div/div/div[4]/div/div/div[2]/section/p').get_attribute("innerHTML")

    return ["Nissan", jobs_count.split()[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_porshe():
    url = "https://jobs.porsche.com/index.php?ac=search_result"
    driver.get(url)
    jobs_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, 
                '/html/body/div[1]/main/div[3]/h1/span/span'))).get_attribute("innerHTML")

    return ["Porshe", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_rivian():
    url = "https://careers.rivian.com/careers-home/jobs"
    driver.get(url)
    jobs_count = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, 
                                '//*[@id="search-results-indicator"]'))).text
    
    return ["Rivian", jobs_count.split()[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_stellantis():
    url = "https://careers.stellantis.com/job-search-results/"
    driver.get(url)
    jobs_count = driver.find_element(By.XPATH, 
                                '//*[@id="live-results-counter"]').get_attribute("innerHTML")
    
    return ["Stellantis", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_tesla():
    current_date = dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles")).date()
    df = pd.read_csv(f"/tesla/tesla_locs_{current_date}_withregion.csv")

    return ["Tesla", df.shape[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]
    


def get_toyota():
    url = "https://careers.toyota.com/us/en/search-results?keywords="
    driver.get(url)
    jobs_count = driver.find_element(By.XPATH, 
                                '/html/body/div[2]/div[3]/div/div/div/div[2]/section[2]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/span[1]').get_attribute("innerHTML")
    
    return ["Toyota", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_valeo():
    url = "https://valeo.wd3.myworkdayjobs.com/en-US/valeo_jobs"
    driver.get(url)
    time.sleep(10)
    jobs_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, 
                '/html/body/div/div/div/div[4]/div/div/div[2]/section/p'))).text

    return ["Valeo", jobs_count.split()[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_volkswagen():
    url = "https://karriere.volkswagen.de/sap/bc/bsp/sap/zvw_hcmx_ui_ext/desktop.html#/SEARCH/RESULTS"
    driver.get(url)
    time.sleep(15)
    jobs_count = driver.find_element(By.XPATH, 
        '/html/body/section/div/div[7]/div[2]/div[2]/div/section/div[3]/div[2]/div/div/section/div[1]/h4').text
    
    return ["Volkswagen", jobs_count.split()[0], dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]


def get_waymo():
    url = "https://waymo.com/careers/#roles"
    driver.get(url)
    categories_div = driver.find_elements(By.CLASS_NAME, 'careers-roles__jobs__categories__item')
    jobs_count = 0
    for cat in categories_div:
        soup = BeautifulSoup(cat.get_attribute('outerHTML'), "html.parser")    
        for job in soup.find_all(class_ = "careers-roles__jobs__categories__job"):
            jobs_count +=1

    return ["Waymo", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]



def get_zf():
    url = "https://jobs.zf.com/search/?createNewAlert=false&q=&optionsFacetsDD_facility=&optionsFacetsDD_shifttype=&optionsFacetsDD_country=&locationsearch="
    driver.get(url)
    jobs_count = driver.find_element(By.XPATH, 
                                '/html/body/div/div[2]/div/div/div[3]/div/div/div/span[1]/b[2]').get_attribute("innerHTML")
    
    return ["ZF", jobs_count, dt.fromtimestamp(time.time(), tz=ZoneInfo("America/Los_Angeles"))]













































    





