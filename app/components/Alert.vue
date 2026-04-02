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
    padding: 6px 8px;
    gap: 12px;
    border-left: 2px solid;

    .alert-icon {
        flex-shrink: 0;
        width: 20px;
        height: 20px;
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
