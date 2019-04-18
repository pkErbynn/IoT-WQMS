/*!
 * magen-iot-admin v1.0.0
 * Copyright 2017-2018 vueghost
 * Licensed under ThemeForest License
 */

 'use strict';

 $(document).ready(function() {

   // displaying time and date in left sidebar
   var interval = setInterval(function() {
     var momentNow = moment();
     $('#ktDate').html(momentNow.format('MMMM DD, YYYY hh:mm:ss') + ' '
       + momentNow.format('dddd')
       .substring(0,3).toUpperCase());
   }, 100);

   $('.kt-sideleft').perfectScrollbar({
     useBothWheelAxes: false,
     suppressScrollX: true,
     wheelPropogation: true
   });

   // hiding all sub nav in left sidebar by default.
   $('.nav-sub').slideUp();

   // showing sub navigation to nav with sub nav.
   $('.with-sub.active + .nav-sub').slideDown();

   // showing sub menu while hiding others
   $('.with-sub').on('click', function(e) {
     e.preventDefault();

     var nextElem = $(this).next();
     if(!nextElem.is(':visible')) {
       $('.nav-sub').slideUp();
     }
     nextElem.slideToggle();
   });

   // showing and hiding left sidebar
   $('#naviconMenu').on('click', function(e) {
     e.preventDefault();
     $('body').toggleClass('hide-left');
   });

   // pushing to/back left sidebar
   $('#naviconMenuMobile').on('click', function(e) {
     e.preventDefault();
     $('body').toggleClass('show-left');
   });

   // highlight syntax highlighter
   $('pre code').each(function(i, block) {
     hljs.highlightBlock(block);
   });

});
