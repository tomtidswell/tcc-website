import { defineContentConfig, defineCollection, z } from '@nuxt/content'

export default defineContentConfig({
    collections: {
        events: defineCollection({
            type: 'page',
            source: 'events/**',
        }),
        home: defineCollection({
            type: 'page',
            source: 'home/**',
        }),
        members: defineCollection({
            type: 'page',
            source: 'members/**',
        }),
    },
})
