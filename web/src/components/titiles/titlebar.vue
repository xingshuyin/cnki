<template>
  <div class="titlebar">
    <div class="bar"></div>
    <slot></slot>
  </div>
</template>

<script setup>
</script>

<style scoped>
.titlebar{
  width: 100%;
  height: 30px;
  font-size: 16px;
  background: linear-gradient(to right, #011229a1, #021c2e52);
  display: flex;
  flex-direction: row;
  align-items: center;
  border-radius: 2px;
  margin-bottom: 7px;
  padding-right: 8px;
  width: min-content;
  white-space: nowrap;
  color: white;
  .bar{
    height: 100%;width: 10px;background: rgb(12, 255, 12);margin-right: 7px;
  }
}


</style>