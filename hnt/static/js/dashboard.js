$(function(){
  'use strict';

  var rs1 = new Rickshaw.Graph({
    element: document.querySelector('#rs1'),
    renderer: 'area',
    stroke: true,
    series: [{
      data: [
        { x: 0, y: 13 },
        { x: 1, y: 15 },
        { x: 2, y: 16 },
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
      color: '#017afd',
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
    stroke: true,
    series: [{
      data: [
        { x: 0, y: 9 },
        { x: 1, y: 7 },
        { x: 2, y: 30 },
        { x: 3, y: 12 },
        { x: 4, y: 16 },
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
      color: 'orange',
    }]
  });
  rs2.render();

  var rs3 = new Rickshaw.Graph({
    element: document.querySelector('#rs3'),
    renderer: 'area',
    stroke: true,
    series: [{
      data: [
        { x: 0, y: 9 },
        { x: 1, y: 7 },
        { x: 2, y: 20 },
        { x: 3, y: 22 },
        { x: 4, y: 16 },
        { x: 5, y: 10 },
        { x: 6, y: 20 },
        { x: 7, y: 7 },
        { x: 8, y: 6 },
        { x: 9, y: 8 },
        { x: 10, y: 9 },
        { x: 11, y: 10 },
        { x: 12, y: 8 },
        { x: 13, y: 10 }
      ],
      color: '#40e0d0',
    }]
  });
  rs3.render();


    var rs4 = new Rickshaw.Graph({
    element: document.querySelector('#rs4'),
    renderer: 'bar',
    stroke: true,
    series: [{
      data: [
        { x: 0, y: 9 },
        { x: 1, y: 7 },
        { x: 2, y: 30 },
        { x: 3, y: 12 },
        { x: 4, y: 16 },
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
      color: '#ADD8E6',
    }]
  });
  rs4.render();

  var rs5 = new Rickshaw.Graph({
    element: document.querySelector('#rs5'),
    renderer: 'area',
    stroke: true,
    series: [{
      data: [
        { x: 0, y: 9 },
        { x: 1, y: 7 },
        { x: 2, y: 30 },
        { x: 3, y: 12 },
        { x: 4, y: 16 },
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
      color: 'red',
    }]
  });
  rs5.render();






  // Responsive Mode
  new ResizeSensor($('.kt-mainpanel'), function(){
    rs2.configure({
      width: $('#rs2').width(),
      height: $('#rs2').height()
    });
    rs2.render();
  });

  var ctb4 = document.getElementById('chartBar4').getContext('2d');
  new Chart(ctb4, {
    type: 'horizontalBar',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
      datasets: [{
        label: '# of Votes',
        data: [15, 29, 33, 10, 22, 19, 10, 18],
        backgroundColor: [
          '#f1116a',
          '#017afd',
          '#0063d3',
          '#f3a344',
          '#95c75d',
          '#17A2B8',
          'red',
          '#6F42C1'
        ]
      }]
    },
    options: {
      legend: {
        display: false,
          labels: {
            display: false
          }
      },
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 10
          }
        }],
        xAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 11,
            max: 50
          }
        }]
      }
    }
  });

});
