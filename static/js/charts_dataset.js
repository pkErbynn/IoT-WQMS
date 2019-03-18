
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
            data: [15, 10, 5, 2],
        }]
    },
    // Configuration options go here
    options: {}
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
        }]
    },
    // Configuration options go here
    options: {}
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
        }]
    },
    // Configuration options go here
    options: {}
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
        }]
    },
    // Configuration options go here
    options: {}
});