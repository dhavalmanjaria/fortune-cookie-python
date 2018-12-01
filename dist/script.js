$(function() {
	$("#fortune").innerHTML = "HEY!";
	$("#form").submit(function(event){
		event.preventDefault();
		
		var name = $("input[name='name']").val();
		var birthdate = $("input[name='birthdate']").val();

		$.ajax({
			url: "http://localhost:5000/get-fortune",
			data: {
				"name": name,
				"birthdate": birthdate
			},
			success: function(res) {
				console.log(res);
				$("#fortune").html(res);
			}
		})
	});
})