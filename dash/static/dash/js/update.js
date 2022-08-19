$(document).ready(function(){

    setInterval(function(){
      $.ajax({
          url: ajaxurl,
          type: "GET",
          dataType: "json",
          success: (response_data) => {
            console.log(response_data);

            //update timeline
            timelineChart.data.labels = response_data.timeline.labels;
            timelineChart.data.datasets[0].data = response_data.timeline.timelines[0];
            timelineChart.data.datasets[1].data = response_data.timeline.timelines[1];
            timelineChart.update();

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
            availabilityChart.data.datasets[0].data = response_data.uptime.nums;
            availabilityChart.data.datasets[0].backgroundColor = response_data.uptime.colors;
            availabilityChart.options.plugins.subtitle.text = String(response_data.uptime.uptime) + '%';
            availabilityChart.update();

            //update performance
            performanceChart.data.datasets[0].data = response_data.performance.nums;
            performanceChart.data.datasets[0].backgroundColor = response_data.performance.colors;
            performanceChart.options.plugins.subtitle.text = String(response_data.performance.performance) + '%';
            performanceChart.update();

            //update quality
            qualityChart.data.datasets[0].data = response_data.quality.nums;
            qualityChart.data.datasets[0].backgroundColor = response_data.quality.colors;
            qualityChart.options.plugins.subtitle.text = String(response_data.quality.quality) + '%';
            qualityChart.update();

            //update oee
            oeeChart.data.datasets[0].data = response_data.oee.nums;
            oeeChart.data.datasets[0].backgroundColor = response_data.oee.colors;
            oeeChart.options.plugins.subtitle.text = String(response_data.oee.oee) + '%';
            oeeChart.update();

          },
          error: (error) => {
            console.log(error);
          }
      });
    }, 10000);

});