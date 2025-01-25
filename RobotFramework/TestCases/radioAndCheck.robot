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

#    verify title
    title should be     Sample Webpage for Selenium Automation Practice | ArtOfTesting

#    input box
    input text  id:fname    Ramya

#    selecting radio button
    select radio button     gender  female

#   checkbox
    select checkbox     Automation
    select checkbox     Performance

    unselect checkbox   Performance
#    sleep    5




*** Keywords ***