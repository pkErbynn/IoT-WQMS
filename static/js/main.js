/*

    This module toggles the left sidebar here and there. 

*/


const sideBarToggler = document.querySelector('#sideBarToggler');
const sidebar = document.querySelector('.sidebar');

sideBarToggler.onclick = () =>{
    sidebar.classList.toggle('visible');
};

$('.alert').alert()