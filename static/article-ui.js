document.querySelectorAll('.article__frame-82 button').forEach((button) => {
  button.addEventListener('click', () => {
    document.querySelector('#article-reading')?.scrollIntoView({
      behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
    });
  });
});
