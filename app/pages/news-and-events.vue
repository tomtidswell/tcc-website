<script setup lang="ts">
const { data: sections } = await useAsyncData('events', () => queryCollection('events').all())

useHead({
    title: 'News & Events - Tottenham Community Choir',
    meta: [
        {
            name: 'description',
            content: 'Upcoming events, past performances, photos, and how to find us',
        },
    ],
})
</script>

<template>
    <template v-if="sections?.length">
        <section v-for="section in sections" :key="section.id" class="content-section">
            <ContentRenderer :value="section" />
        </section>
    </template>
    <div v-else>
        <p>Loading...</p>
    </div>
</template>
