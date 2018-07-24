let title = $("#title"),
    description = $("#description"),
    submitBtn = document.querySelector("#submit-btn");

title.on('input', function(){
    if(Boolean(title.val() && title.val().length >= 5
        && description.val() && description.val().length >= 10))
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
});
description.on('input', function () {
    if (Boolean(title.val() && title.val().length >= 5
        && description.val() && description.val().length >= 10))
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
});
title.trigger('input');