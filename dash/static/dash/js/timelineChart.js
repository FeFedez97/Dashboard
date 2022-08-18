const ctx4 = document.getElementById('timelineChart').getContext('2d');
const timelineChart = new Chart(ctx4, {
    type: 'bar',
    data: {
        labels: ['11:01', '11:02', '11:03', '11:04', '11:05', '11:06', '11:07', '11:08'],
        datasets: [
        {
            label: 'Production',
            data: [1,1,0,0,1,1,0,0],
            backgroundColor: [
                '#33cc33'
            ],
            order: 1
        },
        {
            label: 'Downtime',
            data: [0,0,1,1,0,0,1,1],
            backgroundColor: [
                '#e62e00'
            ],
            order: 0
        }]
    },
    options:{
        barPercentage: 1.0,
        categoryPercentage: 1.0,
        grouped: false,
        scales: {
            x: {
                //stacked: true
                grid: {
                    display: false
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