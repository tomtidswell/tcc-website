// To change the password, replace PASSWORD_HASH with the SHA-256 of the new password.
// Generate it in Node: node -e "const {subtle}=require('crypto').webcrypto,enc=new TextEncoder();subtle.digest('SHA-256',enc.encode('your-password')).then(h=>console.log(Array.from(new Uint8Array(h)).map(b=>b.toString(16).padStart(2,'0')).join('')))"
const PASSWORD_HASH = '788ca74fbc8386bf664299b040354275ae65dbcb0568aee3c552d208cdbb1549'

async function hashPassword(password: string): Promise<string> {
    const data = new TextEncoder().encode(password)
    const buffer = await crypto.subtle.digest('SHA-256', data)
    return Array.from(new Uint8Array(buffer))
        .map(b => b.toString(16).padStart(2, '0'))
        .join('')
}

export const useAuth = () => {
    const isAuthenticated = useState('auth', () => false)

    function checkSession() {
        if (import.meta.client) {
            isAuthenticated.value = sessionStorage.getItem('members-auth') === 'true'
        }
    }

    async function login(password: string): Promise<boolean> {
        const hash = await hashPassword(password)
        if (hash === PASSWORD_HASH) {
            sessionStorage.setItem('members-auth', 'true')
            isAuthenticated.value = true
            return true
        }
        return false
    }

    function logout() {
        if (import.meta.client) {
            sessionStorage.removeItem('members-auth')
        }
        isAuthenticated.value = false
    }

    return { isAuthenticated, login, logout, checkSession }
}
