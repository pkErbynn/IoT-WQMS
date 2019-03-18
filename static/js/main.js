const sideBarToggler = document.querySelector('#sideBarToggler');
const sidebar = document.querySelector('.sidebar');

sideBarToggler.onclick = () =>{
    sidebar.classList.toggle('visible');
};