const ctx = document.getElementById('revenueChart').getContext('2d');

function revenueChart() {
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Total revenue',
          data: total_revenues,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)',
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)',
          ],
          borderWidth: 1,
          yAxisID: 'y1',
          type: 'bar',
        },
        {
          label: 'Item count',
          data: count,
          backgroundColor: 'rgba(255, 166, 158, 0.2)',
          borderColor: 'rgba(255, 166, 158, 1)',
          borderWidth: 2,
          yAxisID: 'y2',
        },
      ],
    },
    options: {
      scales: {
        y1: {
          beginAtZero: true,
          position: 'right',
          ticks: {
            stepsize: 1,
          },
        },
        y2: {
          position: 'left',
        },
      },
    },
  });
}

revenueChart();
