const player = new Plyr('#player', {
    keyboard: {
        focused: true,
        global: true
    }
});
player.on('ended', function(){
    console.log('ended');
    let pathname = window.location.pathname;
    let splitArray = pathname.substring(0, pathname.length - 1).split("/");
    let topicSlug = splitArray[splitArray.length - 1];
    $.ajax({
        method: "POST",
        url: `/tracks/topics/${topicSlug}/completed/`,
        headers: {
            'X-CSRFToken': Cookies.get('csrftoken')
        },
        success: requestSucceeded,
        error: (error) => {
            console.error(error);
        }
    });
});
function requestSucceeded(data, status){
    console.log(status);
    console.log(data);
};