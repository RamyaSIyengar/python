*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Launch Browser1
    open browser    ${url}  ${browser}
    maximize browser window

Select Gender
    [Arguments]     ${gender}
    select radio button    gender     ${gender}

Return title
    [Arguments]    ${appurl}
    open browser    ${appurl}  ${browser}
    ${title}=   get title
    [RETURN]        ${title}