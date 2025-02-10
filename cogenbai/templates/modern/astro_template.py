class AstroTemplate:
    @staticmethod
    def generate_page() -> str:
        return '''---
import Layout from '../layouts/Layout.astro';
import Card from '../components/Card.astro';

const title = "Welcome to Astro";
---

<Layout title={title}>
    <main>
        <h1>{title}</h1>
        <Card
            href="https://docs.astro.build/"
            title="Documentation"
            body="Learn how Astro works and explore the official API docs."
        />
    </main>
</Layout>

<style>
    main {
        margin: auto;
        padding: 1rem;
        width: 800px;
        max-width: calc(100% - 2rem);
        font-size: 20px;
        line-height: 1.6;
    }
</style>
'''

    @staticmethod
    def generate_component() -> str:
        return '''---
interface Props {
    title: string;
    body: string;
    href: string;
}

const { href, title, body } = Astro.props;
---

<div class="card">
    <a href={href}>
        <h2>
            {title}
            <span>&rarr;</span>
        </h2>
        <p>
            {body}
        </p>
    </a>
</div>

<style>
    .card {
        padding: 1rem;
        background-color: #fff;
        border-radius: 0.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
</style>
'''
