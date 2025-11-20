import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Dployr SDK",
  description: "SDK client for interacting with dployr daemon via HTTP requests",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Python', link: '/python' },
      { text: 'TypeScript', link: '/typescript' },
      { text: 'Shapes', link: '/reference' },
    ],

    sidebar: [
      {
        text: 'SDK Clients',
        items: [
          { text: 'Python', link: '/python' },
          { text: 'TypeScript', link: '/typescript' }
        ]
      },
      {
        text: 'Reference',
        items: [
          { text: 'Request & response shapes', link: '/reference' }
        ]
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/dployr-io/dployr-sdk' }
    ]
  }
})
