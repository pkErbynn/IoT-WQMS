$(function(){
  'use strict';

  var ctx1 = document.getElementById('chartst24H').getContext('2d');
  var myChart1 = new Chart(ctx1, {
    type: 'line',
    data: {
      labels: ['00', '01', '02', '03', '04', '05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23'],
      datasets: [{
        data: [12, 39, 20, 10, 25, 18,25,23,11,1,36,30,12,23,6,24,15,32,12, 39, 20, 10, 25, 18,],
        borderColor: 'orange',
        label: '# Votes ',
        backgroundColor: '#FFF9D4'

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
            fontSize: 10,
            max: 80
          }, gridLines:{
            display:false}
        }],
        xAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 11
          }, gridLines:{
            display:false}
        }]
      }
    }
  });
});
