$(function(){
    "use strict";

    //Activate main slider
    $("#featured").carousel({
       interval: 3000,
       pause:"hover",
       keyboard:true
   });


   //////////////////// Search JS
    $('a[href="#search"]').on('click', function(event) {
        event.preventDefault();
        $('#search').addClass('open');
        $('#search > form > input[type="search"]').focus();
    });

    $('#search, #search button.close').on('click keyup', function(event) {
        if (event.target == this || event.target.className == 'close' || event.keyCode == 27) {
            $(this).removeClass('open');
        }
    });

    /* scroll to top code*/



    var amountScrolled = 300;

    $(window).scroll(function() {
    	if ( $(window).scrollTop() > amountScrolled ) {
    		jQuery('a.back-to-top').fadeIn('slow');
    	} else {
    		jQuery('a.back-to-top').fadeOut('slow');
    	}
    });

    $('a.back-to-top').click(function() {
    	$('html, body').animate({
    		scrollTop: 0
    	}, 1000);
    	return false;
    });




    // 
    $(document).ready(function(){

    });

    // call functions when browser resizes
    $(window).resize(function(){

    });

});
