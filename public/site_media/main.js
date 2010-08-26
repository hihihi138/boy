$(document).ready(function(){
	$("#cse").mouseover(function(){
		$(".gsc-adBlock").hide()
	});
	$(":text").click(function(){
		$(this).select()
	});
	if ($.browser.msie && $.browser.version==6.0){$("#side_button").hide();$(".rating").hide()};
});