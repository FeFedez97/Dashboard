const ctx2 = document.getElementById('pieChart').getContext('2d');
const pieChart = new Chart(ctx2, {
    type: 'pie',
    plugins: [ChartDataLabels],
    data: {
        //labels: labels1.concat(labels2),
        datasets: [
        {
            label: 'Reason',
            labels: labels2,
            data: pielvl2,
            backgroundColor: piecolors2
        },
        {
            label: 'Machine',
            labels: labels1,
            data: pielvl1,
            backgroundColor: piecolors1,
            datalabels: {
                font: {
                    weight: 'bold',
                    size: 14
                }
            }
        }]
    },
    options:{
        maintainAspectRatio: false,
        plugins:{
            legend:{
                display: false
            },
            datalabels: {
                color: '#FFFFFF',
                textAlign: 'center',

                formatter: function(value, context){
                    return context.chart.data.datasets[context.datasetIndex].labels[context.dataIndex] + "\n" + value
                }
            },
            tooltip:{
                callbacks:{
                    label: function(context){
                        const level = context.chart.data.datasets[context.datasetIndex].labels[context.dataIndex];
                        return level + ": " + context.formattedValue;
                    }
                }
            }
        }
    }
});
