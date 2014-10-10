window.fbAsyncInit = function() {
	FB.init({
	  appId      : '839210319436433',
	  xfbml      : true,
	  version    : 'v2.1'
	});
	initialize();
};
(function(d, s, id){
	 var js, fjs = d.getElementsByTagName(s)[0];
	 if (d.getElementById(id)) {return;}
	 js = d.createElement(s); js.id = id;
	 js.src = "//connect.facebook.net/en_US/sdk.js";
	 fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));



function initialize() {
	var user;
	var baseUrl = "https://graph.facebook.com/v2.1/";
	getLoginStatus();
    $("#login-fb").click(function(){
    	getLoginStatus(login);
    })
    $("#logout-fb").click(logout);
    $("#post").submit(function(){
    	if(user){
    		var msg = $("#post textarea").val();
    		postToFB(msg);
    		return false;
    	}else{
    		alert("Please Login to post");
    		return false;
    	}
    });

    function getLoginStatus(callback){
    	FB.getLoginStatus(function(response){
    		if(response.status=="connected"){
    			getFBresponse(response);
    			toggleLogin();
    		}else if(typeof callback === 'function' && callback()){
    			callback(response);
    		}
    	});
    }
    function postToFB(message){
    	var url = baseUrl + user.userID + "/feed/";
    	var data = {
					method: "post",
					message: message,
					access_token: user.accessToken
				};
		$.get(url,data,function(response){
					if(response.id){
                        alert('POSTED!')
						var msg = $("#post textarea").val("");
					}else{
						alert('An error occured. Try to reload the page and try again.')
					}
				});	
    }
    function getFBresponse(response){
    	user=response.authResponse;
    }
    function login(){
    	FB.login(function(response){
    		if(response.authResponse){
    			getFBresponse(response);
    			toggleLogin();
    		}
    	}, {scope: 'publish_actions',return_scopes:true});
    }
    function logout(){
    	FB.logout(function(){
    		toggleLogin();
    		user=null;
    	});
	}

    function toggleLogin(){
		$("#login-fb,#logout-fb").toggle();
    }
}

(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=839210319436433&version=v2.0";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));