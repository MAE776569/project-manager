function emailValid(email) {
    return Boolean(email.val() &&
        /^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
            .test(email.val()));
}
function passwordValid(password) {
    return Boolean(password.val() &&
        /^(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+*!=]).*$/
            .test(password.val()));
}
function validateEmail(email, emailIcon) {
    if (email.hasClass('input-error'))
        email.removeClass('input-error');

    emailIcon.removeClass();

    if (emailValid(email))
        emailIcon.addClass("fas fa-check");
    else
        emailIcon.addClass("fas fa-times");
}
function validatePassword(password, passwordIcon) {
    if (password.hasClass('input-error'))
        password.removeClass('input-error');

    passwordIcon.removeClass();

    if (passwordValid(password)) 
        passwordIcon.addClass("fas fa-check");
    else
        passwordIcon.addClass("fas fa-times");
}
function passwordConfirmationValid(password, confirmPassword) {
    return Boolean(confirmPassword.val() &&
        /^(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+*!=]).*$/
            .test(confirmPassword.val()) &&
        confirmPassword.val() === password.val());
}
function validatePasswordConfirmation(password, confirmPassword, confirmPasswordIcon) {
    if (confirmPassword.hasClass('input-error'))
        confirmPassword.removeClass('input-error');

    confirmPasswordIcon.removeClass();

    if (passwordConfirmationValid(password, confirmPassword))
        confirmPasswordIcon.addClass("fas fa-check");
    else
        confirmPasswordIcon.addClass("fas fa-times");
}