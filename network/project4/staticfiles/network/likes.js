console.log("newlikes.js is loaded");

document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed");

    document.querySelectorAll('button[id^="like_button_"]').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();  // Prevent the form submission

            const postId = this.dataset.postId;

            fetch(`/like/${postId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Make sure to get the CSRF token correctly
                },
                body: JSON.stringify({
                    post_id: postId
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);  // Check the response data

                const likeButton = document.getElementById(`like_button_${postId}`);
                likeButton.style.backgroundColor = data.like_status ? 'red' : 'black';

                document.getElementById(`like_count_${postId}`).textContent = data.new_like_count;
                likeButton.textContent = data.like_status ? "Unlike" : "Like";
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}




// console.log("likes.js is loaded");

// document.addEventListener('DOMContentLoaded', function() {
//     console.log("DOM fully loaded and parsed");

// const likeButton = document.getElementById(`like_button_${post.id}`);

// likeButton.addEventListener('click', function() {
//   fetch(`/like/${post.id}`, {  // update this with your endpoint
//       method: 'POST',
//       headers: {
//           'Content-Type': 'application/json',
//           'X-CSRFToken': csrftoken  // uncomment this line if you're using CSRF tokens
//       },
//       body: JSON.stringify({
//           post_id: {{post.id}}  // update this with your post id
//       })
//   })
//   .then(response => response.json())
//   .then(data => {
//       // update your frontend here with the response
//       // for example, if your response contains the new like count:
//       likeButton.style.background-color = data.like_status ? 'red' : 'black';

//       document.getElementById(`like_button_${post.id}`).textContent = data.new_like_count;
//       // You can also update the like button based on the like_status
//       if (data.like_status) {
//           document.getElementById(`like_button_${post.id}`).tag = "like";
//       } else {
//         document.getElementById(`like_button_${post.id}`).tag = "unlike";
//       }
//   })
//   .catch((error) => {
//       console.error('Error:', error);
//   });
// });})
