import './style.css'
import Header, { setupThemeToggle } from './components/Header.js';
import Main from './components/Main.js';
import Footer from './components/Footer.js';
import { setupModals } from './components/Modal.js';
import { setupForms } from './components/Forms.js';

const { VITE_API_URL } = import.meta.env;
if (!VITE_API_URL) throw new Error('Missing env var VITE_API_URL');

const render = (html) => {
  console.log('rendering');
  document.querySelector('#app').innerHTML = html;
  setupThemeToggle();
  setupModals();
  setupForms();
};


render(`
  ${Header}
  ${Main}
  ${Footer}
`);



