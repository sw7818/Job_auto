from os import terminal_size
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

elements = []

""""
text = open('jobs.txt', 'w+')
text.write('Total Jobs Applied for:   \n')
text.write('0\n')
text.close()
"""
dict = {'python': 3, 'word': 10,
        'javascript': 1, 'django': 1, 'react': 1, 'excel': 5, 'salary': 50000}
# undefined object

summary_statement = 'I am severly underqualified for this position, personally I would reject this application, thanks, linkedinBOT'


def reply(Question):
    question1 = Question.lower()
    p = 1

    if 'how many years' in question1:
        if 'python' in question1:
            p = dict.get('python')
            return p

        if 'microsoft word' in question1:
            p = dict.get('word')
            return p

        if 'excel' in question1:
            p = dict.get('excel')
            return p

        if 'javascript' in question1:
            p = dict.get('javascript')
            return p

        if 'django' in question1:
            p = dict.get('django')
            return p

        if 'react' in question1:
            p = dict.get('react')
            return p

        if 'salary' in question1:
            p = dict.get('salary')
            return p

        else:
            p = 1
            return str(p)

    if 'are you' or 'have you' in question1:
        p = 0
        return p


driver = webdriver.Chrome(
    executable_path=r'C:\Users\swewa\chromedriver\chromedriver.exe')

driver.get('https://www.linkedin.com/jobs/search/')

driver.maximize_window()

time.sleep(2)

cook = driver.find_element_by_xpath(
    '//*[@id="artdeco-global-alert-container"]/div[1]/section/div/div[2]/button[2]').click()

time.sleep(0.5)


login = driver.find_element_by_class_name('nav__button-secondary').click()


time.sleep(0.5)

email = driver.find_element_by_xpath(
    '//*[@id="username"]').send_keys('swe.ward@gmail.com')

time.sleep(0.5)


password = driver.find_element_by_xpath(
    '//*[@id="password"]').send_keys('Curlysw88t?')

time.sleep(0.5)


login = driver.find_element_by_xpath(
    '//*[@id="organic-div"]/form/div[3]/button').click()

time.sleep(3)

easy_apply = driver.find_element_by_xpath(
    '//button[text()="Easy Apply"]').click()

process = ''


"""So before we start applying for jobs we need to identify where the jobs are in relation to each other
in regards to the jobs list class.

This can be done via xpath and we're gunna go through /html/body/div[7]/div[3]/div[3]/div/div/section[1]/div/div/ul/li[x]
where each x tag will increment by 1 starting at 1


/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li[1]
/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li[2]
/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li[3]
/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li[4]
...
..
.

Note that the primary div tag will vary from 6 to 7 therefor we wiull try 6 and except 7
"""

time.sleep(2)
num = 0
for x in range(1, 26):

    # selecting the job

    # create text file and write how many job the title time aplied etc....
    """"
    with open('jobs.txt') as file:
        data = file.readlines()
        jobs = int(data[1])
        jobs = jobs + 1

        data[1] = str(jobs)
        file.close()
        file = open('jobs.txt', 'w')
        file.writelines(data)

        file.close()
    """
   # click on the job

    try:
        driver.find_element_by_xpath(
            '/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li' + str([x])).click()
        print('click 1')
    except:
        pass
    try:
        driver.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div[3]/div/div/section[1]/div/div/ul/li' + str([x])).click()
        print('click 2')
    except:
        pass

    app_1 = ''
    try:
        app = driver.find_element_by_xpath(
            '/html/body/div[6]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div/span').text
        app_1 = app.lower()
    except:
        pass

    try:
        app = driver.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div/span').text
        app_1 = app.lower()
    except:
        pass

    if 'applied' in app_1:
        print('affirm')
        continue

    try:
        a = driver.find_element_by_xpath(
            '/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li' + str([x])+'/div/div/div[1]/div[2]/div[1]/a').text
        b = driver.find_element_by_xpath(
            '/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li' + str([x]) + '/div/div/div[1]/div[2]/div[2]/a').text
        c = driver.find_element_by_xpath(
            '/html/body/div[6]/div[3]/div[3]/div/div/section[1]/div/div/ul/li'+str([x]) + '/div/div/div[1]/div[2]/div[3]/ul/li').text
        text = open('jobs.txt', 'a+')
        text.write('\n')
        text.write('Job applied for:   ' + a + '\n')
        text.write('Company name:   ' + b+'\n')
        text.write('Job Location:   ' + c+'\n')
        x = datetime.datetime.now()
        text.write('Date and time applied:    ' + str(x)+'\n')

        try:
            n_a = driver.find_element_by_xpath(
                '/html/body/div[6]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/ul/li[1]/div/ul/li[1]/span').text
            text.write('Number of competing applicants:    ' + n_a + '\n')

        except:
            pass

        text.close()

    except:

        a = driver.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div[3]/div/div/section[1]/div/div/ul/li' + str([x])+'/div/div/div[1]/div[2]/div[1]/a').text
        b = driver.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div[3]/div/div/section[1]/div/div/ul/li' + str([x]) + '/div/div/div[1]/div[2]/div[2]/a').text
        c = driver.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div[3]/div/div/section[1]/div/div/ul/li'+str([x]) + '/div/div/div[1]/div[2]/div[3]/ul/li').text

        text = open('jobs.txt', 'a+')
        text.write('\n')
        text.write('\n')
        text.write('\n')
        text.write('Job applied for:   ' + a+'\n')
        text.write('Company name:   ' + b+'\n')
        text.write('Job Location:   ' + c+'\n')
        x = datetime.datetime.now()
        text.write('Date and time applied:    ' + str(x)+'\n')

        try:
            n_a = driver.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/ul/li[1]/div/ul/li[1]/span').text
            text.write('Number of competing applicants:    ' + n_a + '\n')

        except:
            pass

        text.close()
#
#
#

#
#
#

#
#
    try:

        overlay = driver.find_element_by_xpath(
            '/html/body/div[6]/aside/div[1]/header/section[2]/button[2]').click()

    except:
        overlay_2 = driver.find_element_by_xpath(
            '/html/body/div[7]/aside/div[1]/header/section[2]/button[2]').click()

    time.sleep(2)
    # Easy apply click / apply button
    try:
        driver.find_element_by_xpath(
            '/html/body/div[6]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div/button').click()

    except:
        pass

    try:
        driver.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div[3]/div/div/section[2]/div/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div/button').click()

    except:
        pass

    #  This is typically the contact info section ####
    try:
        progress = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/div/span').text
        print(progress)
    except:
        pass

    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button').click()
    except:
        pass

    # This is typically the resume section

    try:
        progress = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/div/span').text
        print(progress)

    except:
        pass

# cover letter submission

    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div[2]/div/div/div/div/div/textarea').send_keys(summary_statement)
    except:
        pass
    """"
    try:

        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]').click()
    except:
        pass
    """
#
#
#
#
#
#
#
#
#
#
#

    # This is the additional questions section
    """"
    try:
        progress = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/div/span').text
        print(progress)

    except:
        pass

    # we need to have each question and its corresponding answer
    try:
        Q1 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/h3').text
        print(Q1)

    except:
        pass

    try:
        Q2 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[1]/div/label/span[1]').text

        print('Q2  ' + Q2)

        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[1]/div/div/div/input').send_keys(reply(Q2))

    except:
        pass

    try:
        Q3 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[2]/fieldset/legend/span[1]').text
        print('Q3   ' + Q3)

        if reply(Q3) == 0:
            element = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[2]/fieldset/div/div[1]/input')

            actions = ActionChains(driver)
            actions.move_to_element(element).click().perform()

    except:
        pass
    try:
        Q4 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[3]/fieldset/legend/span[1]').text
        print('Q4   ' + Q4)

        try:
            element = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[3]/fieldset/div/div[1]/input')

            actions = ActionChains(driver)
            actions.move_to_element(element).click().perform()
        except:
            pass

    except:
        pass

    try:
        Q5 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[2]/div/label/span[1]').text

        print('Q5   ' + Q5)
        try:
            driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[2]/div/div/select/option[2]').click()

        except:
            pass
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[2]/div/div/div/input').send_keys(reply(Q5))

    except:
        pass

    try:
        Q6 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[1]/fieldset/legend/span[1]').text
        print('Q6   ' + Q6)

        if reply(Q3) == 0:

            print('good so far 1')

            try:
                element = driver.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[2]/fieldset/div/div[1]/input')

                actions = ActionChains(driver)
                actions.move_to_element(element).click().perform()
                print('good so far 2')

            except:
                pass
            print('good so far 4')
            try:
                element = driver.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/form/div/div/div/fieldset/div/div[1]/input')

                actions = ActionChains(driver)
                actions.move_to_element(element).click().perform()

                print('good so far 3')

            except:
                pass

    except:
        pass

    try:
        Q8 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[3]/div/label/span[1]').text
        print('Q8   ' + Q8)

        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[3]/div/div/div/input').send_keys(str(reply(Q8)))
    except:
        pass

    try:
        Q9 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[4]/fieldset/legend/span[1]').text

        print('Q9   ' + Q9)

        try:
            element = driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[4]/fieldset/div/div[1]/input')
            actions = ActionChains(driver)
            actions.move_to_element(element).click().perform()

        except:
            pass

    except:
        pass

    try:
        Q10 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[5]/div/label/span[1]').text

        print('Q10   '+Q10)

        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[5]/div/div/div/input').send_keys(str(reply(Q10)))

    except:
        pass

    try:
        Q11 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[4]/div/label/span[1]').text
        r_1 = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[4]/div/div/select/option[2]').click()
    except:
        pass
    time.sleep(2)
    #

    #
    # This section sends off the application
    #
    #
    #
    #
    #
    #

    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[2]/fieldset/div/div[1]/input').click()

    except:
        pass
        # /html/body/div[3]/div/div/div[2]/div/form/footer/div[3]/button

    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/div/div/div[3]/fieldset/div/div[1]/input').click()
    except:
        pass

    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]').click()
    except:
        pass
    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]').click()

    except:
        pass
    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[3]/button[2]').click()
    except:
        pass

    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[2]/button[2]').click()

    except:
        pass

    time.sleep(1)

    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[2]/div/form/footer/div[3]/button').click()

    except:
        pass

    try:
        driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/button').click()
    except:
        pass
    """

    num += 1
    text = open('jobs.txt', 'a+')
    text.write('Job application number:       ' + str(num)+'\n')
    text.close()
