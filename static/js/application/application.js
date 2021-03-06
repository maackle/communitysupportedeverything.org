$(document).ready(function() {
    var pageHeight = $(window).height();
    var pageWidth = $(window).width();
    var navigationHeight = $("#navigation").outerHeight();
    $(window).resize(function() {
        pageWidth = $(window).width();
        pageHeight = $(window).height();
    });
    $(window).trigger('scroll');
    $('#navigation').fixedonlater({
        speedDown: 250,
        speedUp: 100
    });
    $('.centralized').centralized({
        delay: 1500,
        fadeSpeed: 500
    });
    $.fn.responsivevideos();
    $('#quote-slider').each(function() {
        if ($('.item', this).length) {
            $(this).carousel({
                interval: 20000
            });
        }
    });
    $('#main-menu').onePageNav({
        currentClass: "active",
        changeHash: false,
        scrollOffset: navigationHeight - 10,
        scrollThreshold: 0.5,
        scrollSpeed: 750,
        filter: "",
        easing: "swing"
    });
    if (pageWidth > 980) {
        $('#page-welcome').parallax("0%", 0.2);
//        $('#image-rotator img').parallax("0%", 0.07);
        $('#page-features').parallax("0%", 0.07);
        $('#page-twitter').parallax("0%", 0.1);
    }
    if (typeof(window.ontouchstart) != 'undefined') {
        var touchElements = [".social-icons a", ".portfolio-items li", ".about-items .item"];
        $.each(touchElements, function(i, val) {
            $(val).each(function(i, obj) {
                $(obj).bind('click', function(e) {
                    if ($(this).hasClass('clickInNext')) {
                        $(this).removeClass('clickInNext');
                    } else {
                        e.preventDefault();
                        e.stopPropagation();
                        $(this).mouseover();
                        $(this).addClass('clickInNext');
                    }
                });
            });
        });
    }
    $('#page-welcome .logo a').click(function() {
        $('html, body').animate({
            scrollTop: $($.attr(this, 'href')).offset().top - navigationHeight + 4
        }, 800);
        setTimeout(function() {
            $(window).trigger('scroll');
        }, 900);
        return false;
    });
/*
    var $imageDiv = $("#image-rotator");
    var $imageRotator = $imageDiv.imageRotator({
        imageTime: 6000,
        fadeTime: 4000
    });
    $imageRotator.start();
*/
    
    $('.plugin-filter').click(function() {
        return false;
    });
    $('.plugin-filter-elements').mixitup({
        targetSelector: '.mix',
        filterSelector: '.plugin-filter',
        sortSelector: '.sort',
        buttonEvent: 'click',
        effects: ['fade', 'rotateY'],
        listEffects: null,
        easing: 'smooth',
        layoutMode: 'grid',
        targetDisplayGrid: 'inline-block',
        targetDisplayList: 'block',
        gridClass: '',
        listClass: '',
        transitionSpeed: 600,
        showOnLoad: 'all',
        sortOnLoad: false,
        multiFilter: false,
        filterLogic: 'or',
        resizeContainer: true,
        minHeight: 0,
        failClass: 'fail',
        perspectiveDistance: '3000',
        perspectiveOrigin: '50% 50%',
        animateGridList: true,
        onMixLoad: null,
        onMixStart: null,
        onMixEnd: null
    });
    $('#twitterfeed-slider').tweet({
        modpath: 'plugins/twitter/',
        username: 'TheGridelicious',
        count: 3
    });
    $('#twitterfeed-slider').tweetCarousel({
        interval: 7000,
        pause: "hover"
    });
});
$(document).ajaxSend(function() {
    if ($(".loading").length == 0) {
        $("body").append('<div class="loading"><div class="progress progress-striped active"><div class="bar"></div></div></div>');
        $(".loading").slideDown();
        $(".loading .progress .bar").delay(300).css("width", "100%");
    }
});
$(document).ajaxComplete(function() {
    $(".loading").delay(1000).slideUp(500, function() {
        $(this).remove();
    });
    $(".close-portfolio span").click(function(e) {
        $(".portfolio-item-details").delay(500).slideUp(500, function() {
            $(this).remove();
        });
        window.location.hash = "!";
        return false;
    });
});