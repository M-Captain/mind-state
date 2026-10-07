// Frontend equivalents of the supplied optional React callbacks. No network requests.
document.querySelectorAll('.mindstate-community-footer').forEach((component) => {
  component.querySelectorAll('[data-community-action]').forEach((button) => {
    button.addEventListener('click', () => {
      component.dispatchEvent(new CustomEvent('mindstate:action', {
        bubbles: true, detail: { action: button.dataset.communityAction }
      }));
    });
  });
  component.querySelector('.footer-subscribe').addEventListener('submit', (event) => {
    event.preventDefault();
    component.querySelector('.subscribe-status').textContent = 'Newsletter signup is not connected yet.';
  });
});
