*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  mikko
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mi
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  mikko
    Set Password  sala123
    Set Password Confirmation  sala123
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Passwords
    Set Username  mikko
    Set Password  salasana123
    Set Password Confirmation  salasana321
    Click  button >> text=Register
    Register Should Fail With Message  Passwords do not match

Register Without Username Or Password
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Fail With Message  Username and password are required

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Fail With Message  Username kalle is already taken

*** Keywords ***
Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page