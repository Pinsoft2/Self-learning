document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed");

    document.getElementById('add').addEventListener('click', function() {
        var wordPairDiv = document.createElement('div');
        wordPairDiv.setAttribute('id', 'newpair');
        wordPairDiv.classList.add('word-pair'); // Add a class for centering
        wordPairDiv.innerHTML = '<table><tr class="word-pair"><td>Old Word:</td><td><input type="text" name="old_word"></td></tr><tr class="word-pair"><td>New Word:</td><td><input type="text" name="new_word"></td></tr></table>';
        document.getElementById('data_table').appendChild(wordPairDiv);
    });
});