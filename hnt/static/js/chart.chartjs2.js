$(function(){
  'use strict';

  var ctx1 = document.getElementById('chart1').getContext('2d');
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

  var ctx2 = document.getElementById('chart2').getContext('2d');
  var myChart2 = new Chart(ctx2, {
    type: 'line',
    data: {
      labels: ['Sun','Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat'],
      datasets: [{
        data: [18,23,11,1,24,12, 39, 20, 10, 25, 18],
        borderColor: 'orange',
        label: '# Votes',
        backgroundColor: '#FFF9D4'

      }]
    },
    options: {
      legend: {
        display: false,
          labels: {
            display: false
          },
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

  var ctb3 = document.getElementById('chart3').getContext('2d');
  new Chart(ctb3, {
    type: 'line',
    data: {
      labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
      datasets: [{
        data: [12, 39, 20, 10, 25, 18],
        borderColor: 'orange',
        label: '# Votes',
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
          }, gridLines:{
            display:false}
        }],
        xAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 11,
            max: 80
          }, gridLines:{
            display:false}
        }]
      }
    }
  });

  var ctb4 = document.getElementById('chart4').getContext('2d');
  new Chart(ctb4, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      datasets: [{
        label: '# of Votes',
        data: [12, 39, 20, 10, 25, 18,6,24,15,32,12,20,],
        borderColor: 'orange',
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
            fontSize: 10
          }, gridLines:{
            display:false}
        }],
        xAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 11,
            max: 80
          }, gridLines:{
            display:false}
        }]
      }
    }
  });

  /* LINE CHART */
  var ctx3 = document.getElementById('chartLine1');
  var myChart3 = new Chart(ctx3, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [{
        label: '# of Votes',
        data: [12, 39, 20, 10, 25, 18],
        borderColor: 'orange',
        borderWidth: 1,
        fill: false
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
          }
        }],
        xAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 11
          }
        }]
      }
    }
  });

  var ctx4 = document.getElementById('chartLine2');
  var myChart4 = new Chart(ctx4, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [{
        data: [12, 39, 20, 10, 20, 18],
        borderColor: '#324463',
        borderWidth: 1,
        fill: false
      },{
        data: [30, 50, 28, 23, 25, 28],
        borderColor: 'orange',
        borderWidth: 1,
        fill: false
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
          }
        }],
        xAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 11
          }
        }]
      }
    }
  });
  


  /** AREA CHART **/
  var ctx5 = document.getElementById('chartArea1');
  var myChart5 = new Chart(ctx5, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [{
        data: [12, 39, 20, 10, 25, 18],
        backgroundColor: '#7CBDDF', //rgba(240, 113, 36, 0.4)
        fill: true,
        borderWidth: 0,
        borderColor: '#fff'
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
          }
        }],
        xAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 11
          }
        }]
      }
    }
  });

  var ctx6 = document.getElementById('chartArea2');
  new Chart(ctx6, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [{
        data: [10, 24, 20, 25, 35, 50],
        backgroundColor: '#677489',
        borderWidth: 1,
        fill: true
      },{
        data: [20, 30, 28, 33, 45, 65],
        backgroundColor: '#218bc2',
        borderWidth: 1,
        fill: true
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
          }
        }],
        xAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 11
          }
        }]
      }
    }
  });

  /** STACKED BAR CHART **/
  var ctx7 = document.getElementById('chartStacked1');
  new Chart(ctx7, {
    type: 'bar',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [{
        data: [10, 24, 20, 25, 35, 50],
        backgroundColor: '#677489',
        borderWidth: 1,
        fill: true
      },{
        data: [10, 24, 20, 25, 35, 50],
        backgroundColor: '#218bc2',
        borderWidth: 1,
        fill: true
      },{
        data: [20, 30, 28, 33, 45, 65],
        backgroundColor: '#7CBDDF',
        borderWidth: 1,
        fill: true
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
          stacked: true
        }],
        xAxes: [{
          stacked: true
        }]
      }
    }
  });

  var ctx8 = document.getElementById('chartStacked2');
  new Chart(ctx8, {
    type: 'horizontalBar',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [{
        data: [10, 24, 20, 25, 35, 50],
        backgroundColor: '#677489',
        borderWidth: 1,
        fill: true
      },{
        data: [10, 24, 20, 25, 35, 50],
        backgroundColor: '#218bc2',
        borderWidth: 1,
        fill: true
      },{
        data: [20, 30, 28, 33, 45, 65],
        backgroundColor: '#7CBDDF',
        borderWidth: 1,
        fill: true
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
          stacked: true
        }],
        xAxes: [{
          stacked: true
        }]
      }
    }
  });


  /** PIE CHART **/
  var randomScalingFactor = function() {
    return Math.round(Math.random() * 100);
  };

  var datapie = {
    datasets: [{
      data: [
        randomScalingFactor(),
        randomScalingFactor(),
        randomScalingFactor(),
        randomScalingFactor(),
        randomScalingFactor(),
      ],
      backgroundColor: [
        '#677489',
        '#218bc2',
        '#7CBDDF',
        '#5B93D3',
        '#324463'
      ]
    }]
  };

  var optionpie = {
    responsive: true,
    legend: {
      display: false,
    },
    animation: {
      animateScale: true,
      animateRotate: true
    }
  };

  // For a doughnut chart
  var ctx6 = document.getElementById('chartPie');
  var myPieChart6 = new Chart(ctx6, {
    type: 'doughnut',
    data: datapie,
    options: optionpie
  });

  // For a pie chart
  var ctx7 = document.getElementById('chartDonut');
  var myPieChart7 = new Chart(ctx7, {
    type: 'pie',
    data: datapie,
    options: optionpie
  });

});
