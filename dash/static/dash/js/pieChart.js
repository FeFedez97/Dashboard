const ctx2 = document.getElementById('pieChart').getContext('2d');
const pieChart = new Chart(ctx2, {
    type: 'pie',
    data: {
      //  labels: labels1 + labels2,
        datasets: [
        {
            label: 'Reason',
            labels: labels2,
            data: pielvl2,
            backgroundColor: [
              'rgb(125, 125, 125)',
            ]
        },
        {
            label: 'Machine',
            labels: labels1,
            data: pielvl1,
            backgroundColor: [
                '#5e4fa2',
                '#3288bd',
                '#66c2a5',
                '#abdda4',
                '#e6f598',
                '#fee08b'
            ]
        }]
    },
    options:{
        plugins:{
            legend:{
                display: false
            },
            tooltip:{
                callbacks:{
                    label: function(context){
                        const level = context.chart.data.datasets[context.datasetIndex].labels[context.dataIndex];
                        return level + ":" + context.formattedValue;
                    }
                }
            }
        }
    }
});
