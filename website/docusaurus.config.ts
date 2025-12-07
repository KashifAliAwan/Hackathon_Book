import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'AI-Native Textbook',
  tagline: 'Your AI-Generated Textbook on Physical AI and Humanoid Robotics',
  favicon: 'img/favicon.png',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'http://localhost:3000',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'GIAIC-PakistanZindabad', // Usually your GitHub org/user name.
  projectName: 'Hackathon_Book', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: './docs',
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
          breadcrumbs: true,
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/GIAIC-PakistanZindabad/Hackathon_Book/tree/003-ai-textbook-rag/website/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/GIAIC-PakistanZindabad/Hackathon_Book/tree/003-ai-textbook-rag/website/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'AI-Native Textbook',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: '/', label: 'Home', position: 'left' },
        { to: '/chapter-1-introduction', label: 'Textbook', position: 'left' },
        { to: '/about', label: 'About', position: 'left' },
        {
          href: 'https://github.com/GIAIC-PakistanZindabad/Hackathon_Book',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'LEARN', // Section 1 Title
          items: [
            {
              label: 'Start Your Journey',
              to: '#', // Appropriate path here
            },
            {
              label: 'Full Curriculum',
              to: '#', // Appropriate path here
            },
            {
              label: 'Learning Path',
              to: '#', // Appropriate path here
            },
          ],
        },
        {
          title: 'COMMUNITY', // Section 2 Title
          items: [
            {
              label: 'YouTube',
              href: 'https://www.linkedin.com/in/kashif-ali-awan/', // Appropriate URL here
            },
            {
              label: 'LinkedIn',
              href: 'https://www.linkedin.com/in/kashif-ali-awan/', // Appropriate URL here
            },
            {
              label: 'Instagram',
              href: 'https://www.linkedin.com/in/kashif-ali-awan/', // Appropriate URL here
            },
            {
              label: 'Facebook',
              href: 'https://www.linkedin.com/in/kashif-ali-awan/', // Appropriate URL here
            },
          ],
        },
        {
          title: 'RESOURCES', // Section 3 Title
          items: [
            {
              label: 'GitHub Repository',
              href: 'https://github.com/GIAIC-PakistanZindabad/Hackathon_Book', // Jo aap ne original code mein diya tha
            },
            {
              label: 'AI Native Specification',
              to: '#', // Appropriate path here
            },
            {
              label: 'Example Projects',
              to: '#', // Appropriate path here
            },
          ],
        },
        {
          title: 'ABOUT', // Section 4 Title
          items: [
            {
              label: 'Panaversity',
              to: '#', // Appropriate path here
            },
            {
              label: 'Our Mission',
              to: '#', // Appropriate path here
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Kashif Ali Awan • AI Native Software Development • Free & Open Source`, // Screenshot ke mutabiq
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
