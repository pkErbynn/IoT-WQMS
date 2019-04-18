$(function(){
  'use strict';

  var ctx1 = document.getElementById('chartsm1H').getContext('2d');
  var myChart1 = new Chart(ctx1, {
    type: 'line',
    data: {
      labels: time,
      datasets: [{
        data: s_moist,
        borderColor: '#017afd',
        label: '# Votes ',
        backgroundColor: '#e8f6f9'

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
