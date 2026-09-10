window.onload = function() {
  const docsLinks = [].slice.call(window.document.getElementsByClassName('md-nav__link'));
  const apiLink = docsLinks.find(x => x.href === 'https://api-docs.scarf.sh/v2.html');
  if (apiLink) {
    apiLink.setAttribute('target', '_blank');
  }
};