var email = $("#email"),
    password = $("#password"),
    form = $("#auth-form"),
    emailIcon = $("#email-icon"),
    passwordIcon = $("#password-icon"),
    submitBtn = document.querySelector("#submit-btn");

function emailValid() {
    return Boolean(email.val() &&
        /^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
            .test(email.val()));
}
function passwordValid() {
    return Boolean(password.val() &&
        /^(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+*!=]).*$/
            .test(password.val()));
}
function validateEmail() {
    if (email.hasClass('input-error'))
        email.removeClass('input-error');
    if (emailValid()) {
        emailIcon.removeClass();
        emailIcon.addClass("fas fa-check");
    }
    else {
        emailIcon.removeClass();
        emailIcon.addClass("fas fa-times");
    }
}
function validatePassword() {
    if (password.hasClass('input-error'))
        password.removeClass('input-error');
    if (passwordValid()) {
        passwordIcon.removeClass();
        passwordIcon.addClass("fas fa-check");
    }
    else {
        passwordIcon.removeClass();
        passwordIcon.addClass("fas fa-times");
    }
}
