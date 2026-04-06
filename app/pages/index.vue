<script setup lang="ts">
const { data: sections } = await useAsyncData('home', () => queryCollection('home').all())

const showHappy = ref(false)
const taglineVisible = ref(false)
let interval = 0
onMounted(() => {
    interval = window.setInterval(() => {
        showHappy.value = !showHappy.value
    }, 5000)
    setTimeout(() => {
        taglineVisible.value = true
    }, 300)
})
onUnmounted(() => window.clearInterval(interval))

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
        <img src="/choir-hero.webp" alt="Tottenham Community Choir" class="hero-image" />
        <img
            src="/choir-hero-happy.webp"
            alt="Tottenham Community Choir"
            class="hero-image hero-image--happy"
            :class="{ 'is-visible': showHappy }"
        />
        <div class="tagline-section">
            <span class="tagline" :class="{ 'is-visible': taglineVisible }"
                >Singing makes you feel good!</span
            >
        </div>
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

<style scoped lang="scss">
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

.hero-image--happy {
    position: absolute;
    inset: 0;
    opacity: 0;
    transition: opacity 2s ease-in-out;

    &.is-visible {
        opacity: 1;
    }
}

.tagline-section {
    position: absolute;
    bottom: 20px;
    left: 0;
    right: 0;
    padding: 2.5rem 2rem;
    text-align: center;
}

.tagline {
    display: inline-block;
    font-family: 'Playwrite IE', cursive;
    font-size: clamp(1.6rem, 4vw, 2.5rem);
    font-weight: 300;
    color: $overlay-strong;
    clip-path: inset(0% 100% -33% 0%);
    transition: clip-path 4s cubic-bezier(0.25, 0.1, 0.25, 1);
    text-shadow: 0px 0px 8px $glow-magenta;
    transform: perspective(400px) rotateX(8deg) rotate(-2deg);
    transform-origin: left center;

    &.is-visible {
        clip-path: inset(0% -10% -33% 0%);
    }
}
</style>
