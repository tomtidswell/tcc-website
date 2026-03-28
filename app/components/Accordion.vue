<template>
  <div class="accordion">
    <button 
      class="accordion-header" 
      @click="isOpen = !isOpen"
      :aria-expanded="isOpen"
    >
      <span class="accordion-title">{{ title }}</span>
      <span class="accordion-icon" :class="{ 'is-open': isOpen }">▼</span>
    </button>
    <div class="accordion-content" :class="{ 'is-open': isOpen }">
      <div class="accordion-body">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { title } = defineProps({
  title: {
    type: String,
    required: true
  }
})

const isOpen = ref(false)
</script>

<style scoped lang="scss">
.accordion {
  border: 1px solid #ffffff3d;
  border-radius: 8px;
  margin-bottom: 1rem;
  overflow: hidden;
  transition: box-shadow 0.2s ease;

  &:hover {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
}

.accordion-header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.25rem;
  background: #ffffff3d;
  border: none;
  cursor: pointer;
  font-size: 1.1rem;
  font-weight: 600;
  text-align: left;
  transition: background-color 0.2s ease;

  &:hover {
    background: #ffffff52;
  }
}

.accordion-title {
  flex: 1;
}

.accordion-icon {
  display: inline-block;
  transition: transform 0.3s ease;
  color: #ffffff;
  font-size: 0.9em;

  &.is-open {
    transform: rotate(180deg);
  }
}

.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;

  &.is-open {
    max-height: 2000px;
  }
}

.accordion-body {
  padding: 1.25rem;
  background: #ffffff33;
  
  :deep(p:last-child) {
    margin-bottom: 0;
  }
}
</style>
