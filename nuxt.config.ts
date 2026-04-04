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
        baseURL: '/tcc-website/',
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
        // Exclude ESM-only packages that @nuxtjs/mdc incorrectly adds to optimizeDeps.include,
        // causing unresolvable entry warnings from Vite.
        optimizeDeps: {
            exclude: [
                'remark-gfm',
                'remark-emoji',
                'remark-mdc',
                'remark-rehype',
                'rehype-raw',
                'parse5',
                'unist-util-visit',
                'unified',
                'debug',
            ],
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
