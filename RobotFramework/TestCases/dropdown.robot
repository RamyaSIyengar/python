*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://artoftesting.com/samplesiteforselenium

*** Test Cases ***
TestingRadio
    open browser     ${url}  ${browser}
    maximize browser window
    set selenium speed  1seconds

    select from list by label  testingDropdown  Manual Testing
    select from list by index  testingDropdown  1
    select from list by value  testingDropdown  Database