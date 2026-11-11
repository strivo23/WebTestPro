(() => {
  const DEMO = { name: 'Alex Morgan', email: 'alex@example.com', password: 'DemoPass123' };
  const usersKey = 'webtestpro-users';
  const users = () => JSON.parse(localStorage.getItem(usersKey) || '[]');
  const message = (form, text, success = false) => { const box = form.querySelector('.message'); box.textContent = text; box.classList.toggle('success', success); };
  const validEmail = value => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  const login = document.querySelector('#login-form');
  if (login) login.addEventListener('submit', event => {
    event.preventDefault(); const email = login.email.value.trim(); const password = login.password.value;
    if (!email || !password) return message(login, 'Please complete all required fields.');
    if (!validEmail(email)) return message(login, 'Enter a valid email address.');
    const user = [DEMO, ...users()].find(item => item.email.toLowerCase() === email.toLowerCase() && item.password === password);
    if (!user) return message(login, 'Email or password is incorrect.');
    localStorage.setItem('webtestpro-session', JSON.stringify({ name: user.name, email: user.email })); location.href = 'dashboard.html';
  });
  const register = document.querySelector('#register-form');
  if (register) register.addEventListener('submit', event => {
    event.preventDefault(); const name = register.name.value.trim(), email = register.email.value.trim(), password = register.password.value, confirm = register.confirmPassword.value;
    if (!name || !email || !password || !confirm) return message(register, 'Please complete all required fields.');
    if (!validEmail(email)) return message(register, 'Enter a valid email address.');
    if (password.length < 8) return message(register, 'Password must be at least 8 characters.');
    if (password !== confirm) return message(register, 'Passwords do not match.');
    if ([DEMO, ...users()].some(user => user.email.toLowerCase() === email.toLowerCase())) return message(register, 'An account with this email already exists.');
    const next = [...users(), { name, email, password }]; localStorage.setItem(usersKey, JSON.stringify(next));
    message(register, 'Account created successfully. You can now log in.', true); register.reset();
  });
  const session = JSON.parse(localStorage.getItem('webtestpro-session') || 'null');
  if (location.pathname.endsWith('/dashboard.html')) {
    if (!session) location.replace('login.html');
    else { document.querySelector('#welcome').textContent = `Welcome back, ${session.name.split(' ')[0]}`; document.querySelector('#profile-name').textContent = session.name; document.querySelector('#profile-email').textContent = session.email; }
  }
  document.querySelector('#logout')?.addEventListener('click', () => { localStorage.removeItem('webtestpro-session'); location.href = 'login.html'; });
})();
