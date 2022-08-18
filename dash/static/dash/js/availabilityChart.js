//console.log('hi');
const ctx3 = document.getElementById('availabilityChart').getContext('2d');
const availabilityChart = new Chart(ctx3, {
    type: 'doughnut',
    data: {
        labels: ['Uptime','Downtime'],
        datasets: [{
            label: 'data',
            data: uptimedata,
            backgroundColor: uptimecolor
        }]
    },
    options: {
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
                text: String(uptimelabel)+'%',
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