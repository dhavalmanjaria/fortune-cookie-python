$(function() {
	var handler = function(event){
		var name = $("input[name='name']").val();
		var birthdate = $("input[name='birthdate']").val();

		$.ajax({
			url: "http://localhost:5002/get-fortune",
			data: {
				"name": name,
				"birthdate": birthdate
			},
			success: function(res) {
				console.log(res);
				$("#fortune").html(res);
			}
		})
	};

	$("#submit-div").bind('tap', handler);
	$("#submit").bind('click', handler);
})