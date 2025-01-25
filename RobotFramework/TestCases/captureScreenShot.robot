*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Capture Screenshot
    open browser    https://www.google.com/     chrome
    maximize browser window

    capture element screenshot      xpath://img[@alt="Google"]      C:/Users/soundarr/Desktop/python/pythonBasics/RobotFramework/logo.png
    capture page screenshot     googleSearch.png

