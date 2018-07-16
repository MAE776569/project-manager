let oldPassword = $("#old-password"),
    oldPasswordIcon = $("#old-password-icon"),
    newPassword = $("#new-password"),
    newPasswordIcon = $("#new-password-icon"),
    confirmNewPassword = $("#confirm-password"),
    confirmNewPasswordIcon = $("#confirm-password-icon"),
    submitBtn = document.querySelector("#submit-btn");

function validateChangePassword() {
    if (passwordValid(oldPassword) && passwordValid(newPassword)
        && passwordConfirmationValid(newPassword, confirmNewPassword))
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
}
oldPassword.on("input", function(){
    validatePassword(oldPassword, oldPasswordIcon);
    validateChangePassword();
});
newPassword.on("input", function () {
    validatePassword(newPassword, newPasswordIcon);
    validateChangePassword();
});
confirmNewPassword.on("input", function () {
    validatePasswordConfirmation(newPassword, confirmNewPassword, confirmNewPasswordIcon);
    validateChangePassword();
});
