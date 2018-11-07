const myChart = document.getElementById('lineChart');
console.log(myChart);

let lineChart = new Chart(myChart, {
    type: 'line ',
    data: {
        labels: ['January', 'February', 'March', 'April', 'June', 'July'],
        datasets: [
            {
                label: 'My First dataset',
                fill: false,
                lineTension: 0.1,
                backgroundColor: "rgba(75,192,192, 0.4)",
                borderColor: 'rgba(75,192,192,1)',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: 'rgba(75,192,192,1)',
                pointBackgroundColor: '#fff',
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor:'rgba(75,192,192,1)',
                pointHoverBorderColor:'rgba(220,220,220,1)',
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: [65, 59, 80, 81, 56, 55, 40],
            }
        ]
    }
});  



// var ctx = document.getElementById('myChart').getContext('2d');
// var chart = new Chart(ctx, {
//     // The type of chart we want to create
//     type: 'line',

//     // The data for our dataset
//     data: {
//         labels: ["January", "February", "March", "April", "May", "June", "July"],
//         datasets: [{
//             label: "My First dataset",
//             backgroundColor: 'rgb(255, 99, 132)',
//             borderColor: 'rgb(255, 99, 132)',
//             data: [0, 10, 5, 2, 20, 30, 45],
//         }]
//     },

//     // Configuration options go here
//     options: {}
// });