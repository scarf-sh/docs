window.onload = function() {
  const sideBar = window.document.getElementsByClassName('md-sidebar--secondary').item(0);
  if (sideBar) {
    sideBar.style.display = 'none';
  }
};