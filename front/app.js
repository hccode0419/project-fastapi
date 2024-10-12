// FastAPI로부터 상품 목록을 가져와서 HTML에 추가하는 함수
async function fetchItems(skip = 0, limit = 10) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/item/get_items`, {
            method: 'GET'  // 명시적으로 GET 메서드를 사용
        });
        const items = await response.json();

        // 상품 리스트가 들어갈 요소
        const productList = document.getElementById('product-list');

        // 받은 데이터를 기반으로 상품 요소 생성
        items.forEach(item => {
            console.log(item);
            const productItem = document.createElement('div');
            productItem.classList.add('product-item');

            const productImage = document.createElement('div');
            productImage.classList.add('product-image');
            productImage.style.backgroundColor = '#f0f0f0'; // 기본 이미지 배경
            if (item.image) {
                productImage.style.backgroundImage = `url(${item.image})`;
            }

            const productName = document.createElement('div');
            productName.classList.add('product-name');
            productName.textContent = item.item_name;

            const productPrice = document.createElement('div');
            productPrice.classList.add('product-price');
            productPrice.textContent = `${item.item_price}원`;

            // 생성한 요소들을 productItem에 추가
            productItem.appendChild(productImage);
            productItem.appendChild(productName);
            productItem.appendChild(productPrice);

            // productList에 추가
            productList.appendChild(productItem);
        });
    } catch (error) {
        console.error('Failed to fetch items:', error);
    }
}

// 페이지가 로드되면 상품 목록을 가져옴
document.addEventListener('DOMContentLoaded', () => {
    fetchItems();
});
