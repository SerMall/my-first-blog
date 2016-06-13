var blogpostApp = angular.module('blogpostApp', ["ngRoute", 'ngResource']);

/*
  blogpostApp.config(function($httpProvider) {
    $httpProvider.defaults.headers.common["X-Requested-With"] = 'XMLHttpRequest';
    $httpProvider.defaults.headers.common["FROM-ANGULAR"] = "true";  
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'; 
  });
*/
    blogpostApp.config(function($routeProvider){

	$routeProvider.when('/blogposts/:id',
        {
            templateUrl:'/static/app/blogpost/views/blogpostId.html',
            controller:'BlogpostIdCtrl'
	});

        $routeProvider.when('/new/',
        {
            templateUrl:'/static/app/blogpost/views/newblogpost.html',
            controller:'BlogpostNewCtrl'
        });

        $routeProvider.when('/comments',
        {
            templateUrl:'/static/app/blogpost/views/comments.html',
        //    controller:'CommentCtrl'
        });
	
});



