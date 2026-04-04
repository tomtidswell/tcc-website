<template>
    <footer class="footer">
        <div class="container">
            <div class="footer-section">
                <h4>Rehearsals</h4>
                <p>Every Tuesday</p>
                <p>7:30pm – 9:30pm</p>
            </div>
            <div class="footer-section">
                <h4>Venue</h4>
                <address>
                    <p>Chestnuts Community Centre</p>
                    <p>280 St Ann's Rd</p>
                    <p>London, N15 5BN</p>
                </address>
                <a
                    href="https://www.google.com/maps?q=51.5817834,-0.0886562"
                    target="_blank"
                    rel="noopener"
                    aria-label="View on Google Maps"
                    >View on Google Maps</a
                >
            </div>
            <div class="footer-section">
                <h4>Find Us</h4>
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
                        href="mailto:comms@tottenhamcommunitychoir.org"
                        aria-label="Email us"
                        title="Contact us by email"
                    >
                        <Icon name="lucide:mail" />
                        <span>Comms</span>
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
        </div>
        <div class="footer-bottom">
            <p>&copy; Tottenham Community Choir 2026</p>
        </div>
    </footer>
</template>

<style scoped lang="scss">
.footer {
    background: $color-footer;
    color: $color-white;
    font-family: 'Roboto Slab', serif;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem 2rem 1rem;
    display: flex;
    justify-content: space-between;
    gap: 2rem;
    flex-wrap: wrap;
}

.footer-section {
    h4 {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: $color-white;
        margin: 0 0 0.75rem;
    }

    p,
    address {
        font-size: 0.9rem;
        color: $color-muted-dark;
        margin: 0;
        font-style: normal;
        line-height: 1.8;
    }

    a {
        font-size: 0.85rem;
        color: $color-muted-dark;
        text-decoration: none;
        transition: color 0.2s ease;

        &:hover {
            color: $color-white;
        }

        &:focus-visible {
            outline: 2px solid $color-white;
            outline-offset: 2px;
            border-radius: 2px;
        }
    }
}

.social-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;

    a {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
}

.footer-bottom {
    border-top: 1px solid rgba($color-white, 0.1);
    text-align: center;
    padding: 1rem 2rem;

    p {
        margin: 0;
        font-size: 0.8rem;
        color: $color-muted-darker;
    }
}

@media (max-width: 600px) {
    .container {
        flex-direction: column;
        gap: 1.5rem;
    }
}
</style>
