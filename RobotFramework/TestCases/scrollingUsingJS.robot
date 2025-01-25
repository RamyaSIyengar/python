*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
scroll
    open browser    https://www.worldometers.info/geography/flags-of-the-world/     chrome
    maximize browser window

#    execute javascript  window.scrollTo(0,1500)
     execute javascript  window.scrollTo(0,document.body.scrollHeight)
     sleep  1
     execute javascript  window.scrollTo(0,-document.body.scrollHeight)
#    scroll element into view    xpath://div[text()="India"]

