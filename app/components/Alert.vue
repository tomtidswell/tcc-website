<template>
    <div class="alert" :class="color">
        <svg
            class="alert-icon"
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="20"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
        >
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="8" x2="12" y2="12"></line>
            <line x1="12" y1="16" x2="12.01" y2="16"></line>
        </svg>
        <div class="alert-content">
            <slot></slot>
        </div>
    </div>
</template>

<script setup lang="ts">
const { color } = defineProps({
    color: {
        type: String,
        default: 'orange',
    },
})
</script>

<style scoped lang="scss">
.alert {
    display: inline-flex;
    align-items: center;
    padding: 12px 16px;
    gap: 0.75rem;
    padding: 6px 8px;
    border-left: 2px solid;
    // border-right: 2px solid;
    // border-radius: 0.5rem;

    .alert-icon {
        flex-shrink: 0;
    }

    .alert-content {
        flex: 1;
        :deep(> p) {
            display: inline;
            margin: 0;
        }
    }

    &.orange {
        border-color: $alert-orange-border;
    }

    &.red {
        border-color: $alert-red-border;
    }
}
</style>
