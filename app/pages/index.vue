<script setup lang="ts">
const { data: sections } = await useAsyncData('home', () => queryCollection('home').all())

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
    <div class="hero-container">
        <img src="/choir-hero.jpg" alt="Tottenham Community Choir" class="hero-image" />
    </div>
    <template v-if="sections?.length">
        <section v-for="section in sections" :key="section.id" class="content-section">
            <ContentRenderer :value="section" />
        </section>
    </template>
    <div v-else>
        <p>Loading...</p>
    </div>
</template>

<style scoped>
.hero-container {
    width: 100%;
    height: 60vh;
    min-height: 400px;
    max-height: 600px;
    overflow: hidden;
    position: relative;
}

.hero-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
}
</style>
