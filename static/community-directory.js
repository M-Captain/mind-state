(() => {
  const page = document.querySelector('.community-directory-page');
  if (!page) return;

  const search = page.querySelector('[data-member-search]');
  const sort = page.querySelector('[data-member-sort]');
  const role = page.querySelector('[data-member-role]');
  const alphabet = page.querySelector('.community-directory-alphabet');
  const groups = page.querySelector('[data-member-groups]');
  const count = page.querySelector('[data-member-count]');
  const empty = page.querySelector('[data-member-empty]');
  let activeLetter = 'all';

  function updateDirectory() {
    const query = search.value.trim().toLocaleLowerCase();
    const selectedRole = role.value;
    const descending = sort.value === 'za';
    const sections = [...groups.querySelectorAll('[data-letter-section]')];
    // data-letter-section maps to dataset.letterSection; dataset.letter is undefined.
    sections.sort((a, b) => a.dataset.letterSection.localeCompare(b.dataset.letterSection) * (descending ? -1 : 1));

    let visibleCount = 0;
    for (const section of sections) {
      const cards = [...section.querySelectorAll('[data-member-card]')];
      cards.sort((a, b) => a.dataset.name.localeCompare(b.dataset.name) * (descending ? -1 : 1));
      const list = section.querySelector('ul');
      for (const card of cards) {
        const matchesQuery = !query || `${card.dataset.name} ${card.dataset.role}`.includes(query);
        const matchesRole = selectedRole === 'all' || card.dataset.role === selectedRole;
        const matchesLetter = activeLetter === 'all' || card.dataset.letter === activeLetter;
        card.hidden = !(matchesQuery && matchesRole && matchesLetter);
        if (!card.hidden) visibleCount += 1;
      }
      list.replaceChildren(...cards);
      section.hidden = !cards.some((card) => !card.hidden);
    }
    groups.replaceChildren(...sections);
    count.textContent = `${visibleCount} ${visibleCount === 1 ? 'member' : 'members'}`;
    empty.hidden = visibleCount !== 0;
  }

  search.addEventListener('input', updateDirectory);
  sort.addEventListener('change', updateDirectory);
  role.addEventListener('change', updateDirectory);
  alphabet.addEventListener('click', (event) => {
    const button = event.target.closest('[data-member-letter]');
    if (!button || button.disabled) return;
    activeLetter = button.dataset.memberLetter;
    for (const letterButton of alphabet.querySelectorAll('[data-member-letter]')) {
      letterButton.setAttribute('aria-pressed', String(letterButton === button));
    }
    updateDirectory();
  });

  updateDirectory();
})();
