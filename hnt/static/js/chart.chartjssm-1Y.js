$(function(){
  'use strict';

  var ctx1 = document.getElementById('chartsm1Y').getContext('2d');
  var myChart1 = new Chart(ctx1, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
          label: '# of Votes',
          data: [12, 39, 20, 10, 25, 18,6,24,15,32,12,20,],        
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
