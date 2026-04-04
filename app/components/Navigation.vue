<template>
    <nav class="navbar">
        <div class="container">
            <NuxtLink to="/" class="logo">
                <img src="/favicon.svg" alt="TCC" class="logo-icon" />
            </NuxtLink>

            <button
                class="menu-toggle"
                :aria-expanded="isMenuOpen"
                aria-label="Toggle navigation menu"
                @click="isMenuOpen = !isMenuOpen"
            >
                <span class="hamburger"></span>
            </button>

            <ul class="nav-menu" :class="{ 'is-active': isMenuOpen }">
                <li><NuxtLink to="/" @click="closeMenu">Home</NuxtLink></li>
                <li><NuxtLink to="/news-and-events" @click="closeMenu">News & Events</NuxtLink></li>
                <li v-if="isAuthenticated" class="logout-link">
                    <button @click="handleLogout">Log out</button>
                </li>
                <li class="members-link">
                    <NuxtLink to="/members" @click="closeMenu">Members Area</NuxtLink>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script setup>
const isMenuOpen = ref(false)
const { isAuthenticated, logout, checkSession } = useAuth()

onMounted(() => checkSession())

const closeMenu = () => {
    isMenuOpen.value = false
}

const handleLogout = () => {
    logout()
    closeMenu()
    navigateTo('/')
}
</script>

<style scoped lang="scss">
.navbar {
    background: $color-primary;
    padding: 1rem 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    position: relative;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo-icon {
    height: 40px;
    width: auto;
    display: block;
    filter: brightness(0) invert(1);
}

.menu-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;

    &:focus-visible {
        outline: 2px solid $color-white;
        outline-offset: 2px;
        border-radius: 4px;
    }
}

.hamburger {
    display: block;
    width: 25px;
    height: 2px;
    background: $color-white;
    position: relative;
}

.hamburger::before,
.hamburger::after {
    content: '';
    position: absolute;
    width: 25px;
    height: 2px;
    background: $color-white;
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
    font-family: 'Roboto Slab', serif;
}

.nav-menu a {
    color: $color-white;
    text-decoration: none;
    transition: opacity 0.2s;
    font-weight: 600;
}

.nav-menu a:hover {
    opacity: 0.8;
}

.nav-menu a:focus-visible {
    outline: 2px solid $color-white;
    outline-offset: 2px;
    border-radius: 2px;
}

.nav-menu a.router-link-active {
    border-bottom: 2px solid $color-white;
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

.logout-link button {
    background: none;
    border: none;
    color: $color-white;
    font-family: 'Roboto Slab', serif;
    font-size: inherit;
    font-weight: 600;
    cursor: pointer;
    padding: 0;
    opacity: 1;
    transition: opacity 0.2s;

    &:hover {
        opacity: 0.7;
    }
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
        background: $color-primary;
        flex-direction: column;
        align-items: flex-end;
        padding: 1rem;
        gap: 1rem;
        display: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 100;
    }

    .nav-menu.is-active {
        display: flex;
    }

    .nav-menu a.router-link-active {
        border-bottom: none;
        border-left: 3px solid $color-white;
        padding-left: 1rem;
    }
}
</style>
