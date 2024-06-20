
document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between viewsmail2/mail/static/mail/inbox.js mail2/mail/templates/mail/inbox.html
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});


function load_mailbox(mailbox) {

  document.querySelector('#emails-view').innerHTML = '';
  document.querySelector('#email-detail-view').innerHTML= '';

  // Show the mailbox and hide other views

  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-detail-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;


  // Default view
  fetch(`/emails/${mailbox}`)
      .then(response => response.json())
      .then(emails => {
          // Print emails
          var email_summary = document.createElement('table');
          email_summary.setAttribute('id', 'emailList')
          document.querySelector('#emails-view').append(email_summary)

          var title = document.createElement('tr');
          title.style.backgroundColor = "#FFE7EE"
          title.innerHTML = `<th>Subject</th> <th>sender</th> <th>Time</th> `;
          document.querySelector('#emailList').append(title);

          emails.forEach(email => {
            console.log(email);
            var each_email = document.createElement('tr');
            each_email.setAttribute('id', 'eachEmail');
            each_email.style.cursor="pointer";
            each_email.innerHTML = `<th>${email.subject}</th>
            <th>${email.sender}</th>
            <th>${email.timestamp}</th>`;
            document.querySelector('#emailList').append(each_email);
            //read detail
            each_email.onclick =() =>{
              fetch(`/emails/${email.id}`)
              .then(response => response.json())
              .then(email => {
                  // Print email
                  var email_detail = document.createElement('table')
                  email_detail.setAttribute('id', 'defaultEmailDetail')
                  email_detail.innerHTML = `
                  <tr><th colspan="2">Subject: ${email.subject}</th></tr>
                  <tr>
                  <td>Sender: ${email.sender} </td>
                  <td>Sent on: ${email.timestamp} </td>
                  </tr>
                  <tr><td colspan="2"><div id="email_body" >${email.body}</div></td></tr>`
                  // email_detail.style.backgroundColor = "lightpink";
                  document.querySelector('#email-detail-view').append(email_detail);
                  //hide other divs, expose new div with subject and body
                      document.querySelector('#email-detail-view').style.display = 'block';
                      document.querySelector('#emails-view').style.display = 'none';
                      document.querySelector('#compose-view').style.display = 'none';

                    //mark read
                    fetch(`/emails/${email.id}`, {
                      method: 'PUT',
                      body: JSON.stringify({
                          read: true
                      })
                    })
                    //add archive button
                    var archive_button = document.createElement('button');
                        archive_button.setAttribute('id', 'archiveButton');
                          if (email.archived === true) {
                            archive_button.textContent = `Unarchive`;
                            document.querySelector('#email-detail-view').append(archive_button);
                            archive_button.onclick = () => {
                              fetch(`/emails/${email.id}`, {
                                  method: 'PUT',
                                  body: JSON.stringify({
                                      archived: false
                                  })
                              })
                              setTimeout(() => {
                                load_mailbox('inbox');
                              }, 300);
                            }}
                          else if (email.archived === false) {
                            archive_button.innerHTML  = `Archive`; // Update button text
                            document.querySelector('#email-detail-view').append(archive_button);
                            archive_button.onclick = () => {
                              fetch(`/emails/${email.id}`, {
                                  method: 'PUT',
                                  body: JSON.stringify({
                                      archived: true
                                  })
                              })
                              setTimeout(() => {
                                load_mailbox('inbox');
                              }, 300);
                            }}

                            //add reply button
                    var reply_button = document.createElement('button');
                    reply_button.setAttribute('id', 'replyButton');
                    reply_button.innerHTML = `Reply`;
                    document.querySelector('#email-detail-view').append(reply_button);
                    reply_button.onclick = () => {
                      compose_email();
                      document.querySelector('#compose-recipients').value = email.sender;
                      document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
                      document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote:\n\n"${email.body}"`;
                    };
                    }
                  )}
          });

      })
      .catch(error => {
        console.error('Error:', error);
      })


  // inbox specific view
      document.querySelector('#inbox').onclick= () =>{
      fetch(`/emails/${mailbox}`)
      .then(response => response.json())
      .then(emails => {
          // Print emails
          var email_summary = document.createElement('table');
          email_summary.setAttribute('id', 'emailList2')
          document.querySelector('#emails-view').append(email_summary)

          var title = document.createElement('tr');
          title.style.backgroundColor = "#FFE7EE"
          title.innerHTML = `<th>Subject</th> <th>sender</th> <th>Time</th> <th>Read?</th>`;

          document.querySelector('#emailList2').append(title);
          document.querySelector('#emailList').style.display = 'none';

          emails.forEach(email => {
            var each_email = document.createElement('tr');
            each_email.setAttribute('id', 'eachEmail')
            each_email.style.cursor="pointer";
            each_email.innerHTML = `<th>${email.subject}</th> <th>${email.sender}</th> <th>${email.timestamp}</th> <th>${email.read}</th>`;

            if (email.read == "true"){
              each_email.style.backgroundColor = "lightgrey";
            }
            else {each_email.style.backgroundColor = "white";
            each_email.style.fontWeight = "bold";
           }
           document.querySelector('#emailList2').append(each_email);
           //here we do load individual emails
           each_email.onclick =() =>{
            fetch(`/emails/${email.id}`)
            .then(response => response.json())
            .then(email => {
                // Print email
                var email_detail = document.createElement('table')
                email_detail.innerHTML = `
                <tr><th colspan="2">Subject: ${email.subject}</th></tr>
                <tr>
                <td>Sender: ${email.sender} </td>
                <td>Sent on: ${email.timestamp} </td>
                </tr>
                <tr><td colspan="2"><div id="email_body" >${email.body}</div></td></tr>`
                // email_detail.style.backgroundColor = "lightpink";
                document.querySelector('#email-detail-view').append(email_detail);
                //hide other divs, expose new div with subject and body
                    document.querySelector('#email-detail-view').style.display = 'block';
                    // document.querySelector('#defaultEmailDetail').style.display = 'none';
                    document.querySelector('#emails-view').style.display = 'none';
                    document.querySelector('#compose-view').style.display = 'none';

                //mark read if unread
                if (email.read =="false"){
                    fetch(`/emails/${email.id}`, {
                      method: 'PUT',
                      body: JSON.stringify({
                          read: true
                      })
                    })}

                //add archive button


                var archive_button = document.createElement('button');
                archive_button.setAttribute('id', 'archiveButton');
                  if (email.archived === true) {
                    archive_button.textContent = `Unarchive`;
                    document.querySelector('#email-detail-view').append(archive_button);
                    archive_button.onclick = () => {
                      fetch(`/emails/${email.id}`, {
                          method: 'PUT',
                          body: JSON.stringify({
                              archived: false
                          })
                      })
                      setTimeout(() => {
                        load_mailbox('inbox');
                      }, 300);
                    }}
                  else if (email.archived === false) {
                    archive_button.innerHTML  = `Archive`; // Update button text
                    document.querySelector('#email-detail-view').append(archive_button);
                    archive_button.onclick = () => {
                      fetch(`/emails/${email.id}`, {
                          method: 'PUT',
                          body: JSON.stringify({
                              archived: true
                          })
                      })
                      setTimeout(() => {
                        load_mailbox('inbox');
                      }, 300);
                    }}


                  //add reply button
                  var reply_button = document.createElement('button');
                  reply_button.setAttribute('id', 'replyButton');
                  reply_button.innerHTML = `Reply`;
                  document.querySelector('#email-detail-view').append(reply_button);
                  reply_button.onclick = () => {
                    compose_email();
                    document.querySelector('#compose-recipients').value = email.sender;
                    document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
                    document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote:\n\n"${email.body}"`;
                  };
                })}
          })
        })
      }


  // sent box specific view
    document.querySelector('#sent').onclick= () =>{

      fetch(`/emails/${mailbox}`)
      .then(response => response.json())
      .then(emails => {
          // Print emails
          var email_summary = document.createElement('table');
          email_summary.setAttribute('id', 'sentList')
          document.querySelector('#emails-view').append(email_summary)
          var title = document.createElement('tr');
          title.style.backgroundColor = "#FFE7EE"
          title.innerHTML = `<th>Subject</th> <th>recipients</th> <th>Time</th>`;
          document.querySelector('#sentList').append(title);

          emails.forEach(email => {
            var each_email = document.createElement('tr');
            each_email.innerHTML = `<th>${email.subject}</th> <th>${email.recipients}</th> <th>${email.timestamp}</th>`;
            document.querySelector('#sentList').append(each_email);
          });

          document.querySelector('#emailList').style.display = 'none';

          emails.forEach(email => {
            console.log(email);
          });
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }}


    function compose_email() {
      // Show compose view and hide other views
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'block';
      document.querySelector('#email-detail-view').style.display = 'none';

      // Clear out composition fields
      document.querySelector('#compose-recipients').value = '';
      document.querySelector('#compose-subject').value = '';
      document.querySelector('#compose-body').value = '';

      // On form submission, get inputs:
      document.querySelector('#compose-form').onsubmit = () => {
        var recipients = document.querySelector("#compose-recipients").value;
        var subject = document.querySelector("#compose-subject").value;
        var body = document.querySelector("#compose-body").value;

        // Send email out
        fetch(`/emails`, {
          method: 'POST',
          body: JSON.stringify({ recipients: recipients, subject: subject, body: body })
        })
        .then(response => {
          console.log(response)
          console.log(response.status)
          var element = document.createElement('div');
          element.setAttribute("id","submission_message");
          // Check response status
          if (response.status === 400) {
            // Display error message
            element.innerHTML = 'User with email ' + document.querySelector('#compose-recipients').value + ' does not exist';
            document.body.append(element);
          }

          if (response.status === 202 || response.status === 201) {
            // Display success message
            element.innerHTML = 'Email Sent! :)';
            document.body.append(element);
            // Redirect to home page after 3 seconds
            setTimeout(() => {
              load_mailbox('sent')
            }, 300);
            element.innerHTML = ''
          }
        })

        return false; // Prevent default form submission
      };
    }