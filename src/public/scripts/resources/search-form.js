let searchInput = $("#search-input"),
    submitBtn = document.querySelector("#submit-btn");

searchInput.on('input', function(){
    if(searchInput.val())
        submitBtn.disabled = false;
    else
        submitBtn.disabled = true;
});