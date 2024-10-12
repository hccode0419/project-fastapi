document.getElementById('item-form').addEventListener('submit', async function (event) {
    event.preventDefault(); // 폼이 제출될 때 페이지가 새로고침되지 않도록 막음

    // 입력된 폼 데이터 가져오기
    const itemId = document.getElementById('item_id').value;
    const itemName = document.getElementById('item_name').value;
    const itemPrice = document.getElementById('item_price').value;

    // FastAPI로 POST 요청 보내기
    try {
        const response = await fetch(`http://127.0.0.1:8000/item/create_item`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }         
            ,
            body: JSON.stringify({
                item_id: parseInt(itemId),
                item_name: itemName,
                item_price: parseInt(itemPrice),
            }),
        });

        const result = await response.json();
        
        // 결과를 화면에 출력
        if (response.ok) {
            document.getElementById('result').textContent = '상품이 성공적으로 등록되었습니다.';
        } else {
            document.getElementById('result').textContent = `에러: ${result["error message"]}`;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').textContent = '상품 등록 중 오류가 발생했습니다.';
    }
});
