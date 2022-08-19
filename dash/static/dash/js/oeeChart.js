//console.log('hi');
const ctx7 = document.getElementById('oeeChart').getContext('2d');
const oeeChart = new Chart(ctx7, {
    type: 'doughnut',
    data: {
        labels: ['Uptime','Downtime'],
        datasets: [{
            label: 'data',
            data: oeedata,
            backgroundColor: oeecolor
        }]
    },
    options: {
        aspectRatio: 1,
        maintainAspectRatio: false,
        circumference: 180,
        rotation: 270,
        aspectRatio: 1,
        events: [],
        plugins: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: 'OEE',
                align: 'center',
                padding: {
                    top: 2,
                    bottom: 2
                },
                font:{
                    size: 20
                }
            },
            subtitle: {
                display: true,
                text: String(oeelabel)+'%',
                align: 'center',
                position: 'bottom',
                padding: {
                    top: 2,
                    bottom: 2
                },
                font:{
                    size: 30
                }
            }
        }
    }
});