const ctx4 = document.getElementById('timelineChart').getContext('2d');
const timelineChart = new Chart(ctx4, {
    type: 'bar',
    data: {
        labels: timelinelabels,
        datasets: [
        {
            label: 'Production',
            data: timelines[0],
            backgroundColor: [
                '#33cc33'
            ],
        },
        {
            label: 'Downtime',
            data: timelines[1],
            backgroundColor: [
                '#e62e00'
            ],
        }]
    },
    options:{
        maintainAspectRatio: false,
        barPercentage: 1.0,
        categoryPercentage: 1.0,
        animations: false,
        grouped: false,
        scales: {
            x: {
                //stacked: true
                grid: {
                    display: false
                },
                ticks: {
                    align: 'end',
                    maxRotation: 90,
                    minRotation: 90
                }
            },
            y: {
                display: false,
            }
        },
        plugins: {
            legend: {
                onClick: (e) => e.stopPropagation()
            }
        }
    }
});