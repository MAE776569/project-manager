let email = $("#email"),
    password = $("#password"),
    emailIcon = $("#email-icon"),
    passwordIcon = $("#password-icon"),
    confirmPassword = $("#confirm-password"),
    confirmPasswordIcon = $("#confirm-password-icon"),
    submitBtn = document.querySelector("#submit-btn");

function validateRegiteration() {
    if (emailValid(email) && passwordValid(password)
        && passwordConfirmationValid(password, confirmPassword))
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
}
email.on('input', ()=>{
    validateEmail(email, emailIcon);
    validateRegiteration();
});
password.on('input', ()=>{
    validatePassword(password, passwordIcon);
    validateRegiteration();
});
confirmPassword.on('input', ()=>{
    validatePasswordConfirmation(password, confirmPassword, confirmPasswordIcon);
    validateRegiteration();
});