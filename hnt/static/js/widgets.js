$(function(){
  'use strict';

  var styleMapBox = [{
    'featureType': 'water',
    'stylers': [{
      'saturation': 43
    }, {
      'lightness': -11
    }, {
      'hue': '#0088ff'
    }]
  }, {
    'featureType': 'road',
    'elementType': 'geometry.fill',
    'stylers': [{
      'hue': '#ff0000'
    }, {
      'saturation': -100
    }, {
      'lightness': 99
    }]
  }, {
    'featureType': 'road',
    'elementType': 'geometry.stroke',
    'stylers': [{
      'color': '#808080'
    }, {
      'lightness': 54
    }]
  }, {
    'featureType': 'landscape.man_made',
    'elementType': 'geometry.fill',
    'stylers': [{
      'color': '#ece2d9'
    }]
  }, {
    'featureType': 'poi.park',
    'elementType': 'geometry.fill',
    'stylers': [{
      'color': '#ccdca1'
    }]
  }, {
    'featureType': 'road',
    'elementType': 'labels.text.fill',
    'stylers': [{
      'color': '#767676'
    }]
  }, {
    'featureType': 'road',
    'elementType': 'labels.text.stroke',
    'stylers': [{
      'color': '#ffffff'
    }]
  }, {
    'featureType': 'poi',
    'stylers': [{
      'visibility': 'off'
    }]
  }, {
    'featureType': 'landscape.natural',
    'elementType': 'geometry.fill',
    'stylers': [{
      'visibility': 'on'
    }, {
      'color': '#b8cb93'
    }]
  }, {
    'featureType': 'poi.park',
    'stylers': [{
      'visibility': 'on'
    }]
  }, {
    'featureType': 'poi.sports_complex',
    'stylers': [{
      'visibility': 'on'
    }]
  }, {
    'featureType': 'poi.medical',
    'stylers': [{
      'visibility': 'on'
    }]
  }, {
    'featureType': 'poi.business',
    'stylers': [{
      'visibility': 'simplified'
    }]
  }];

  var map1 = GMaps.staticMapURL({
    size: [600, 400],
    zoom: 14,
    lat: 40.702247,
    lng: -73.996349,
    key: 'AIzaSyAEt_DBLTknLexNbTVwbXyq2HSf2UbRBU8',
    styles: styleMapBox
  });

  $('<img class="img-fluid" alt="">').attr('src', map1).appendTo('#map1');


  var rs1 = new Rickshaw.Graph({
    element: document.querySelector('#rs1'),
    renderer: 'area',
    series: [{
      data: [
        { x: 0, y: 13 },
        { x: 1, y: 12 },
        { x: 2, y: 10 },
        { x: 3, y: 11 },
        { x: 4, y: 12 },
        { x: 5, y: 10 },
        { x: 6, y: 12 },
        { x: 7, y: 10 },
        { x: 8, y: 12 },
        { x: 9, y: 14 },
        { x: 10, y: 8 },
        { x: 11, y: 15 },
        { x: 12, y: 7 },
        { x: 13, y: 10 }
      ],
      color: '#DFDFDF',
    }]
  });
  rs1.render();

  // Responsive Mode
  new ResizeSensor($('.kt-mainpanel'), function(){
    rs1.configure({
      width: $('#rs1').width(),
      height: $('#rs1').height()
    });
    rs1.render();
  });

  var rs2 = new Rickshaw.Graph({
    element: document.querySelector('#rs2'),
    renderer: 'area',
    series: [{
      data: [
        { x: 0, y: 5 },
        { x: 1, y: 7 },
        { x: 2, y: 10 },
        { x: 3, y: 11 },
        { x: 4, y: 12 },
        { x: 5, y: 10 },
        { x: 6, y: 9 },
        { x: 7, y: 7 },
        { x: 8, y: 6 },
        { x: 9, y: 8 },
        { x: 10, y: 9 },
        { x: 11, y: 10 },
        { x: 12, y: 7 },
        { x: 13, y: 10 }
      ],
      color: '#DFDFDF',
    }]
  });
  rs2.render();

  // Responsive Mode
  new ResizeSensor($('.kt-mainpanel'), function(){
    rs2.configure({
      width: $('#rs2').width(),
      height: $('#rs2').height()
    });
    rs2.render();
  });

  var rs3 = new Rickshaw.Graph({
    element: document.querySelector('#rs3'),
    renderer: 'bar',
    series: [{
      data: [
        { x: 0, y: 5 },
        { x: 1, y: 7 },
        { x: 2, y: 10 },
        { x: 3, y: 11 },
        { x: 4, y: 12 },
        { x: 5, y: 10 },
        { x: 6, y: 9 },
        { x: 7, y: 7 },
        { x: 8, y: 6 },
        { x: 9, y: 8 },
        { x: 10, y: 9 },
        { x: 11, y: 10 },
        { x: 12, y: 7 },
        { x: 13, y: 10 }
      ],
      color: '#17ABCC',
    }]
  });
  rs3.render();

  // Responsive Mode
  new ResizeSensor($('.kt-mainpanel'), function(){
    rs3.configure({
      width: $('#rs3').width(),
      height: $('#rs3').height()
    });
    rs3.render();
  });

  var rs4 = new Rickshaw.Graph({
    element: document.querySelector('#rs4'),
    renderer: 'line',
    series: [{
      data: [
        { x: 0, y: 5 },
        { x: 1, y: 7 },
        { x: 2, y: 10 },
        { x: 3, y: 11 },
        { x: 4, y: 12 },
        { x: 5, y: 10 },
        { x: 6, y: 9 },
        { x: 7, y: 7 },
        { x: 8, y: 6 },
        { x: 9, y: 8 },
        { x: 10, y: 9 },
        { x: 11, y: 10 },
        { x: 12, y: 7 },
        { x: 13, y: 10 }
      ],
      color: '#17ABCC',
    }]
  });
  rs4.render();

  // Responsive Mode
  new ResizeSensor($('.kt-mainpanel'), function(){
    rs4.configure({
      width: $('#rs4').width(),
      height: $('#rs4').height()
    });
    rs4.render();
  });

});
