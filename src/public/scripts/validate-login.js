let email = $("#email"),
    password = $("#password"),
    emailIcon = $("#email-icon"),
    passwordIcon = $("#password-icon"),
    submitBtn = document.querySelector("#submit-btn");

function validateLogin() {
    if (emailValid(email) && passwordValid(password))
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
}
email.on('input', () => {
    validateEmail(email, emailIcon);
    validateLogin();
});
password.on('input', () => {
    validatePassword(password, passwordIcon);
    validateLogin();
});