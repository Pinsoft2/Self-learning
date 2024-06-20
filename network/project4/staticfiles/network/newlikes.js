console.log("newlikes.js is loaded");

document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed");
    document.querySelectorAll('button[id^="like_button_"]').forEach(button => {
        button.addEventListener('click', function() {
            console.log("clicked!")
            let postId = this.id.split('_')[2];
            let userId = this.dataset.userId;
            let likeCountElement = document.querySelector("#like_count_" + postId);
            let likeButton = this;

            fetch('/like/' + postId + '/', {
                method: 'POST',
                body: JSON.stringify({
                    'user_id': userId
                }),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('input[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.like_status) {
                    likeButton.style.backgroundColor = 'grey';
                    likeCountElement.textContent = parseInt(likeCountElement.textContent) + 1;
                } else {
                    likeButton.style.backgroundColor = 'red';
                    likeCountElement.textContent = parseInt(likeCountElement.textContent) - 1;
                }
            });
        });
    });
});
