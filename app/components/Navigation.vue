<template>
  <nav class="navbar">
    <div class="container">
      <NuxtLink to="/" class="logo">
        Tottenham Community Choir
      </NuxtLink>
      
      <button 
        class="menu-toggle" 
        @click="isMenuOpen = !isMenuOpen"
        :aria-expanded="isMenuOpen"
        aria-label="Toggle navigation menu"
      >
        <span class="hamburger"></span>
      </button>

      <ul class="nav-menu" :class="{ 'is-active': isMenuOpen }">
        <li><NuxtLink to="/" @click="closeMenu">Home</NuxtLink></li>
        <li><NuxtLink to="/joining-tcc" @click="closeMenu">Joining TCC</NuxtLink></li>
        <li><NuxtLink to="/about" @click="closeMenu">About Us</NuxtLink></li>
        <li><NuxtLink to="/news-and-dates" @click="closeMenu">News and Dates</NuxtLink></li>
        <li><NuxtLink to="/gallery" @click="closeMenu">Gallery</NuxtLink></li>
        <li><NuxtLink to="/how-to-find-us" @click="closeMenu">How to Find Us</NuxtLink></li>
        <li class="members-link">
          <NuxtLink to="/members-area" @click="closeMenu">Members Area</NuxtLink>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
const isMenuOpen = ref(false)

const closeMenu = () => {
  isMenuOpen.value = false
}
</script>

<style scoped>
.navbar {
  background: #5848b7;
  color: white;
  padding: 1rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
  text-decoration: none;
}

.logo:hover {
  color: #f0f0f0;
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
}

.hamburger {
  display: block;
  width: 25px;
  height: 2px;
  background: white;
  position: relative;
}

.hamburger::before,
.hamburger::after {
  content: '';
  position: absolute;
  width: 25px;
  height: 2px;
  background: white;
  left: 0;
}

.hamburger::before {
  top: -8px;
}

.hamburger::after {
  bottom: -8px;
}

.nav-menu {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
  align-items: center;
}

.nav-menu a {
  color: white;
  text-decoration: none;
  transition: opacity 0.2s;
}

.nav-menu a:hover {
  opacity: 0.8;
}

.nav-menu a.router-link-active {
  border-bottom: 2px solid white;
  padding-bottom: 0.25rem;
}

.members-link a {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.5rem 1rem;
  border-radius: 4px;
}

.members-link a:hover {
  background: rgba(255, 255, 255, 0.3);
}

@media (max-width: 768px) {
  .menu-toggle {
    display: block;
  }

  .nav-menu {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: #5848b7;
    flex-direction: column;
    padding: 1rem;
    gap: 1rem;
    display: none;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  }

  .nav-menu.is-active {
    display: flex;
  }

  .nav-menu a.router-link-active {
    border-bottom: none;
    border-left: 3px solid white;
    padding-left: 1rem;
  }
}
</style>
