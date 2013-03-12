
function AsanaCtrl($scope){

	$.ajax({
			url: 'https://app.asana.com/api/1.0/users/me',
			type: 'GET',
			dataType: 'json',
			username: '',
			success: function(json){
				$scope.$apply(function(){
					$scope.page = json.data;
				});
		}
	});
		
	$scope.getData = function(){
		return $scope;
	};

}
