<template>
  <div class="paper">
    <slot />
  </div>
</template>

<script>
export default {
  name: "paper",
  data() {
    return {};
  },
};
</script>

<style scoped>
.paper {
  margin: 2% auto;
  width: 50vw;
  height: 30vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  box-shadow: var(--panel-shadow);
  border-radius: 4px;
  user-select: none;
}
</style>