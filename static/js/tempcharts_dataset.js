
//Example 1 ==========================================
let temperature = document.querySelector("#temperature").getContext('2d');
let turbidity = document.querySelector("#turbidity").getContext('2d');
let ph = document.querySelector("#ph").getContext('2d');
let water = document.querySelector("#water").getContext('2d');


const temperatureChart = new Chart(temperature, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April"],
        datasets: [{
            label: "Dataset for all temperature measurements",
            borderColor: 'rgb(255, 99, 132)',
            data: [25, 10, 5, 32, 33],
            fill: true,
            backgroundColor: ['rgba(00, 255, 00, 0.1)',],
            borderColor: ['rgba(54, 162, 235, 1)',],
            borderWidth: 1.5
        }]
    },
    // Configuration options go here
    options: {
        legend: false,
        elements: {
            line: {
                fill: false,
            },
            point: {
                // hoverBackgroundColor: makeHalfAsOpaque,
                // radius: adjustRadiusBasedOnData,
                
                hoverRadius: 8,
            }

        }
        
    }
});

const turbidityChart = new Chart(turbidity, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April"],
        datasets: [{
            label: "Dataset for Turbidity measurements",
            borderColor: 'rgb(255, 99, 132)',
            data: [15, 10, 5, 2],
            backgroundColor: ['rgba(00, 255, 00, 0.1)',],
            borderColor: ['rgba(54, 162, 235, 1)',],
            borderWidth: 1.5,
        }]
    },
    // Configuration options go here
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        },
        legend: false,
        elements: {
            
        }
    }
});

const phChart = new Chart(ph, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April"],
        datasets: [{
            label: "Dataset for pH",
            borderColor: 'rgb(255, 99, 132)',
            data: [15, 10, 5, 2],
            backgroundColor: ['rgba(00, 255, 00, 0.1)',],
            borderColor: ['rgba(54, 162, 235, 1)',],
            borderWidth: 1.5,
        }]
    },
    // Configuration options go here
    options: {
        legend: false,
    }
});

const waterChart = new Chart(water, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April"],
        datasets: [{
            label: "Dataset for Water Level ",
            borderColor: 'rgb(255, 99, 132)',
            data: [15, 10, 5, 2],
            backgroundColor: ['rgba(00, 255, 00, 0.1)',],
            borderColor: '#4dc9f6',
            borderWidth: 1.5
        }]
    },
    // Configuration options go here
    options: {
        legend: false,
    }
});