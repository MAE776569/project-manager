let email = $("#email"),
    name = $("#name"),
    emailIcon = $("#email-icon"),
    nameIcon = $("#name-icon"),
    submitBtn = document.querySelector("#submit-btn");

function nameValid() {
    return Boolean(name.val() && name.val().length >= 5);
}
function validateName() {
    if (name.hasClass('input-error'))
        name.removeClass('input-error');

    nameIcon.removeClass();
    
    if(nameValid())
        nameIcon.addClass("fas fa-check");
    else
        nameIcon.addClass("fas fa-times");
}
function validateAccountVerification() {
    if (emailValid(email) && nameValid())
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
}

email.on('input', () => {
    validateEmail(email, emailIcon);
    validateAccountVerification();
});
name.on('input', ()=>{
    validateName();
    validateAccountVerification();
});