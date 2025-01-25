*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Right Click
    open browser    https://demo.guru99.com/test/simple_context_menu.html  chrome
    maximize browser window

    open context menu   xpath://span[text()="right click me"]
    click element  xpath://li[contains(@class, "context-menu-icon")][1]
    sleep  1
    Handle Alert   # clicks ok

Double Click
    go to    https://testautomationpractice.blogspot.com/
    double click element    xpath://button[text()="Copy Text"]
    sleep  1
    close browser

Drap and Drop
    open browser  https://testautomationpractice.blogspot.com/  chrome
    maximize browser window
    drag and drop   id:draggable  id:droppable
    sleep  1
    close browser
