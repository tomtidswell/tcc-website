<script setup lang="ts">
const { data: sections } = await useAsyncData('home-sections', () =>
    queryCollection('content').where('_path', 'LIKE', '/home/%').order('order', 'ASC').all()
)

useHead({
    title: 'Home - Tottenham Community Choir',
    meta: [
        {
            name: 'description',
            content: 'Tottenham Community Choir - Singing Makes You Feel Good!',
        },
    ],
})
</script>

<template>
    <div class="page-sections">
        <section v-for="section in sections" :key="section._id" class="content-section">
            <ContentRenderer :value="section" />
        </section>
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
