$(document).ready(function(){

    setInterval(function(){
      $.ajax({
          url: ajaxurl,
          type: "GET",
          dataType: "json",
          success: (response_data) => {
            //console.log(response_data);

            //update pareto
            paretoChart.data.labels = response_data.pareto.labels;
            paretoChart.data.datasets[0].data = response_data.pareto.minutes;
            paretoChart.update();

            //update pie chart
            pieChart.data.datasets[0].data = response_data.pie.failures_times;
            pieChart.data.datasets[0].labels = response_data.pie.failures_labels;
            pieChart.data.datasets[0].backgroundColor = response_data.pie.failures_colors;
            pieChart.data.datasets[1].data = response_data.pie.machines_times;
            pieChart.data.datasets[1].labels = response_data.pie.machines_labels;
            pieChart.data.datasets[1].backgroundColor = response_data.pie.machines_colors;
            pieChart.update();

            //update availability
            availabilityChart.data.datasets[0].data = [response_data.uptime, 100-response_data.uptime];
            availabilityChart.options.plugins.subtitle.text = String(response_data.uptime) + '%'
            availabilityChart.update();
          },
          error: (error) => {
            console.log(error);
          }
      });
    }, 10000);

});