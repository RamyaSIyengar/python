*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${LOGIN_URL}    https://opensource-demo.orangehrmlive.com/
${BROWSER}      chrome

*** Keywords ***
OPEN My Browser
    open browser    ${LOGIN_URL}  ${BROWSER}
    maximize browser window

Close Browsers
    Close All Browsers

Input username
    [Arguments]     ${username}
    input text  xpath://input[@name="username"]     ${username}

Input password
    [Arguments]   ${password}
    input text  xpath://input[@name="password"]     ${password}

click login
    click element   xpath://button[@type="submit"]

Dashboard page should be visible
    page should contain     Dashboard

Error message should be displayed
    page should contain     Invalid credentials