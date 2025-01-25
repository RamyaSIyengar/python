*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
GetAllLinks
    open browser    https://www.google.com/     chrome
    maximize browser window

    ${linksCount}=   get element count  xpath://a
    log to console  ${linksCount}

    @{Linkitems}   create list

    FOR   ${i}   IN RANGE  1  ${linksCount}
    ${linkText}=    get text  xpath://a[${i}]
    LOG TO CONSOLE   ${linkText}
    END

