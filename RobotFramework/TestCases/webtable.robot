*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TableValidation

    open browser  https://testautomationpractice.blogspot.com/   chrome
    maximize browser window

    ${rows} =   get element count  xpath://table[@name="BookTable"]//tr
    ${cols} =   get element count  xpath://table[@name="BookTable"]//tr[1]/th
     ${res} =   get text  xpath://table[@name="BookTable"]//tr[1]/th[1]

    log to console      ${rows}
    log to console      ${cols}
    log to console      ${res}

#    validation of the table
    table column should contain     xpath://table[@name="BookTable"]    2   Author
    table row should contain     xpath://table[@name="BookTable"]    4   Learn JS
    table cell should contain     xpath://table[@name="BookTable"]    2  4  300
    table header should contain     xpath://table[@name="BookTable"]    BookName

    close browser





