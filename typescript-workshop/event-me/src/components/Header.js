import { Theme as ThemeIcon } from "@components/Icons";

const themeId = "theme";

const Header = `
<header>
    <hgroup>
        <h1 class=".parkinsans">event me</h1>
        <p>All the events you never knew you needed to attend!</p>
    </hgroup>
    <a href="#" role="toggle" id="${themeId}"  title="Toggle color scheme" >
        ${ThemeIcon} 
    </a>
</header>
<hr/>
`;

export function setupThemeToggle() {
    const toggleDarkMode = () => {
        const doc = document.documentElement;
        const currentTheme = doc.getAttribute("data-theme");
        const newTheme = currentTheme === "dark" ? "light" : "dark";
        doc.setAttribute("data-theme", newTheme);
    };
    const themeButton = document.getElementById("theme");
    if (themeButton !== null) {
        themeButton.addEventListener("click", toggleDarkMode);
    }
}

export default Header;
