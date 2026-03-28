<template>
  <footer class="footer">
    <div class="container">
      <p>&copy; Tottenham Community Choir 2026</p>
      <div class="social-links">
        <a href="https://en-gb.facebook.com/TottenhamCommunityChoir/" target="_blank" rel="noopener" aria-label="Facebook" title="Visit our Facebook page">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
          </svg>
          <span>Facebook</span>
        </a>
        <a href="https://www.redbubble.com/people/Tottenhamchoir/shop?asc=u" target="_blank" rel="noopener" aria-label="Merchandise shop" title="Buy choir merchandise">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="9" cy="21" r="1"></circle>
            <circle cx="20" cy="21" r="1"></circle>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
          </svg>
          <span>Online Shop</span>
        </a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: #2c2c2c;
  color: white;
  padding: 2rem 0;
  margin-top: 4rem;
}

.footer .container {
  max-width: 800px;
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
  align-items: center;
}

.social-links a {
  color: white;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: opacity 0.2s ease;
}

.social-links a:hover {
  opacity: 0.8;
}

.social-links svg {
  flex-shrink: 0;
}

@media (max-width: 768px) {
  .footer .container {
    flex-direction: column;
    text-align: center;
  }
}
</style>
