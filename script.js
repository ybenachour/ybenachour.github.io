document.documentElement.classList.add('js');
const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
menu.addEventListener('click', () => { const open = menu.getAttribute('aria-expanded') !== 'true'; menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('open', open); });
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => { menu.setAttribute('aria-expanded','false');nav.classList.remove('open'); }));
const search = document.querySelector('#publication-search');
const buttons = [...document.querySelectorAll('[data-filter]')];
const papers = [...document.querySelectorAll('.publication')];
let selected = 'All';
function filterPapers() {
  const query = search.value.trim().toLocaleLowerCase();
  let count = 0;
  papers.forEach(paper => { const visible = (selected === 'All' || paper.dataset.type === selected || paper.dataset.status === selected) && paper.textContent.toLocaleLowerCase().includes(query); paper.hidden = !visible; if (visible) count++; });
  document.querySelector('#result-count').textContent = `${count} of ${papers.length} records`;
  document.querySelector('#no-results').hidden = count !== 0;
  buttons.forEach(button => { const active = button.dataset.filter === selected; button.classList.toggle('active', active); button.setAttribute('aria-pressed', String(active)); });
}
buttons.forEach(button => button.addEventListener('click', () => { selected = button.dataset.filter; filterPapers(); }));
search.addEventListener('input', filterPapers);
document.querySelectorAll('.research-filter').forEach(link => link.addEventListener('click', () => {selected='All';search.value=link.dataset.query;filterPapers();}));
document.querySelector('#year').textContent = new Date().getFullYear();
