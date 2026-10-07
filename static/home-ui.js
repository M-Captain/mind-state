const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
document.querySelectorAll('[data-scroll-target]').forEach((button) => {
  const track = document.getElementById(button.dataset.scrollTarget);
  const update = () => {
    const end = track.scrollWidth - track.clientWidth;
    button.disabled = Number(button.dataset.scrollDirection) < 0 ? track.scrollLeft <= 1 : track.scrollLeft >= end - 1;
  };
  button.addEventListener('click', () => track.scrollBy({ left: Number(button.dataset.scrollDirection) * (track.firstElementChild.getBoundingClientRect().width + 20), behavior: reduceMotion.matches ? 'instant' : 'smooth' }));
  track.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
});
document.querySelectorAll('.home-signup').forEach((form) => {
  let status = form.querySelector('[role="status"]');
  if (!status) { status = document.createElement('p'); status.className = 'home-signup-message'; status.setAttribute('role', 'status'); status.hidden = true; form.append(status); }
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const button = form.querySelector('[type="submit"]');
    if (button.disabled) return;
    button.disabled = true;
    status.hidden = false;
    status.textContent = 'Adding you to the list…';
    try {
      const response = await fetch(form.action, { method: 'POST', body: new FormData(form), credentials: 'same-origin' });
      const page = new DOMParser().parseFromString(await response.text(), 'text/html');
      if (!response.ok || !page.querySelector('[data-signup-confirmed]')) throw new Error('Signup was not confirmed');
      status.innerHTML = '<div class="home-signup-success"><span aria-hidden="true">✓</span><p>You’re on the list! Lovely to have you here.</p></div>';
      form.reset();
    } catch { status.textContent = 'We couldn’t confirm your signup. Please try again.'; }
    finally { button.disabled = false; }
  });
});
