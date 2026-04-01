<template>
    <footer class="footer">
        <div class="container">
            <p>&copy; Tottenham Community Choir 2026</p>
            <div class="social-links">
                <a
                    href="https://en-gb.facebook.com/TottenhamCommunityChoir/"
                    target="_blank"
                    rel="noopener"
                    aria-label="Facebook"
                    title="Visit our Facebook page"
                >
                    <Icon name="lucide:facebook" />
                    <span>Facebook</span>
                </a>
                <a
                    href="https://www.redbubble.com/people/Tottenhamchoir/shop?asc=u"
                    target="_blank"
                    rel="noopener"
                    aria-label="Merchandise shop"
                    title="Buy choir merchandise"
                >
                    <Icon name="lucide:shopping-cart" />
                    <span>Online Shop</span>
                </a>
            </div>
        </div>
    </footer>
</template>

<style scoped>
.footer {
    background: #2c2c2c;
    color: white;
    padding: 2rem 0;
    font-family: 'Roboto Slab', serif;
}

.footer .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
}

.footer p {
    margin: 0;
    font-size: 0.9rem;
    color: #aaa;
}

.social-links {
    display: flex;
    gap: 1.5rem;
    align-items: center;
}

.social-links a {
    color: white;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: opacity 0.2s ease;
}

.social-links a:hover {
    opacity: 0.8;
}

.social-links :deep(svg) {
    flex-shrink: 0;
    width: 24px;
    height: 24px;
}

@media (max-width: 768px) {
    .footer .container {
        flex-direction: column;
        text-align: center;
    }
}
</style>
