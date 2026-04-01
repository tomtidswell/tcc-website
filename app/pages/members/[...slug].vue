<script setup lang="ts">
const route = useRoute()

const { data: page } = await useAsyncData(`members-${route.path}`, () => {
    return queryCollection('members').path(route.path).first()
})

if (!page.value) {
    throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
}
</script>

<template>
    <div v-if="page" class="content-section">
        <ContentRenderer :value="page" />
    </div>
</template>
