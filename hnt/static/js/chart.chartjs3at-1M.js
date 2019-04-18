$(function(){
  'use strict';

  var ctx1 = document.getElementById('chartat1M').getContext('2d');
  var myChart1 = new Chart(ctx1, {
    type: 'line',
    data: {
        labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        datasets: [{
          data: [12, 39, 20, 10, 25, 18],        
            borderColor: 'red',
        label: '# Votes ',
        backgroundColor: '#FFDFDF'

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
