from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class Busca_NFS:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path =r"C:\Users\ADM\Documents\Chrome Driver\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get('http://177.124.184.59:5660/issweb/paginas/login;jsessionid=dJjhQcInRu3dX9d3yWICCA8q.undefined')

        time.sleep(2)
        driver.find_element_by_id('username').send_keys(self.username)
        driver.find_element_by_id('password').send_keys(self.password + Keys.RETURN)
        time.sleep(3)

    def consulta_nfs(self, datain, datafim):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/section/div/aside/div[2]/div[1]/nav/form/ul/li[3]/a').click()
        driver.find_element_by_xpath('//*[@id="navConNfs"]/a/span').click()
        driver.find_element_by_id('form:dtInicio_input').clear()
        driver.find_element_by_id('form:dtInicio_input').send_keys(datain)
        driver.find_element_by_id('form:dtFim_input').clear()
        driver.find_element_by_id('form:dtFim_input').send_keys(datafim)
        driver.find_element_by_xpath('/html/body/section/div/section/form/div[2]/div[2]/div[1]/div[2]/div/div[3]/span').click()
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/ul/li[2]/div/div[2]/span').click()
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/ul/li[3]/div/div[2]/span').click()
        driver.find_element_by_xpath('/html/body/section/div/section/form/div[4]/button/span[2]').click()
        time.sleep(5)
        for i in range(1,5):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        driver.find_element_by_xpath('/html/body/section/div/section/form/div[6]/button[3]/span[2]').click()
        driver.find_element_by_xpath('/html/body/section/div/section/form/div[6]/button[1]/span[2]').click()

boot = Busca_NFS('32375442000109', '32375')
boot.login()
boot.consulta_nfs('01/08/2021', '31/08/2021')

