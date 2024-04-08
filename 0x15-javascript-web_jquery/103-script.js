$(document).ready(function () {
	$("INPUT#btn_translate").click(fetchTrans);
	$("INPUT#language_code").keyup(function (event) {
		if (event.keyCode === 13) {
			fetchTrans();
		}
	});

	function fetchTrans() {
		const language_code = $("INPUT#language_code").val();
		$.getJSON(
			`https://fourtonfish.com/hellosalut/hello/?lang=${language_code}`,
			function (data) {
				$("#hello").text(data.hello);
			}
		);
	}
});
