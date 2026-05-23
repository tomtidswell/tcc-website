// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: ['@nuxt/content', '@nuxt/icon', '@nuxt/eslint', '@nuxtjs/sitemap'],
    devtools: { enabled: true },
    devServer: {
        port: 3000,
    },
    compatibilityDate: '2025-07-01',
    future: {
        compatibilityVersion: 4,
    },
    app: {
        // baseURL: '/tcc-website/',
        head: {
            title: 'TCC',
            meta: [
                {
                    name: 'description',
                    content: 'Tottenham Community Choir',
                },
            ],
            link: [],
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
    sitemap: {
        exclude: ['/members', '/members/**'],
    },
    vite: {
        build: {
            modulePreload: { polyfill: false },
        },
        // Override @nuxtjs/mdc's optimizeDeps.include entries which are ESM-only
        // and cannot be pre-bundled by Vite.
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
