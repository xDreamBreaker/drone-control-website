document.getElementById('takeoff').addEventListener('click', function() {
    console.log('Дрон взлетает');
    // Здесь вы можете добавить вызовы к API или другие действия
});

document.getElementById('land').addEventListener('click', function() {
    console.log('Дрон приземляется');
});

document.getElementById('move-forward').addEventListener('click', function() {
    console.log('Дрон летит вперед');
});

document.getElementById('move-backward').addEventListener('click', function() {
    console.log('Дрон летит назад');
});

document.getElementById('turn-left').addEventListener('click', function() {
    console.log('Дрон поворачивает налево');
});

document.getElementById('turn-right').addEventListener('click', function() {
    console.log('Дрон поворачивает направо');
});
