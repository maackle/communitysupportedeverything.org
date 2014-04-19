( function( $ ) {

	function removeNoJsClass() {
		$( 'html:first' ).removeClass( 'no-js' );
	}

	/* Superfish the menu drops ---------------------*/
	function superfishSetup() {
		$('.menu').superfish({
			delay: 200,
			animation: {opacity:'show', height:'show'},
			speed: 'fast',
			cssArrows: true,
			autoArrows:  true,
			dropShadows: false
		});
	}
	    
	/* Flexslider ---------------------*/
	function flexSliderSetup() {
		if( ($).flexslider) {
			var slider = $('.flexslider');
			slider.fitVids().flexslider({
				slideshowSpeed		: slider.attr('data-speed'),
				animationDuration	: 600,
				animation			: 'slide',
				video				: false,
				useCSS				: false,
				touch				: false,
				animationLoop		: true,
				smoothHeight		: true,
				
				start: function(slider) {
					slider.removeClass('loading');
				}
			});
		}
	}
	    
   /* Portfolio Filter ---------------------*/
   function isotopeSetup() {
	   	var mycontainer = $('#portfolio-list');
	   	mycontainer.isotope({
	   		itemSelector: '.portfolio-item'
	   	});
   
	   	// filter items when filter link is clicked
	   	$('#portfolio-filter a').click(function(){
	   		var selector = $(this).attr('data-filter');
	   		mycontainer.isotope({ filter: selector });
	   		return false;
	   	});
    }
	    
	function modifyPosts() {
	
		/* Share Modal Box ---------------------*/
		$('.btn-share').click(function(event) {
			event.preventDefault();
			$('#social').modal();
			try {
				FB.XFBML.parse();
			}catch(ex){}
		});
		
		/* Wrap DIV Around Home More ---------------------*/
		$( "#homepage .more-link" ).wrap( "<div class='align-center text-center'></div>" );
		
		/* Fit Vids ---------------------*/
		$('.feature-vid, .postarea, .article').fitVids();
		
		/* jQuery UI Tabs ---------------------*/
		$(function() {
			$( ".organic-tabs" ).tabs();
		});
		
		/* jQuery UI Accordion ---------------------*/
		$(function() {
			$( ".organic-accordion" ).accordion({
				collapsible: true,
				heightStyle: "content"
			});
		});
		
		/* Close Message Box ---------------------*/
		$('.organic-box a.close').click(function() {
			$(this).parent().stop().fadeOut('slow', function() {
			});
		});
		
		/* Toggle Box ---------------------*/
		$('.toggle-trigger').click(function() {
			$(this).toggleClass("active").next().fadeToggle("slow");
		});
	}
	
	$( document )
	.ready( removeNoJsClass )
	.ready( superfishSetup )
	.ready( modifyPosts )
	.on( 'post-load', modifyPosts );
	
	$( window )
	.load( flexSliderSetup )
	.load( isotopeSetup )
	.resize( isotopeSetup );
    
})( jQuery );