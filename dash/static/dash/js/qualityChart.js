//console.log('hi');
const ctx6 = document.getElementById('qualityChart').getContext('2d');
const qualityChart = new Chart(ctx6, {
    type: 'doughnut',
    data: {
        labels: ['Uptime','Downtime'],
        datasets: [{
            label: 'data',
            data: qualitydata,
            backgroundColor: qualitycolor
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
                text: 'Quality',
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
                text: String(qualitylabel)+'%',
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