<template>
  <div class="app">
    <Navigation />
    <main class="main-content">
      <NuxtRouteAnnouncer />
      <NuxtPage />
    </main>
    <footer class="footer">
      <div class="container">
        <p>&copy; Tottenham Community Choir 2015</p>
        <div class="social-links">
          <a href="https://en-gb.facebook.com/TottenhamCommunityChoir/" target="_blank" rel="noopener">Facebook</a>
          <a href="https://www.redbubble.com/people/Tottenhamchoir/shop?asc=u" target="_blank" rel="noopener">Merchandise</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  line-height: 1.6;
  color: #333;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.footer {
  background: #2c2c2c;
  color: white;
  padding: 2rem 0;
  margin-top: 4rem;
}

.footer .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.social-links {
  display: flex;
  gap: 1.5rem;
}

.social-links a {
  color: white;
  text-decoration: none;
}

.social-links a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .footer .container {
    flex-direction: column;
    text-align: center;
  }
}
</style>