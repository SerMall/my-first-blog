
//angular
//  .module('blogpostService', ['ngResource'])
  blogpostApp.factory("BlogpostService", ['$resource', function ($resource) {
    return $resource('/blogpost/blogposts/:id\/', {id:'@id'}, {'get':    {method:'GET'},
						     'save':   {method:'POST'					 
							,url:'/blogpost/blogposts/'
							},
						     'query': {method: 'GET', isArray: false},
						     'remove': {method:'DELETE'},
						     'delete': {method:'DELETE'},
						     'update': {method:'PUT'}} 
						     ,{stripTrailingSlashes: false}
						); 
  }]);

  blogpostApp.factory("BlogpostServiceAdd", ['$resource', function ($resource) {
    return $resource('/blogpost/blogposts/', {}, {'save':   {method:'POST'
							     ,credentials: true
								},} 
						     ,{stripTrailingSlashes: false}
						); 
  }]);

