<template>
    <div class="alert" :class="color">
        <Icon name="lucide:alert-circle" class="alert-icon" />
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
        :deep(svg) {
            width: 20px;
            height: 20px;
        }
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
