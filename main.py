from ast import Continue
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import time
import re




ID = "ID"             # 인터파크 아이디
Password = "PassWord"    # 인터파크 비밀번호
CODE = "22001534"       #CODE = "22000970" # 데스노트
startTime = "2022-04-20-20-31-30"  #예매 시작 시간


book_date = "20220527"  #예매할 날짜
count = "001"        # 하루에 공연이 1개이면 001 만약 2개일경우 앞에 공연은 001 뒷시간 공연은 002


people_ = "2"      #people : 안원수 
Level = "VIP"    # level : VIP, R, A  등 좌석의 등급
block = "A"   # block : A, B, C 등 좌석의 구역을 설정
Floor = "w"   # seat : 숫자 또는 영어. 열을 지정





month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}


def seat_title_checking1(level, block, seat):
    return "[title*='" + level + "석'][title*='" + block + "구역 " + str(seat) + "열']"

def seat_title_checking2(level, block, seat):
    return "[title*='" + level + "석'][title*='" + block + "구역" + str(seat) + "열']"

def seat_title_checking3(level,  block, seat):
    return "[title*='" + level + "석'][title*='" + block + "블럭" + str(seat) + "열']"

def seat_title_checking4(level, block, seat):
    return "[title*='" + level + "석'][title*='-" + str(seat) + "열']"

def seat_title_checking5(level, block, seat):
    return "[title*='" + level + "석'][title*='-" + chr(64 + seat) + "열']"

def seat_title_checking6(level,floor,seat):
    return "[title*='" + level + "석'][title*='" + floor + "층 " + "-" + str(seat) + "열']"

def seat_title_checking7(level,floor,seat):
    return "[title*='" + level + "석'][title*='" + floor + "층" + "-" + str(seat) + "열']"

def seat_title_checking8(level,floor,seat):
    return "[title*='" + "객석" + level + "석'][title*='" + floor + "층 " + "-" + str(seat) + "열']"

def seat_title_checking9(level,floor,seat):
    return "[title*='" +"객석" + level + "석'][title*='" + floor + "층" + "-" + str(seat) + "열']"    
 

driver = webdriver.Chrome(r'크롬드라이버 위치')

driver.set_window_size(1400,1000)
driver.get("https://ticket.interpark.com/Gate/TPLogin.asp")

driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='leftLoginBox']/iframe[@title='login']"))
userid = driver.find_element(By.ID,"userId")
userid.send_keys(ID)
userPwd = driver.find_element(By.ID,"userPwd")
userPwd.send_keys(Password)
userPwd.send_keys(Keys.ENTER)
driver.get('https://ticket.interpark.com/')


'''
driver.get("https://tickets.interpark.com/goods/"+CODE)


driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])


def check_exists_by_element(by, name):
    try:
        driver.find_element(by, name)
    except NoSuchElementException:
        return False
    return True


# 메인 팝업창 제거
ticketingInfo_check = check_exists_by_element(By.XPATH,'//*[@id="popup-prdGuide"]/div[@class="popupWrap"]/div[@class="popupFooter"]/button[@class="popupCloseBtn is-bottomBtn"]')
if ticketingInfo_check:
    driver.find_element(By.XPATH, '//*[@id="popup-prdGuide"]/div[@class="popupWrap"]/div[@class="popupFooter"]/button[@class="popupCloseBtn is-bottomBtn"]').click()


# 날짜선택
calen = driver.find_elements(By.CSS_SELECTOR,".datepicker-panel")
uls = calen[0].find_elements(By.TAG_NAME,"ul")
year_month = uls[0].find_elements(By.TAG_NAME,"li")[1].text.split(". ")
year = year_month[0]
month = year_month[1]


wantYear = "2022"
wantMonth = "6"
wantDate =  15
hour = "20"
min_ = "00"


yearC = int(wantYear) - int(year)
monthC = int(wantMonth) - int(month)

prev = uls[0].find_elements(By.TAG_NAME, "li")[0]
next = uls[0].find_elements(By.TAG_NAME, "li")[2]

s = yearC * 12 + monthC
i = 0
if s > 0:
    while i < s:
        next.click()
        i = i + 1
elif s < 0:
    while i < s:
        prev.click()
        i = i - 1



CellPlayDate = driver.find_elements(By.XPATH, "//ul[@data-view='days']/li[@class!='disabled']")
for cell in CellPlayDate:
    if cell.text == wantDate:
        cell.click()
        break

# 선택 가능한 시간 가져오기
time_li = driver.find_elements(By.XPATH, "//a[@class='timeTableLabel']/span")

hour_min = hour + ":" + min_

for li in time_li:
    if li.text == hour_min:
        li.click()
        break

'''





url = 'https://ticket.interpark.com'
while True:


    date = urllib.request.urlopen(url).headers['Date'][5:-4]
    d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], str(int(date[12:14])+9), date[15:17], date[18:]
    nowTime = y + "-" + m + "-" + d + "-" + hour + "-" + min + "-" + sec 
    print(f'[{url}]의 서버시간\n{y}년 {m}월 {d}일 {hour}시 {min}분 {sec}초')
    if nowTime == startTime:
        break
    else:
        continue




'''
while True:
    now = datetime.now()

    startTime = "2022-4-20-16-58-0"

    nowTime = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second) 
    print(nowTime)
    if nowTime == startTime:
        break
    else:
        continue
'''



# 'http://poticket.interpark.com/Book/BookSession.asp?GroupCode={}&Tiki=N&Point=N&PlayDate={}&PlaySeq={}&BizCode=&BizMemberCode='.format(CODE, book_date, count)
url = 'http://poticket.interpark.com/Book/BookSession.asp?GroupCode={}&Tiki=N&Point=N&PlayDate={}&PlaySeq={}&BizCode=&BizMemberCode='.format(CODE, book_date, count)
driver.get(url)


#driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div[3]/div/div[2]/a[1]').click()




#close_check = check_exists_by_element(By.CLASS_NAME ,"prdGuide")
#if close_check: 
#	driver.find_element(By.CLASS_NAME, "is-bottomBtn").click()



for x in range(0, 5): #안내창 종료
            try:
                alert = driver.switch_to.alert
                alert.accept()
            except:
                pass


for x in range(0, 8): #안내창 종료
            try:
                driver.find_element_by_class_name('closeBtn').click()
            except:
                pass


while True:
    try:
        first_iframe = driver.find_element_by_id('ifrmSeat')  # 첫번째 아이프레임
    except:
        continue
    else:
        break
driver.switch_to.frame(first_iframe)
while True:
    try:
        next_iframe = driver.find_element_by_id('ifrmSeatDetail')  # 두번째 좌석선택 아이프레임
    except:
        continue
    else:
        break
driver.switch_to.frame(next_iframe)



while True:
    try:
        # 활성화 되어 있는 좌석의 class 속성 stySeat
        seat_check = driver.find_element(By.CSS_SELECTOR, "img.stySeat")
        seat_title = seat_check.get_attribute('title')
        b = seat_title.split('-')
        print(b)


        if '구역' in b[1]:
            if b[1][b[1].find('역') + 1] == ' ':
                zone_seat_return = seat_title_checking1
            else:
                zone_seat_return = seat_title_checking2
        elif '블럭' in b[1]:
            zone_seat_return = seat_title_checking3
        elif '층' in b[1]:
            if '객석' in b[1]:
                if b[1][b[1].find('층') + 1] == ' ':
                    zone_seat_return = seat_title_checking8
                else:
                    zone_seat_return = seat_title_checking9
            else:
                if b[1][b[1].find('층') + 1] == ' ':
                    zone_seat_return = seat_title_checking6
                else:
                    zone_seat_return = seat_title_checking7
        else:
            c = re.compile('[0-9]')
            if c.match(b[1]):
                zone_seat_return = seat_title_checking4
            else:
                zone_seat_return = seat_title_checking5

        # 좌석 선택
        w_check = False
        seat = 0
        cnt = 0




        while seat < 20:
            seat = seat + 1
            # zon_seat_return의 매개변수 설명
            # level : VIP, R, A  등 좌석의 등급
            # block : A, B, C 등 좌석의 구역을 설정
            # seat : 숫자 또는 영어. 열을 지정
            if zone_seat_return == seat_title_checking6 or zone_seat_return == seat_title_checking7 or zone_seat_return == seat_title_checking8 or zone_seat_return == seat_title_checking9:
                seat_string = zone_seat_return(Level,Floor,seat)
            else:
                seat_string = zone_seat_return(Level, block, seat)	
            imgs = driver.find_elements(By.CSS_SELECTOR, "img.stySeat" + seat_string)

            for i in imgs:
                i.click()
                cnt = cnt + 1
                if cnt == int(people_):
                    w_check = True
                    break

            if w_check:
                break
                
        # 원래 팝업 프레임으로 돌아가기
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='divBookSeat']/iframe[@id='ifrmSeat']"))
        # 다음 버튼 클릭
        driver.find_element(By.XPATH, "/html/body/form[1]/div/div[1]/div[3]/div/div[4]/a").click()
    except:
        continue
    else:
        break
