<template>
  <paper id="graph" v-if="plots.length > 0">
    <apexchart
      width="550"
      height="350"
      type="line"
      :options="chartOptions"
      :series="getSeries"
    ></apexchart>
  </paper>
</template>
<script>
import { toRaw } from "vue";
import VueApexCharts from "vue3-apexcharts";
import Paper from "./Paper.vue";

export default {
  name: "graph",
  components: {
    Paper,
    apexchart: VueApexCharts,
  },
  props: {
    plots: {
      type: Array,
    },
  },
  data() {
    return {
      chartOptions: {
        chart: {
          id: "vuechart-example",
          toolbar: false,
          foreColor: "#fff",
        },
        xaxis: {
          categories: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        },
        yaxis: {
          categories: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        },
        colors: ["#546E7A", "#E91E63"],
        tooltip: { enabled: false },
      },
      series: [
        {
          name: "Benford's Law",
          data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6],
        },
        {
          name: "Your Data",
          data: [],
        },
      ],
    };
  },
  created() {
    this.series[1].data = this.plots;
  },
  computed: {
    getSeries() {
      this.series[1].data = this.plots;
      this.series = [
        {
          name: "Benford's Law",
          data: [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6],
        },
        { name: "Your Data", data: toRaw(this.plots) },
      ];
      console.log("watch", this.series);
      return this.series;
    },
  },
};
</script>

<style>
#graph {
  width: 70vw;
  height: 50vh;
}
</style>