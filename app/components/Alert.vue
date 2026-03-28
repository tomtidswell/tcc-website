<template>
  <div class="alert" :class="color">
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
const { color } = defineProps({
  color: {
    type: String,
    default: 'orange'
  }
})
</script>

<style scoped lang="scss">
.alert {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  border: 2px solid;
  border-radius: 0.5rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  .alert:hover {
    transform: translateY(-2px);
    box-shadow: $alert-shadow-hover;
  }
  &.orange {
    background-color: $alert-orange-bg;
    box-shadow: $alert-shadow;
    color: $alert-orange-text;
    border-color: $alert-orange-border;
  }
  &.red {
    background-color: $alert-red-bg;
    box-shadow: $alert-shadow;
    color: $alert-red-text;
    border-color: $alert-red-border;
  }
}

</style>