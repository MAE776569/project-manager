function validateLogin() {
    if (emailValid() && passwordValid())
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
}
email.on('input', () => {
    validateEmail();
    validateLogin();
});
password.on('input', () => {
    validatePassword();
    validateLogin();
});