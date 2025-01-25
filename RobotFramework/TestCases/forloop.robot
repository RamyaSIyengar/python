*** Test Cases ***
For loop
    FOR  ${i}  IN RANGE  1   10
    Log to console  ${i}
    END

For loop1
    FOR  ${i}  IN  1 2 3 4 5 6
    Log to console  ${i}
    END

ForloopWithList
    @{items}    create list     1  2  3  4  5  6  7
    FOR  ${i}  IN   @{items}
    Log to console  ${i}
    exit for loop if    ${i}==5
    END

Forloop4
    FOR  ${i}  IN  ron  raj  ram  ren
    LOG TO CONSOLE  ${i}
    END