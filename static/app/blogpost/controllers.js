
var blogpostApp = angular.module('blogpostApp');
  blogpostApp.controller ('BlogpostCtrl', ['$scope', 'BlogpostService',
    function ($scope, BlogpostService) {

      $scope.newblogs = BlogpostService.query(function(data) {
        $scope.blogposts = data.results;
      });
    }]);
  
blogpostApp.controller ('BlogpostIdCtrl', ['$scope', '$routeParams', 'BlogpostService',
    function ($scope, $routeParams, BlogpostService) {

      $scope.blogpostId = BlogpostService.get({'id': $routeParams.id})

      $scope.delete = function(blogpostId) {
        BlogpostService.delete(blogpostId);
      } 

      $scope.update = function() {
        BlogpostService.update($scope.blogpostId);
      }

    }]);

blogpostApp.controller ('BlogpostNewCtrl', ['$scope',  'BlogpostServiceAdd',
    function ($scope,  BlogpostServiceAdd) {

      $scope.blogpostnew = {};
      $scope.save = function(blogpost) {
$scope.blogpostnew1 = blogpost;
$scope.blogpost.title = blogpost.title;
$scope.blogpost.content = blogpost.content;
	var blogpost = new BlogpostServiceAdd();
        blogpost.$save($scope.blogpost);
        //$scope.blogposts.push($scope.blogpostnew)
      }

    }]);
  

