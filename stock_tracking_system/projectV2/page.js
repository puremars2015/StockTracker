import { Constants } from "./constants";
import { SubPage } from "./subpage";

class Page {
    constructor(no) {
        this.Constants = new Constants();
        this.no = no;
        this.ctx = document.getElementById('chart' + no);
        this.labels = [];
        this.datapoints = [];
        this.data = {
            labels: this.labels,
            datasets: [
                {
                    label: '股價數據',
                    data: this.datapoints,
                    borderColor: this.CHART_COLORS.green,
                    fill: false,
                    tension: 0
                }
            ],
            stockCode: null,
            pointTime: null
        };
        this.config = {
            type: 'line',
            data: this.data,
            options: {
                responsive: false,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: '------------Chart Title------------'
                    }

                },
                interaction: {
                    intersect: false,
                },
                scales: {
                    x: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Date'
                        }
                    },
                    y: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Price'
                        }
                    }
                }
            },
        };
        this.myChart = new Chart(this.ctx, this.config);
    }
}