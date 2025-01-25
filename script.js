document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:5000/books')
        .then(response => response.json())
        .then(data => {
            const bookList = document.getElementById('book-list');
            data.forEach(book => {
                const bookItem = document.createElement('div');
                bookItem.className = 'book';
                bookItem.innerHTML = `
                    <h3>${book.title}</h3>
                    <p>Автор: ${book.author}</p>
                    <p>Год: ${book.year}</p>
                    <p>Категория: ${book.category}</p>
                    <p>Цена: $${book.price}</p>
                `;
                bookList.appendChild(bookItem);
            });
        });
});