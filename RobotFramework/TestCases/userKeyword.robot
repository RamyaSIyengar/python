*** Settings ***
Library  SeleniumLibrary
Resource    ../Resources/resources.robot

*** Variables ***
${url}      https://testautomationpractice.blogspot.com/
${browser}  chrome
${gender}   female

*** Test Cases ***
UserDefined withoutAgruments
    Launch Browser1         #userdefined keyword
    input text  id:name     Rajesh
    input text  id:email    test@abc.com
    input text  id:phone    9876543121
    sleep  1

UserDefined withArguments
    Select Gender  ${gender}
    sleep  1
    close browser

UserDefined withArgumentAndReturn
    ${title}=  Return title    ${url}
    log to console      ${title}
    log     ${title}   #logs to report




