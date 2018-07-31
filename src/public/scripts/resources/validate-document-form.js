let documentInput = document.querySelector("#document-upload"),
    doucmentLabelText = $("#document-upload-label-text"),
    title = $("#title"),
    subtitle = $("#subtitle"),
    submitBtn = document.querySelector("#submit-btn");

documentInput.addEventListener('change', function () {
    if (validateFile()) {
        doucmentLabelText.text(this.files[0].name);
        if(validateInput())
            submitBtn.disabled = false;
        else
            submitBtn.disabled = true;
    }
    else
        submitBtn.disabled = true;
});
function validateFile() {
    return Boolean(documentInput.files && documentInput.files.length === 1);
}
function validateInput() {
    return Boolean(title.val() && title.val().length >= 5
        && subtitle.val() && subtitle.val().length >= 10);
}
function validateCreate() {
    if (validateInput() && validateFile())
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
}
function validateUpdate() {
    if (validateInput())
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
}