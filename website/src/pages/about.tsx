import React from 'react';
import Layout from '@theme/Layout';

export default function About(): JSX.Element {
  return (
    <Layout title="About" description="About Kashif Ali Awan">
      <main style={{ padding: '2rem', maxWidth: '900px', margin: 'auto' }}>
        <h1>About Me</h1>

        <p>
          Hi! I'm <strong>Kashif Ali Awan</strong>, a passionate{" "}
          <strong>React.js & Next.js Developer</strong>,{" "}
          <strong>Agentic AI Engineering Trainee</strong>, and{" "}
          <strong>WordPress & Shopify Developer</strong> from Karachi, Pakistan.
        </p>

        <p>
          I am currently pursuing a <strong>Bachelor of Science in Computer Science (BSCS)</strong> and
          training in <strong>Agentic AI Software Engineering</strong> at GIAIC, along with{" "}
          <strong>Modern Web & Mobile App Development</strong> at SMIT.
        </p>

        <h2>Career Summary</h2>
        <p>
          I am working as an <strong>IT Project Executive at Techxem LLC</strong>, where I manage and
          deliver web projects for multiple companies. My experience includes building WordPress
          and Shopify stores, managing e-commerce products, creating digital designs, and handling marketing campaigns.
        </p>

        <h2>Skills & Technologies</h2>
        <ul>
          <li>React.js, Next.js, TypeScript</li>
          <li>Python & AI Tools</li>
          <li>Agentic AI Engineering (In Progress)</li>
          <li>WordPress & Shopify Development</li>
          <li>UI/UX & Product Design</li>
          <li>Digital Marketing</li>
          <li>Excel Reporting & Data Handling</li>
        </ul>

        <h2>Key Projects</h2>
        <ul>
          <li><strong>Luxzio Sports Wear:</strong> Shopify store, AI-based apparel designs & branding</li>
          <li><strong>American Safety Wear:</strong> WordPress website, content & design</li>
          <li><strong>Used Medical Equipment:</strong> Product management & marketing</li>
          <li><strong>New York Precious Metals:</strong> Website optimization & branding</li>
          <li><strong>Used Computer Lots:</strong> Inventory & website management</li>
        </ul>

        <h2>Contact & Profile</h2>
        <p>
          Email: <a href="mailto:kashifalismitofficial@gmail.com">kashifalismitofficial@gmail.com</a>
        </p>
        <p>
          Location: Karachi, Pakistan
        </p>
        <p>
          LinkedIn:{" "}
          <a href="https://www.linkedin.com/in/kashif-ali-awan/" target="_blank" rel="noreferrer">
            linkedin.com/in/kashif-ali-awan
          </a>
        </p>

        <h2>Languages</h2>
        <p>Urdu (Native), Hindko (Fluent), English (Intermediate)</p>
      </main>
    </Layout>
  );
}
