$(function(){
  'use strict';

  var ctx1 = document.getElementById('chartst1H').getContext('2d');
  var myChart1 = new Chart(ctx1, {
    type: 'line',
    data: {
      labels: time,
      datasets: [{
        data: soil_temp,
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
            //beginAtZero:true,
            fontSize: 10,
             // max: 40,
	      steps: 0.5,
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
