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
const {
    app: { baseURL },
} = useRuntimeConfig()
useHead({
    link: [
        { rel: 'icon', type: 'image/svg+xml', href: `${baseURL}favicon.svg` },
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
* {
    box-sizing: border-box;
}

html {
    background-color: $color-primary;
}

body {
    margin: 0;
    font-family: 'Roboto Slab', Georgia, serif;
    font-weight: 300;
    background-color: $color-purple-dark-1;
    line-height: 1.6;
    color: $color-white;
}

.app {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.main-content {
    flex: 1;
    width: 100%;

    [data-content-id] {
        > * {
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }
    }
}
</style>
