// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: ['@nuxt/content', '@nuxt/icon', '@nuxt/eslint', '@nuxtjs/sitemap'],
    devtools: { enabled: true },
    devServer: {
        port: 5000,
    },
    compatibilityDate: '2025-07-01',
    future: {
        compatibilityVersion: 4,
    },
    app: {
        head: {
            title: 'TCC',
            meta: [
                {
                    name: 'description',
                    content: 'Tottenham Community Choir',
                },
            ],
            link: [{ rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
        },
    },
    css: ['@/assets/styles/content.scss'],
    content: {
        renderer: {
            anchorLinks: false,
        },
    },
    site: {
        url: 'https://www.tottenhamcommunitychoir.org',
    },
    vite: {
        optimizeDeps: {
            include: [],
        },
        css: {
            preprocessorOptions: {
                scss: {
                    additionalData: '@use "@/assets/styles/_variables.scss" as *;',
                },
            },
        },
    },
})
