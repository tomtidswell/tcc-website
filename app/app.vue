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

<style lang="scss">
@import '~/assets/styles/content.scss';

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background-color: #8f50e2;
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