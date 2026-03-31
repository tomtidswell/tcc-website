// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    modules: ['@nuxt/content', '@nuxt/icon'],
    devtools: { enabled: true },
    compatibilityDate: '2024-04-03',
    content: {
        renderer: {
            anchorLinks: false,
        },
    },
    vite: {
        css: {
            preprocessorOptions: {
                scss: {
                    additionalData: '@use "~/assets/styles/_variables.scss" as *;',
                },
            },
        },
    },
})
