const ctx2 = document.getElementById('pieChart').getContext('2d');
const pieChart = new Chart(ctx2, {
    type: 'pie',
    data: {
        labels: ['TEST1','TEST2','TEST3'],
        datasets: [{
            label: 'My First Dataset',
            data: [300, 50, 100],
            backgroundColor: [
              'rgb(255, 99, 132)',
              'rgb(54, 162, 235)',
              'rgb(255, 205, 86)',
              'rgb(65, 158, 64)',
              'rgb(88, 255, 14)'
            ]
        }]
    }
});