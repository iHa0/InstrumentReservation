from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time

times = 0
sleep_time = 1

# 此处设置需要设置的日期
start_index = 16
end_index = 18
day = 9
web = "此处输入相对应的预约网址，eg.http://yqgx.zcmu.edu.cn/lims/"
username = "此处输入 username"
password = "此处输入 password"

### 控制时间
# strat_time = "2021-12-" + str(day) + " " + str(start_index) + ":00:01"
# end_time = "2021-12-" + str(day) + " " + str(end_index) + ":00:00"
# print(strat_time)
# print(end_time)
# stimeArray = time.strptime(strat_time, "%Y-%m-%d %H:%M:%S")
# etimeArray = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
# start_timestamp = time.mktime(stimeArray)
# end_timestamp = time.mktime(etimeArray)
# print(end_timestamp - start_timestamp)
# print("h")

# option=webdriver.ChromeOptions()
# option.add_argument('headless') # 设置option
# driver = webdriver.Chrome(chrome_options=option)  # 调用带参数的谷歌浏览器
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome("chromedriver")
driver.get(web)

driver.find_element_by_xpath("//*[@id='sidebar']/div/div/div[2]/div[3]/div/h1/a").click()

driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("//*[@id='fm1']/table/tbody/tr[4]/td/input").click()
print("ok")
# 点击首页预约
driver.find_element_by_xpath("//*[@id='table_equipments_follow_equipments']/tbody/tr[1]/td[2]/div/div/a").click()
time.sleep(2)
# 此处为了解决加载慢的问题
# 自动判断"添加"按钮是否加载完成
# for i in range(200):
#     try:
#         el = driver.find_element_by_link_text("添加")
#         if el.is_displayed():
#             break
#     except:
#         pass
#     time.sleep(0.1)
# else:
#     print("无法找到\"添加\"元素，TimeOut！")
while True:
    ### 控制时间
    strat_time = "2021-12-" + str(day) + " " + str(start_index) + ":00:01"
    end_time = "2021-12-" + str(day) + " " + str(end_index) + ":00:00"
    stimeArray = time.strptime(strat_time, "%Y-%m-%d %H:%M:%S")
    etimeArray = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    start_timestamp = time.mktime(stimeArray)
    end_timestamp = time.mktime(etimeArray)
    above = driver.find_element_by_link_text("添加")
    ActionChains(driver).double_click(above).perform()
    time.sleep(2)

    # 将焦点放到新的元素上面
    # 此次有新的窗口弹出，将焦点聚集到新弹出的小页面上
    a = driver.find_element_by_class_name('dialog_content')
    driver.execute_script('arguments[0].click()',a)

    time.sleep(0.5)
    Target_Div = driver.find_element_by_name("project_lab")
    driver.execute_script("arguments[0].setAttribute('style','display:\"true\"')", Target_Div)
    time.sleep(0.5)
    sel = driver.find_element_by_name("project_lab")
    Select(sel).select_by_index(1)
    time.sleep(0.2)

    start_val = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/form/table/tbody/tr[4]/td[2]/input[1]")
    driver.execute_script("arguments[0].value = \'"+ str(int(start_timestamp)) +"\';", start_val)

    start_val = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/form/table/tbody/tr[4]/td[2]/input[2]")
    driver.execute_script("arguments[0].value = \'"+ str(int(start_timestamp)) +"\';", start_val)

    end_val = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/form/table/tbody/tr[5]/td[2]/input[1]")
    driver.execute_script("arguments[0].value = \'"+ str(int(end_timestamp)) +"\';", end_val)

    end_val = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/form/table/tbody/tr[5]/td[2]/input[2]")
    driver.execute_script("arguments[0].value = \'"+ str(int(end_timestamp)) +"\';", end_val)
    time.sleep(0.2)
    Target_Div2 = driver.find_element_by_name("project")
    driver.execute_script("arguments[0].setAttribute('style','display:\"true\"')", Target_Div2)
    time.sleep(1)
    sel = driver.find_element_by_name("project")
    time.sleep(2)
    try:
        Select(sel).select_by_value("510")
    except:
        print("选择510，此处发生错误！")
    time.sleep(0.2)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div/form/table/tbody/tr[9]/td/div/input").click()

    # driver.find_element_by_xpath("//*[@id='tr_lab_6188c40f2f90a']/td[2]/div/div").click()
    # aa = driver.find_element_by_link_text("--")
    # aa = driver.find_element_by_xpath("# aa = driver.find_element_by_class_name('dropdown_text')")
    # aa = driver.find_element_by_class_name("text autoselect").text
    # print(aa)
    # ActionChains(driver).double_click(aa).perform()
    # bb = driver.find_element_by_link_text("XXX课题组")
    # ActionChains(driver).double_click(bb).perform()
    # 将焦点放到新的元素上面
    time.sleep(1)
    b = driver.find_element_by_class_name('dialog_title')
    driver.execute_script('arguments[0].click()', b)
    try:
        time.sleep(2)
        e1 = driver.find_element_by_class_name("dialog_title")
        if e1.is_displayed():
            # 预约失败，可能是时间未到
            times += 1
            print("正在进行第【{}】次尝试，时间【{}】".format(times, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            driver.find_element_by_class_name("select").click()
            time_h = time.localtime().tm_hour
            time_m = time.localtime().tm_min
            time_s = time.localtime().tm_sec
            now_time = "2021-12-" + str(day) + " " + str(time_h) + ":"+ str(time_m) +":"+ str(time_s) + ""
            end_time = "2021-12-" + str(day) + " " + str(end_index) + ":00:01"
            print("预约时间为【{}】,现在时间为【{}】".format(end_time, now_time))
            stimeArray = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            end_timestamp = time.mktime(stimeArray)
            stimeArray2 = time.strptime(now_time, "%Y-%m-%d %H:%M:%S")
            now_timestamp = time.mktime(stimeArray2)
            sleep_time = end_timestamp - now_timestamp
            #现在还没有到预约的时间
            if sleep_time > 0:
                print("1.还没到时间，预约【{}】还需要等待【{}】秒".format(end_time, sleep_time))
                time.sleep(sleep_time)
            else:
                continue
            time.sleep(2)
            continue
        else:
            print("2021-12-{} {}:00:01-{}:00:00预约成功，成功时间为【{}】".format(day,start_index, end_index,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
            start_index += 2
            end_index += 2
            if end_index == 24:
                day += 1
                start_index = 8
                end_index = 10
                print("全天预约结束，等待8小时候继续预约！")
                sleep_time = 60 * 60 * 8 - 60
                sleep_time(sleep_time)
            else:
                time_h = time.localtime().tm_hour
                time_m = time.localtime().tm_min
                time_s = time.localtime().tm_sec
                now_time = "2021-12-" + str(day) + " " + str(time_h) + ":" + str(time_m) + ":" + str(time_s) + ""
                end_time = "2021-12-" + str(day) + " " + str(end_index) + ":00:01"
                stimeArray = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
                end_timestamp = time.mktime(stimeArray)
                stimeArray2 = time.strptime(now_time, "%Y-%m-%d %H:%M:%S")
                now_timestamp = time.mktime(stimeArray2)
                sleep_time = end_timestamp - now_timestamp
                if sleep_time > 0:
                    print("2.预约【{}】等待【{}】秒".format(end_time, sleep_time))
                    time.sleep((sleep_time)-2)
    except:
        pass
    time.sleep(2)
    print("Success, OK!")
