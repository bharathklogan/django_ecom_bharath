function check_title_fields() {
	alert('hereeeeeeeeeeeeeeeee');
	var a = document.getElementById('store_id').value;
	alert('aaaaaaaaaaaaaaaaaaaaaaaaa' + a); 
	if(document.getElementById('store_id').value == '') {
		alert('Please give valid store number');
		document.getElementById('store_id').focus()
	}
}