Library   SeleniumLibrary     # https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html

*** Variables ***

# Username and password must be passed in with --variable

${BROWSER}  googlechrome
${LOGIN_URL}    https://www.dropout.tv/login

User watches Dropout.tv

    Given user is logged in to DropOut
    Then Page Should Contain    Lot out

User is logged in to DropOut
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Input Text      signin-email-input    ${USERNAME}
    Click Element   signin-email-submit
    Input Text      signin-password-input    ${PASSWORD}
    Click Element   signin-password-submit




