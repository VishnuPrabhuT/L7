<template>
  <div>
    <h1 for="uploader">Benford's Law</h1>
    <uploader @plotData="plotPoints($event)" />
    <graph v-if="plots.length > 0" :plots="plots" />
  </div>
</template>

<script>
import Uploader from "./components/Uploader.vue";
import Graph from "./components/Graph.vue";

export default {
  name: "app",
  components: {
    Uploader,
    Graph,
  },
  data() {
    return {
      plots: [],
    };
  },
  methods: {
    plotPoints(d) {
      console.log(d);
      this.plots = d;
    },
  },
};
</script>

<style>
:root {
  --soft-black: #333333;
  --c_text_green: #5db85c;
  --panel-shadow: 0px 1px 10px 4px rgba(170, 164, 164, 0.5);
  --button_shadow: 0px 1px 10px 4px rgba(170, 164, 164, 0.2);
  --button_shadow_hover: 0px 1px 10px 4px rgba(170, 164, 164, 0.5);
}
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  outline: none;
}
body {
  max-width: 100vw;
  max-height: 100vh;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: whitesmoke;
  background-color: var(--soft-black);
}

#app {
  height: 100%;
  width: 100%;
  padding: 1%;
}
</style>