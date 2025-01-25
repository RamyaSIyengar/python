*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
Testing Frames
        open browser  https://demo.automationtesting.in/Frames.html      chrome
        select frame  singleframe
        input text  xpath://input   frame
        set selenium speed  3seconds
        unselect frame




