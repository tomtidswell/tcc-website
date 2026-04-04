<script setup lang="ts">
const { isAuthenticated, login, checkSession } = useAuth()
const password = ref('')
const error = ref('')
const loading = ref(false)

onMounted(() => {
    checkSession()
    if (isAuthenticated.value) {
        navigateTo('/members')
    }
})

async function handleSubmit() {
    error.value = ''
    loading.value = true
    const success = await login(password.value)
    loading.value = false
    if (success) {
        await navigateTo('/members')
    } else {
        error.value = 'Incorrect password. Please try again.'
        password.value = ''
    }
}
</script>

<template>
    <div class="login-section">
        <div class="login-card">
            <h1>Members Area</h1>
            <p>Enter the password to access the members area.</p>
            <form @submit.prevent="handleSubmit">
                <div class="field">
                    <label for="password">Password</label>
                    <input
                        id="password"
                        v-model="password"
                        type="password"
                        autocomplete="current-password"
                        required
                    />
                </div>
                <p v-if="error" class="error">{{ error }}</p>
                <button type="submit" :disabled="loading">
                    {{ loading ? 'Checking…' : 'Sign in' }}
                </button>
            </form>
        </div>
    </div>
</template>

<style scoped lang="scss">
.login-section {
    background-color: $color-purple-dark-2;
    min-height: calc(100vh - 70px);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
}

.login-card {
    background-color: $color-purple-dark-1;
    border-radius: 8px;
    padding: 2.5rem;
    width: 100%;
    max-width: 400px;
    color: $color-white;

    h1 {
        font-family: 'Jost', sans-serif;
        font-size: 2rem;
        font-weight: 200;
        margin: 0 0 0.5rem;
    }

    p {
        color: $color-muted-dark;
        margin-bottom: 2rem;
        font-size: 0.95rem;
    }
}

.field {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    margin-bottom: 1rem;

    label {
        font-size: 0.875rem;
        color: $color-muted-dark;
    }

    input {
        background: $color-purple-dark-2;
        border: 1px solid $overlay-medium;
        border-radius: 4px;
        padding: 0.75rem 1rem;
        color: $color-white;
        font-size: 1rem;
        outline: none;
        transition: border-color 0.2s;

        &:focus {
            border-color: $color-primary;
        }
    }
}

.error {
    color: $alert-red-border;
    font-size: 0.875rem;
    margin: 0 0 1rem;
}

button[type='submit'] {
    width: 100%;
    background: $color-primary;
    color: $color-white;
    border: none;
    border-radius: 4px;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-family: 'Roboto Slab', serif;
    cursor: pointer;
    transition: opacity 0.2s;

    &:hover:not(:disabled) {
        opacity: 0.85;
    }

    &:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }
}
</style>
