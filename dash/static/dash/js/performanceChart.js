//console.log('hi');
const ctx5 = document.getElementById('performanceChart').getContext('2d');
const performanceChart = new Chart(ctx5, {
    type: 'doughnut',
    data: {
        labels: ['Uptime','Downtime'],
        datasets: [{
            label: 'data',
            data: performancedata,
            backgroundColor: performancecolor
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
                text: 'Performance',
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
                text: String(performancelabel)+'%',
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