*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Tabhandle window
    open browser    https://demo.automationtesting.in/Windows.html      chrome
    click link      xpath://div[@id="Tabbed"]/a

    Sleep           2  # Wait for the new tab to open
#    List Windows    # Debugging: Lists all open windows in the log

    switch Window    title=Selenium
    click element       xpath://span[text()='Downloads']
    sleep   3
    close all browsers

Multiple browsers
    open browser    https://www.google.com/     chrome
    maximize browser window

    sleep  3

    open browser    https://www.bing.com/       chrome
    maximize browser window

    switch browser  1
    ${title1}=  get title
    log to console     ${title1}

    switch browser  2
    ${title2}=  get title
    log to console      ${title2}

    sleep  2
    close all browsers

#browser related kewywords
#1. go to  2. go back  3. get location
Navigation test
    open browser    https://www.google.com/     chrome
    ${loc}=     get location
    log to console      ${loc}

    go to       https://www.bing.com/
    ${loc}=     get location
    log to console      ${loc}

    go back
    ${loc}=     get location
    log to console      ${loc}

# to run single testcase
#robot --test "Navigation test" .\TestCases\window.robot