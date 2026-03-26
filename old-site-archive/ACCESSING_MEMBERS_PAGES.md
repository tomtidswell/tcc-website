# Accessing Password-Protected Pages

**Site:** https://www.tottenhamcommunitychoir.org/  
**Members Area Password:** Copland0!  
**Authentication System:** Weebly built-in password protection

---

## Authentication Flow

The members-only pages use a cookie-based authentication system. To access them programmatically:

### Step 1: Get Session Cookies

First, request a protected page to receive session cookies:

```bash
curl -i 'https://www.tottenhamcommunitychoir.org/repertoire.html' \
  --head --silent | grep -i 'set-cookie'
```

### Step 2: Authenticate

POST the password to the login endpoint with the session cookies:

```bash
curl -X POST 'https://www.tottenhamcommunitychoir.org/401/login.php' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: [session-cookie-from-step-1]' \
  -d 'p=Copland0!&redirect=/repertoire.html&u=weebs' \
  --include
```

### Step 3: Access Protected Content

Use both the session cookie and the login cookie (`WeeblySiteLogin`) from the authentication response to access any members page.

---

## Node.js Implementation

Complete example using the fetch API:

```javascript
async function fetchProtectedPage(pageUrl) {
  // 1. Get session cookies
  const sessionResponse = await fetch(pageUrl, { redirect: 'manual' });
  const sessionCookies = sessionResponse.headers.get('set-cookie');

  // 2. Login
  const loginResponse = await fetch('https://www.tottenhamcommunitychoir.org/401/login.php', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': sessionCookies
    },
    body: new URLSearchParams({
      p: 'Copland0!',
      redirect: '/' + new URL(pageUrl).pathname.split('/').pop(),
      u: 'weebs'
    }),
    redirect: 'manual'
  });

  // 3. Get login cookies and redirect URL
  const loginCookies = loginResponse.headers.get('set-cookie');
  const redirectUrl = loginResponse.headers.get('location');

  if (!redirectUrl || !loginCookies.includes('WeeblySiteLogin')) {
    throw new Error('Authentication failed');
  }

  // 4. Access the protected page
  const finalResponse = await fetch(redirectUrl, {
    headers: { 'Cookie': [sessionCookies, loginCookies].join('; ') }
  });
  
  return await finalResponse.text();
}

// Usage
const html = await fetchProtectedPage('https://www.tottenhamcommunitychoir.org/repertoire.html');
console.log(html);
```

---

## Technical Details

| Property | Value |
|----------|-------|
| **Login Endpoint** | `https://www.tottenhamcommunitychoir.org/401/login.php` |
| **Password** | `Copland0!` |
| **Login Cookie Name** | `WeeblySiteLogin` |
| **Session Duration** | Browser session (until cookies expire) |
| **Platform** | Weebly's built-in password protection |

### POST Parameters

When authenticating, send these form parameters:

- `p` - The password (`Copland0!`)
- `redirect` - The page to redirect to after login (e.g., `/repertoire.html`)
- `u` - Static value: `weebs`

### Response

Successful authentication returns:
- HTTP 302 redirect
- `Location` header pointing to the requested page
- `Set-Cookie` header with `WeeblySiteLogin` cookie

---

## Protected Pages

All pages in the `members-only/` directory require this authentication:

1. members-area.html
2. repertoire.html
3. comments-and-chat.html
4. contact.html
5. dress-code.html
6. feedback.html
7. members-gallery.html
8. serving-refreshments.html
9. video-gallery.html

---

## Reference

This authentication approach was adapted from:
- https://github.com/jameshfisher/tcc-repertoire/blob/main/scripts/fetch-repertoire.ts
