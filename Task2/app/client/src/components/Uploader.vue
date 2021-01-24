<template>
  <paper>
    <h1 for="uploader">Benford's Law</h1>
    <div class="item">
      <label for="uploader">Select file -</label>
      <input id="uploader" ref="file" type="file" @change="setOptions" />
    </div>

    <div class="item">
      <label for="Select Target Column">Select target column -</label>
      <select name="Select Target Column" ref="selectedColumn">
        <option :key="index" v-for="(option, index) in headers" value="">
          {{ option.name }}
        </option>
      </select>
    </div>
    <button @click="upload">Upload</button>
  </paper>
</template>

<script>
import Paper from "./Paper.vue";
export default {
  name: "uploader",
  components: {
    Paper,
  },
  data() {
    return {
      file: "",
      headers: [{ name: "None", val: -1 }],
    };
  },
  methods: {
    async setOptions() {
      this.file = await this.$refs.file.files[0].text();

      let i = 0;
      let headers = [];
      for (let option of this.file.split("\n")[0].split("\t")) {
        headers.push({ name: option, value: i });
        i += 1;
      }
      this.headers = headers;
      console.log(this.headers);
    },
    async upload() {
      let selectedColumn = await this.$refs.selectedColumn.selectedIndex;
      let vueref = this;

      fetch("/upload", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          column: selectedColumn,
          fileContent: this.file,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          vueref.$emit("plotData", data.bl);
        });
    },
  },
};
</script>

<style>
.item {
  width: 100%;
}
button {
  padding: 1% 3%;
  border-color: gray;
  border-radius: 5px;
  background: rgb(81, 126, 163);
  box-shadow: var(--button_shadow);
  color: whitesmoke;
  font-weight: bold;
}

button:hover {
  box-shadow: var(--button_shadow_hover);
}

input,
select,
button {
  font-size: 14px;
}

label {
  border-radius: 5px;
  padding: 1%;
  border: 1px solid black;
  background: rgba(122, 126, 122, 0.1);
  margin-right: 2%;
}
</style>