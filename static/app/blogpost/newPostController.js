
//angular
//  .module ('blogpostApp', ['blogpostService'])
var blogpostApp = angular.module('blogpostApp');
  blogpostApp.controller ('NewpostCtrl', ['$scope', '$http', '$route', 'BlogpostService',
    function ($scope, $http, $route, BlogpostService) {

/*
	var ref = new BlogpostService();
	$scope.newblogs = $firebaseArray(ref);

	$scope.newblog = new BlogpostService();
	$scope.save = function(){
	  $scope.newblog.$save({title: 'Saimon', content: 'saimon@devdactic.com'});
	  $scope.newblogs.push($scope.newblog);
	  $scope.newblog = new BlogpostService();
	}
*/


//https://egghead.io/lessons/angularjs-using-resource-for-data-models#/tab-discuss
	$scope.newblog = {};
//$scope.newblog1 = [];
	//$scope.newblogs = [BlogpostService.query()];
	
//	var newblog = BlogpostService.get({id:1}, function(){
///$scope.newblog1=newblog;
//$scope.newblog2= newblog.content;
//	  	newblog.content='rrrrr';
//		newblog.$save(newblog);
//	});
 	//$scope.newblogs.push($scope.newblog);

//$scope.newblog1=$scope.newblogpost;
//$scope.newblog2= $scope.newblogpost.content;
//	  //$scope.newblog=$scope.newblogpost;
//	  $scope.newblog=$scope.newblog.$save($scope.newblogpost);
//	  $scope.newblogs.push($scope.newblog);
//	
	
	
	//$scope.newblogs.push($scope.newblog);
	$scope.newblog = BlogpostService();
	$scope.newblogs = [BlogpostService.query()];
//$scope.newblog2 = newblog;
	$scope.save = function(newblogpost){
//$scope.newblog1=$scope.newblogpost;
//$scope.newblog2= $scope.newblogpost.content;
	  $scope.newblog1 = newblogpost;
	  //$scope.newblog.title = newblogpost.title;
	  //$scope.newblog.content = newblogpost.content;
	  //BlogpostService.save($scope.newblog);

	  BlogpostService.save($scope.newblog);
	  $scope.newblogs.push($scope.newblog);
	  //$scope.newblog = new BlogpostService();
//var title = $scope.newblogpost.title;

	  //$scope.newblog1  =  {title: 'Saimon', content: 'saimon@devdactic.com'};
	  //$scope.newblogs.push($scope.newblogpost);
	}

///////////////////////////////////////////////////
/*
	//$scope.newblog = {};
	$scope.newblog = new BlogpostService();
	//var newblog = new BlogpostService();
	$scope.newblogs = [BlogpostService.query()];

//$scope.newblog1 = [];
	//$scope.newblog1.$save($scope.newblogpost);
	

	$scope.savenew = function(){
//$scope.newblog1.$save($scope.newblogpost);
$scope.newblog1 = $scope.newblogpost.title;
$scope.newblog2 = $scope.newblogpost.content;
//var newblog = new BlogpostService();
	  $scope.newblog3 = $scope.newblog.$save($scope.newblogpost);
	  //$scope.newblogs.push($scope.newblog);
	  //$scope.newblog = new BlogpostService();


	  //$scope.newblog1  =  {title: 'Saimon', content: 'saimon@devdactic.com'};
	  //$scope.newblogs.push($scope.newblogpost);
	}

*/
//////////////////////////////////////////////////
/*
      //data = {blogpost[title: 'Saimon', content: 'saimondevdacti']};
      $scope.newblog = new BlogpostService.get({id: 1});
	
      //BlogpostService.save(function(data){});
	$scope.newblog.$save({'title': 'Saimon', 'content': 'saimon@devdactic.com'});
*/
/*
 function ($scope, $http){
         
        var save = {
	  method : 'POST',
	  url: "/blogpost/blogposts/",
	  headers: {
   	    'Content-Type': undefined
 	  },
 	  data: { blogpost: 'newblogpost' }	
	}

	$http(save).then(function(){$scope.response = newblogpost}, function(){$scope.response1 = "newblogpost"});
*/




//1    function ($scope, BlogpostService) {
      //$scope.blogposts = BlogpostService.query();

/*
      var newblogpost = new BlogpostService($scope.newblogpost);
      newblogpost.$save()


      $scope.newblogpost = new BlogpostService();
      $scope.save = $scope.newblogpost.$save({blogpost: $scope.newblogpost}, function(data) {
	$scope.newblogpost.$save();
      });
*/

/*
      BlogpostService.query(function(data) {
        $scope.blogposts = data.results;
      });

      BlogpostService.save({blogpost: '$scope.blogpost'}, $scope.blogposts
      );
*/
      //var blogpost = BlogpostService.save({ id: 1 }, function(data) {
        //$scope.blogpost = data.results;
	//blogpost.title = 'blogpost.title';
	//blogpost.$save();
      //});

     /*
      var blogposts = BlogpostService.get( function(data) {
	//var blogposts = data.results;
   	var blogpost = data.results[1];
	blogpost.title = 'blogpost.title';
  	blogpost.$save();
      }); 
      */ 
/*
// 1 
      BlogpostService.get(function(data) {
        $scope.blogpost = data.results[1];

	$scope.blog = $scope.blogpost.title;
	$scope.blogpost.title = "NEW title";
	//$scope.blogpostForm = function($scope){
	BlogpostService.save({blogpost: $scope.blogpost}, {method: 'POST', isArray: true});
	//};
      });
      
 */       
      //$scope.blog = newblogpost;
      //blogpost.title = "My new title";
  	
     
      //blogpost.$save();
	

        
      //var blogpost = new BlogpostService();
      //blogpost.title = 'blogpost.title';
      //blogpost.content = 'blogpost.content';
      //blogpost.$save();

      //$scope.blog1 = 'blogpost.title';
      //$scope.blog2 = 'blogpost.content';
    }]);
  


/*
angular
  .module('blogpost', [])
  
  .controller('BlogpostCtrl', ['$scope', '$http', function($scope, $http) {
   
    $scope.blogposts = [{title:"title none", content:"content none"}]

    $http.get("/blogpost/blogposts")
      .success(function (data) {       
        $scope.blogposts = data.results;	
	$scope.blog = "BLOG";       
      });      
    $scope.name = 'World';
  }]);
*/

