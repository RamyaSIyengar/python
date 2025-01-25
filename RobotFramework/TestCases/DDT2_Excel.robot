*** Settings ***
Library   SeleniumLibrary
Resource    ../Resources/login_resources.robot
Library     DataDriver      ../TestDataFile/login.xlsx  sheet_name=Sheet1


Suite Setup  OPEN My Browser    # opens one time in begining
Suite Teardown  Close Browsers
Test Template   Invalid login


*** Test Cases ***
LoginTestWithExcel using ${username} and ${password}

*** Keywords ***
Invalid login
    [Arguments]    ${username}    ${password}
    sleep  2
    Input username   ${username}
    Input password   ${password}
    click login
    sleep  2
    Error message should be displayed