<script setup lang="ts">
const { data: sections } = await useAsyncData('events-sections', () =>
    queryCollection('content').where('_path', 'LIKE', '/events/%').order('order', 'ASC').all()
)

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
    <div>
        <h1>News & Events</h1>
        <div v-if="sections" class="page-sections">
            <section v-for="section in sections" :key="section._id" class="content-section">
                <ContentRenderer :value="section" />
            </section>
        </div>
        <div v-else>
            <p>Loading...</p>
        </div>
    </div>
</template>

<style scoped>
.page-sections {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.content-section {
    width: 100%;
}
</style>
