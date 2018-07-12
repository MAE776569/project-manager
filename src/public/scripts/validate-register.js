var confirmPassword = $("#confirm-password"),
    confirmPasswordIcon = $("#confirm-password-icon");

function passwordConfirmationValid() {
    return Boolean(confirmPassword.val() &&
        /^(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+*!=]).*$/
            .test(confirmPassword.val()) &&
        confirmPassword.val() === password.val());
}

function validatePasswordConfirmation() {
    if (confirmPassword.hasClass('input-error'))
        confirmPassword.removeClass('input-error');
    if (passwordConfirmationValid()) {
        confirmPasswordIcon.removeClass();
        confirmPasswordIcon.addClass("fas fa-check");
    }
    else {
        confirmPasswordIcon.removeClass();
        confirmPasswordIcon.addClass("fas fa-times");
    }
}
function validateRegiteration() {
    if (emailValid() && passwordValid() && passwordConfirmationValid())
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
}
email.on('input', ()=>{
    validateEmail();
    validateRegiteration();
});
password.on('input', ()=>{
    validatePassword();
    validateRegiteration();
});
confirmPassword.on('input', ()=>{
    validatePasswordConfirmation();
    validateRegiteration();
});