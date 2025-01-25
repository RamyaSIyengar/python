*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${URL}    https://demo.nopcommerce.com/
${BROWSER}     Chrome
*** Test Cases ***
LoginTest
#    create webdriver  chrome excutable_path="C:\Drivers\chromedriver-win64\chromedriver.exe"
    open browser  ${URL}  ${BROWSER}
#    input text  id:APjFqb   Robot Framework
    click link  xpath://a[text()="Log in"]
    set selenium speed  3seconds




*** Keywords ***