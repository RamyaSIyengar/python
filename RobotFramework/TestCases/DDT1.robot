*** Settings ***
Library  SeleniumLibrary
Resource    ../Resources/login_resources.robot
Suite Setup   OPEN My Browser   #executes once
Suite Teardown     Close All Browsers
Test Template       Invalid Login

#*** Variables ***
#${email}=   Admin
#${pwd}=     admin123

*** Test Cases ***
#RightUser EmptyPasswd     Admin       ${EMPTY}
RightUser WrongPasswd     Admin       admin
WrongUser RightPasswd     user!2        admin123
#WrongUser EmptyPasswd     user1@        ${EMPTY}
WrongUser WrongPasswd     user@        admin@


*** Keywords ***
Invalid Login
    [Arguments]     ${username}    ${pwd}
    sleep  2
    Input username   ${username}
    Input password   ${pwd}
    click login
    sleep  2
    Error message should be displayed