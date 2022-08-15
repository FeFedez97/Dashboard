//console.log('hi');
const ctx3 = document.getElementById('availabilityChart').getContext('2d');
const availabilityChart = new Chart(ctx3, {
    type: 'doughnut',
    data: {
        labels: ['Uptime','Downtime'],
        datasets: [{
            label: 'data',
            data: [uptime, 100-uptime],
            backgroundColor: [
              '#0099FF',
              '#D9D9D9',
            ]
        }]
    },
    options: {
        circumference: 180,
        rotation: 270,
        aspectRatio: 1,
        plugins: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: 'Availability',
                align: 'center',
                padding: {
                    top: 2,
                    bottom: 2
                },
                font:{
                    size: 60
                }
            },
            subtitle: {
                display: true,
                text: String(uptime) + '%',
                align: 'center',
                position: 'bottom',
                padding: {
                    top: 2,
                    bottom: 2
                },
                font:{
                    size: 60
                }
            }
        }
    }
});