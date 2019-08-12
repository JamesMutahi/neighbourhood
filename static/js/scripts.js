$(document).ready(function() {
//Preloader
$(window).on("load", function() {
let preloaderFadeOutTime = 1000;
function hidePreloader() {
var preloader = $('.spinner-wrapper');
preloader.fadeOut(preloaderFadeOutTime);
}
hidePreloader();
});
});

$(function() {
//animations
  $(".menu-link").click(function(e) {
    e.preventDefault();
    $(".menu").toggleClass("open");
    $(".menu-overlay").toggleClass("open");
  });
  $('.menu-link').click(function(){
		$('.home').toggleClass('animated fadeInDown slow');
		$('.gall').toggleClass('animated fadeInDown slow delay-1s');
		$('.featured').toggleClass('animated fadeInDown slow delay-2s');
		$('.log').toggleClass('animated fadeIn slower delay-2s');
		$('.socials').toggleClass('animated fadeIn delay-2s');
		});

  })

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}


