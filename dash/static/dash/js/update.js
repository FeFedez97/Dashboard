$(document).ready(function(){

    setInterval(function(){
      $.ajax({
          url: ajaxurl,
          type: "GET",
          dataType: "json",
          success: (response_data) => {
            //console.log(response_data);
            paretoChart.data.labels = response_data.categories;
            paretoChart.data.datasets[0].data = response_data.categories_min;
            paretoChart.update();
            pieChart.data.labels = response_data.description;
            pieChart.data.datasets[0].data = response_data.description_min;
            pieChart.data.datasets[0].label = response_data.description;
            pieChart.update();
            availabilityChart.data.datasets[0].data = [response_data.uptime, 100-response_data.uptime];
            availabilityChart.options.subtitle.text = String(response_data.uptime) + '%'
            availabilityChart.update();
           },
          error: (error) => {
            console.log(error);
          }
      });
    }, 10000);

});