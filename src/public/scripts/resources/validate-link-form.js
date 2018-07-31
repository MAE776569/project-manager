let title = $("#title"),
    subtitle = $("#subtitle"),
    url = $("#url"),
    submitBtn = document.querySelector("#submit-btn");

function validateURL() {
    return Boolean(/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/
        .test(url.val()) ||
        /[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/
        .test(url.val()));
}
function validateInput() {
    return Boolean(title.val() && title.val().length >= 5
        && subtitle.val() && subtitle.val().length >= 10
        && validateURL());
}
title.on('input', function () {
    if (validateInput())
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
});
subtitle.on('input', function () {
    if (validateInput())
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
});
url.on('input', function () {
    if (validateInput())
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
});
title.trigger('input');