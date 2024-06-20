document.addEventListener('DOMContentLoaded', function() {

// on cliking like_button, post api call runs to add liked_by user to the post
const username = "{{ user.username }}";

  // Get the CSRF token from the cookie
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
// load main screen
fetch('/')
      .then(response => {
        console.log('Response from the server:', response);
        return response.json();
      })
      .then(posts => {
// loop against each post
        posts.forEach(post =>{
          const likeButton = document.querySelector(`#like_button_${post.id}`);
          const likeCountElement = document.querySelector(`#like_count_${post.id}`);
          // set color based on status
          likeButton.style.color = post.liked ? 'red' : 'black';

          likeButton.addEventListener('click', () => {
            const csrftoken = getCookie('csrftoken');
            fetch(`/like/${post.id}/`, {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
              },
              body: JSON.stringify({
                username: username,
              }),
            })
              .then(response => response.json())
              .then(data => {
                // Update the like button color and like count
                likeButton.style.color = data.liked ? 'red' : 'black';
                likeCountElement.textContent = data.likes_count;
              })})
        })})})





