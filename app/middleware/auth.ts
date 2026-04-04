export default defineNuxtRouteMiddleware(() => {
    if (import.meta.server) return

    const { isAuthenticated, checkSession } = useAuth()
    checkSession()

    if (!isAuthenticated.value) {
        return navigateTo('/members/login')
    }
})
