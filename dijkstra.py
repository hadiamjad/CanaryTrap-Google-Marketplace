import json
import time
import pandas as pd
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter

# download the app with specified app url
def GsuiteAppDownload(appurl):
    opt = webdriver.ChromeOptions()
    opt.add_argument(r"user-data-dir=C:\Users\Haadi\AppData\Local\Google\Chrome\User Data")
    opt.add_argument('--profile-directory=Profile 1')
    # chrome web driver
    driver = webdriver.Chrome(options=opt)

    driver.get(appurl)
    # delay
    time.sleep(5)
    # install btn click
    btn = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/c-wiz/div[2]/div[1]/div/div/div[2]/div/div/button[2]")
    btn.click()
    # delay
    time.sleep(5)
    # continue click
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[5]/div/div[2]/div[3]/div[2]/span/span").click()
    # delay
    time.sleep(5)
    # windows handler
    handlers = driver.window_handles
    driver.switch_to.window(handlers[1])
    # account re-vist click
    driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div").click()
    # delay
    time.sleep(5)
    try:
        # allow permissions click
        driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
        time.sleep(5)
    except:
        time.sleep(3)
    driver.quit()

# delete google app with specified app url
def GsuiteAppDelete(appurl):
    opt = webdriver.ChromeOptions()
    opt.add_argument(r"user-data-dir=C:\Users\Haadi\AppData\Local\Google\Chrome\User Data")
    opt.add_argument('--profile-directory=Profile 1')
    # chrome web driver
    driver = webdriver.Chrome(options=opt)

    driver.get(appurl)
    # delay
    time.sleep(5)
    # uninstall btn click
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/c-wiz/div[2]/div[1]/div/div/div[2]/div/div/button[1]/div[2]").click()
    # confirmation pop-up btn click
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[5]/div/div[2]/div[3]/div[2]/span/span").click()
    # delay
    time.sleep(5)

    driver.quit()

# Check the given list for the Apps which are no longer supported.
def cleaningJSON():
    json_url = urlopen("https://irwinreyes.com/assets/files/2020-conpro/scrape-20200102.json")
    dic = json.loads(json_url.read())
    count = 0

    for apps in dic["data"]:
        try:
            if count < 240:
                print(count)
                count+=1
            else:
                opt = webdriver.ChromeOptions()
                opt.add_argument(r"user-data-dir=C:\Users\Haadi\AppData\Local\Google\Chrome\User Data")
                opt.add_argument('--profile-directory=Profile 1')
                # chrome web driver
                driver = webdriver.Chrome(options=opt)
                driver.implicitly_wait(6)
                driver.get(apps["app_url"])
                # delay
                time.sleep(5)
                # install btn click
                btn = driver.find_element_by_xpath(
                    "//*[@id='yDmH0d']/c-wiz/div/c-wiz/div[2]/div[1]/div/div/div[2]/div/div/button[2]")
                if btn.is_enabled():
                    btn.click()
                    # delay
                    time.sleep(5)
                    # continue click
                    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[5]/div/div[2]/div[3]/div[2]/span/span").click()
                    # delay
                    time.sleep(5)
                    # windows handler
                    handlers = driver.window_handles
                    driver.switch_to.window(handlers[1])
                    # account re-vist click
                    driver.find_element_by_xpath(
                        "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div").click()
                    time.sleep(5)
                    if len(driver.window_handles) == 1:
                        driver.switch_to.window(handlers[0])
                    elif "danger" in driver.current_url:
                        print(apps["app_url"])
                else:
                    print(apps["app_url"])
                print(count)
                count += 1
                driver.quit()
        except:
            print(count)
            count += 1
            print(apps["app_url"])
            driver.quit()

# List1 - List2
def List_cleaning_helper():
    json_url = urlopen("https://irwinreyes.com/assets/files/2020-conpro/scrape-20200102.json")
    dic = json.loads(json_url.read())
    list1 = []
    list2 = []
    for apps in dic["data"]:
        list1.append(apps["app_url"])

    df = pd.read_excel('rem.xlsx')
    for ind in df.index:
        list2.append(df['topic'][ind])

    for a in list2:
        if a in list1:
            list1.remove(a)
        else:
            print(a)

# send verification email
def VerificationEmail(new_email):
    opt = webdriver.ChromeOptions()
    opt.add_argument(r"user-data-dir=C:\Users\Haadi\AppData\Local\Google\Chrome\User Data")
    opt.add_argument('--profile-directory=Profile 1')
    # chrome web driver
    driver = webdriver.Chrome(options=opt)

    driver.get("https://myaccount.google.com/?pli=1")
    # delay
    time.sleep(5)
    # personal info btn click
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/c-wiz/div/div[1]/div[3]/c-wiz/nav/ul/li[2]/a/div[2]").click()
    # delay
    time.sleep(5)
    # personal info btn click
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/c-wiz/c-wiz/div/div[3]/div/div/c-wiz/section/div[2]/article/div/div/div[2]/div/a").click()
    # delay
    time.sleep(5)
    # personal info btn click
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[3]/c-wiz/div/div[3]/div[1]/a").click()
    # delay
    time.sleep(5)
    if "v2" not in driver.current_url:
        driver.quit()
        VerificationEmail(new_email)
    # password enter
    pwd = driver.find_element_by_name("password")
    pwd.send_keys("hadi1234")
    # next btn
    nxt = driver.find_element_by_class_name("VfPpkd-RLmnJb")
    nxt.click()
    # delay
    time.sleep(5)
    # edit email  info btn click
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div[3]/c-wiz/div/div[3]/div[1]/div/div/div/div[2]/div/span/span/span").click()
    # delay
    time.sleep(5)
    # new_email enter
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[11]/div/div[2]/span/div/div[1]/div[1]/div/div[1]/input").send_keys(new_email)
    # delay
    time.sleep(5)
    # send email verification btn click
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[11]/div/div[2]/div[3]/div[2]/span/span").click()
    # delay
    time.sleep(5)
    # ok btn click
    driver.find_element_by_xpath("//*[@id='yDmH0d']/div[11]/div/div[2]/div[3]/div/span/span").click()
    # delay
    time.sleep(5)
    # re-send verification btn click
    #driver.find_element_by_xpath("//*[@id='ow23']/div/div[3]/div[1]/div/div[2]/div/div[1]/div[4]/div/div/span/span").click()
    #driver.find_element_by_class_name("RveJvd").click()
    # delay
    #time.sleep(5)
    # re-send verification okay btn click
    #driver.find_element_by_xpath("//*[@id='yDmH0d']/div[11]/div/div[2]/div[3]/div[2]/span/span").click()
    # delay
    #time.sleep(5)

    driver.quit()

    EmailRotation(new_email)


# email rotation using sogo
def EmailRotation(new_email):
    #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

    # Now opening SoGo for verification
    opt = webdriver.ChromeOptions()
    opt.add_argument(r"user-data-dir=C:\Users\Haadi\AppData\Local\Google\Chrome\User Data")
    opt.add_argument('--profile-directory=Profile 1')
    # chrome web driver
    driver = webdriver.Chrome(options=opt)

    driver.get("http://mail.danial.live/SOGo/")
    # delay
    time.sleep(15)
    # new_email enter
    driver.find_element_by_xpath("//*[@id='input_1']").send_keys(new_email)
    # new_email_password enter
    driver.find_element_by_xpath("//*[@id='input_2']").send_keys("helloworld")
    # -> arrow click
    driver.find_element_by_xpath("//*[@id='login']/form/div[3]/button[2]").click()
    # delay
    time.sleep(15)
    driver.find_element_by_xpath("/html/body/main/section/div/div[1]/md-toolbar[2]/div/button[2]/md-icon").click()
    time.sleep(3)
    # select first verification email
    driver.find_element_by_xpath("//*[@id='messagesList']/md-virtual-repeat-container/div/div[2]/md-list/md-list-item[1]/div/button").click()
    time.sleep(5)
    #print(driver.find_element_by_xpath("//*[@id='detailView']/div/div[1]/md-card/md-card-content/div[1]/h5").text)
    if driver.find_element_by_xpath("//*[@id='detailView']/div/div[1]/md-card/md-card-content/div[1]/h5").text != "Google Accounts: Email Change Verification":
        # disconnect sogo
        driver.find_element_by_xpath("/html/body/main/section/md-toolbar[1]/div[2]/a[6]/md-icon").click()
        # delay
        time.sleep(8)
        driver.quit()
        VerificationEmail(new_email)
        return
    else:
        # delay
        time.sleep(8)
        # click here in verification email
        driver.find_element_by_xpath("//*[@id='detailView']/div/div[1]/md-card/md-card-content/div[6]/div/div/div/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div[1]/div[2]/a").click()
        # delay
        time.sleep(8)
        # windows handler
        handlers = driver.window_handles
        driver.switch_to.window(handlers[1])
        if "AccountChooser" in driver.current_url:
            # account click
            driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div").click()
        if "verify" in driver.current_url:
            driver.switch_to.window(handlers[0])
            # delay
            time.sleep(3)
            # disconnect sogo
            driver.find_element_by_xpath("/html/body/main/section/md-toolbar[1]/div[2]/a[6]/md-icon").click()
            # delay
            time.sleep(8)
            driver.quit()
            VerificationEmail(new_email)
            return
        time.sleep(8)
        '''
        if "v2" not in driver.current_url:
            driver.switch_to.window(handlers[0])
            # delay
            time.sleep(3)
            # disconnect sogo
            driver.find_element_by_xpath("/html/body/main/section/md-toolbar[1]/div[2]/a[6]/md-icon").click()
            # delay
            time.sleep(8)
            driver.quit()
            VerificationEmail(new_email)
            return
        '''
        # password enter
        pwd = driver.find_element_by_name("password")
        pwd.send_keys("hadi1234")
        # next btn
        nxt = driver.find_element_by_class_name("VfPpkd-RLmnJb")
        nxt.click()
        # delay
        time.sleep(8)
        driver.switch_to.window(handlers[0])
        # delay
        time.sleep(3)
        #disconnect sogo
        driver.find_element_by_xpath("/html/body/main/section/md-toolbar[1]/div[2]/a[6]/md-icon").click()
        # delay
        time.sleep(8)


        driver.quit()

# complete driver
def CompleteDriver():
    VerificationEmail("test23@danial.live")

    GsuiteAppDownload("https://gsuite.google.com/marketplace/app/bjorns_accentsnsymbols/102285000011")

    GsuiteAppDelete("https://gsuite.google.com/marketplace/app/bjorns_accentsnsymbols/102285000011")



#----------------------------------Main(Testing)---------------------------------------------------------------#
#GsuiteAppDownload("https://gsuite.google.com/marketplace/app/lucidpress_free_design_tool/701689253383")
#GsuiteAppDelete("https://gsuite.google.com/marketplace/app/lucidpress_free_design_tool/701689253383")
#cleaningJSON()
#emails = ["test1@danial.live", "test2@danial.live", "test3@danial.live", "test4@danial.live"]
#count = 0
#for i in range(25):
    #VerificationEmail("test"+str(i+13)+"@danial.live")
    #print("test"+str(i+1)+"@danial.live"Passwd)

CompleteDriver()


#"//*[@id="password"]"
#"//*[@id="password"]/div[1]/div/div[1]/input"