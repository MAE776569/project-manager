let app = angular.module('topic-details', ['ui.router', 'youtube-embed']);

app.config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('video', {
            url: '/video',
            templateUrl: '/public/templates/topic-video.html',
            controller: 'videoController'
        })
        .state('note', {
            url: '/note',
            templateUrl: '/public/templates/topic-note.html',
            controller: 'noteController'
        });

    $urlRouterProvider.otherwise('/video');
});

app.factory('topicFactory', ['$http', function ($http){
    let topicSlug = getSlug();
    let factory = {};

    factory.getVideoID = function () {
        return $http.get(`/api/topics/${topicSlug}/video-id`)
        .then((response)=>{
            return response.data.video_id;
        }, (response)=>{
            console.error("Error: " + response.status + " " + response.statusText);
            return null;
        });
    };

    factory.getNote = function(){
        return $http.get(`/api/topics/${topicSlug}/note`)
        .then((response)=>{
            return response.data.note;
        }, (response)=>{
            console.error("Error: " + response.status + " " + response.statusText);
            return null;
        })
    };

    return factory;
}]);

app.controller('videoController', ['$scope', 'topicFactory',
    function ($scope, topicFactory){
        topicFactory.getVideoID().then(function (video_id) {
            if(video_id){
                $scope.video_id = video_id;
                $scope.$on('youtube.player.ended', function ($event) {
                    onPlayerEnded($event);
                });
                $scope.playerVars = {
                    controls: 1,
                    rel: 0,
                    fs: 1,
                    color: 'white'
                };
            }
            else
                $scope.video_id = null;
        });
}]);

app.controller('noteController', ['$sce', '$scope', 'topicFactory',
    function ($sce, $scope, topicFactory) {
        topicFactory.getNote().then(function(note){
            $scope.note = $sce.trustAsHtml(note);
        });
}]);

function getSlug() {
    let pathname = window.location.pathname,
        splitArray = pathname.substring(0, pathname.length - 1).split("/"),
        topicSlug = splitArray[splitArray.length - 1];
    return topicSlug;
}

function onPlayerEnded(event) {
    console.log('ended');
    let pathname = window.location.pathname,
        splitArray = pathname.substring(0, pathname.length - 1).split("/"),
        topicSlug = splitArray[splitArray.length - 1];
    $.ajax({
        method: "POST",
        url: `/api/topics/${topicSlug}/completed/`,
        headers: {
            'X-CSRFToken': Cookies.get('csrftoken')
        },
        success: requestSucceeded,
        error: (error) => {
            console.error(error);
        }
    });
};
function requestSucceeded(data, status) {
    console.log(status);
    console.log(data);
};