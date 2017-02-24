/**
 * Created by Anders on 2/24/2017.
 */
$.ajax({
	url: 'https://api.randomuser.me',
	method: 'GET',
	data: {'results' : 5},
	success: function(rsp){
	console.log(rsp);
},
	error: function(err){
	console.log(err);
}
});