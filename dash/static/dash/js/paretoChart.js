//console.log('im in');
const ctx = document.getElementById('paretoChart').getContext('2d');
const paretoChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: paretolabels,
        datasets: [{
            label: 'downtime',
            data: paretodata,
            backgroundColor: [
                'rgba(255,5,5,0.9)',
                'rgba(255,91,0,0.9)',
                'rgba(255,143,0,0.9)',
                'rgba(255,195,2,0.9)',
                'rgba(255,246,0,0.9)',
            ],
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                grid: {
                    color: '#dee2e6',
                    drawBorder: false
                },
                ticks: {
                    color: '#333333',
                    padding: 10,
                    font: {
                        size: 16
                    }
                }
            },
            x: {
                grid: {
                    display: false,
                    drawBorder: false,
                    drawTicks: false
                },
                ticks: {
                    color: '#333333'
                }
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
});