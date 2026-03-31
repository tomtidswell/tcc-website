<template>
    <div class="app">
        <Navigation />
        <main class="main-content">
            <NuxtRouteAnnouncer />
            <NuxtPage />
        </main>
        <Footer />
    </div>
</template>

<script setup>
useHead({
    link: [
        {
            rel: 'preconnect',
            href: 'https://fonts.googleapis.com',
        },
        {
            rel: 'preconnect',
            href: 'https://fonts.gstatic.com',
            crossorigin: '',
        },
        {
            rel: 'stylesheet',
            href: 'https://fonts.googleapis.com/css2?family=Jost:wght@200;300;400&family=Roboto+Slab:wght@300;400;500;600&family=Playwrite+IE:wght@300&display=swap',
        },
    ],
})
</script>

<style lang="scss">
@use '~/assets/styles/content.scss';

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: 'Roboto Slab', Georgia, serif;
    font-weight: 300;
    background-color: #8f50e2;
    line-height: 1.6;
    color: white;
}

.app {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.main-content {
    flex: 1;
    max-width: 800px;
    width: 100%;
    margin: 0 auto;
    padding: 2rem 1rem;
}
</style>
