*** Settings ***
Library  DatabaseLibrary
Library  OperatingSystem

Suite Setup     Connect To Database     pymysql      ${DBName}      ${DBUser}       ${DBPasswd}     ${DBHost}       ${DBPort}
Suite Teardown  Disconnect From Database


*** Variables ***
${DBName}    mydb
${DBUser}    root
${DBPasswd}  root
${DBHost}    127.0.0.1
${DBPort}    3306


*** Test Cases ***
#Create Person Table
#    ${output}=  Execute SQL String      Create table Person(id integer, first_name varchar(20), last_name varchar(20));
#    log to console   ${output}
#    Should be equal as strings  ${output}    None

#Insert data into Person Table
##     Single record
##    ${output}=  Execute SQL String      Insert Into person values(101,"raj","ram");
##    log to console   ${output}
##    Should be equal as strings  ${output}    None
#
##    multiple record
#    ${output}=  Execute SQL Script      ./TestDataFile/mydb_person_insertData.sql
#    log to console   ${output}
#    Should be equal as strings  ${output}    None

Check row count is equal to some value
    Row Count is equal to x     Select id from mydb.person where first_name="elon";    1

Check Person Table must exist
    table must exist  person

Update record in table
    ${output}=  Execute SQL String      Update mydb.person set first_name="radhe" where id=101;
    log to console   ${output}
    Should be equal as strings  ${output}    None

Retrieve Records from Table
    @{queryResults}=  Query  SELECT * FROM person;
    Log To Console  ${queryResults}
