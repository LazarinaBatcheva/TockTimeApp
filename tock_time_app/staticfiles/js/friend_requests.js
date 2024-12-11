function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return null;
}

/**
 * Sends a friend request to the specified user.
 * @param {string} receiverUsername - The username of the recipient.
 */
async function sendFriendRequest(receiverUsername) {
    try {
        const response = await fetch('/friends/api/friend-requests/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({receiver_username: receiverUsername}),
        });

        if (response.ok) {
            const data = await response.json();
            alert(`Friend request sent to ${receiverUsername}!`);
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        console.error('Error sending friend request:', error);
        alert('An error occurred while sending the friend request.');
    }
}

/**
 * Fetches and displays the list of friend requests for the current user.
 */
async function listFriendRequests() {
    try {
        // Send a GET request to retrieve the list of friend requests
        const response = await fetch('/friends/api/friend-requests/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(), // Include the CSRF token for security
            },
        });

        if (response.ok) {
            // Parse the response as JSON
            const requests = await response.json();
            const requestsCount = requests.length;

            // Display the number of requests in the button
            const countElement = document.getElementById('requests-count');
            if (requestsCount > 0) {
                countElement.textContent = `You have ${requestsCount} friend request(s).`;
                countElement.style.display = 'inline-block'; // Show the count
            } else {
                countElement.textContent = 'You have no pending friend requests.';
                countElement.style.display = 'inline-block'; // Show the message
            }

            // Get the container element where requests will be displayed
            const container = document.getElementById('friend-requests-container');
            container.innerHTML = ''; // Clear any previous content

            // Loop through each friend request and dynamically create elements
            requests.forEach(request => {
                // Create a container <div> for the friend request
                const div = document.createElement('div');
                div.className = 'friend-request'; // Add a class for styling

                // Create a <p> element to display the sender's name
                const text = document.createElement('p');
                text.textContent = `${request.sender_username} sent you a friend request.`;

                // Create an "Accept" button
                const acceptButton = document.createElement('button');
                acceptButton.textContent = 'Accept';
                acceptButton.className = 'btn btn-success'; // Add a class for styling
                acceptButton.addEventListener('click', () => {
                    updateFriendRequest(request.id, 'accepted'); // Call function to accept the request
                });

                // Create a "Reject" button
                const rejectButton = document.createElement('button');
                rejectButton.textContent = 'Reject';
                rejectButton.className = 'btn btn-danger'; // Add a class for styling
                rejectButton.addEventListener('click', () => {
                    updateFriendRequest(request.id, 'rejected'); // Call function to reject the request
                });

                // Append the text and buttons to the request container
                div.appendChild(text);
                div.appendChild(acceptButton);
                div.appendChild(rejectButton);

                // Append the request container to the main container
                container.appendChild(div);
            });
        } else {
            // Handle errors from the server response
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        // Handle any network or runtime errors
        console.error('Error fetching friend requests:', error);
        alert('An error occurred while fetching friend requests.');
    }
}

/**
 * Updates the status of a friend request.
 * @param {number} requestId - The ID of the friend request.
 * @param {string} status - The new status ('accepted' or 'rejected').
 */
async function updateFriendRequest(requestId, status) {
    try {
        const response = await fetch(`/friends/api/friend-requests/${requestId}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({status}),
        });

        if (response.ok) {
            alert(`Friend request ${status} successfully!`);
            await listFriendRequests();
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        console.error('Error updating friend request:', error);
        alert('An error occurred while updating the friend request.');
    }
}

/**
 * Sends a DELETE request to remove a friend.
 * @param {number} friendId - The ID of the friend to remove.
 */
async function removeFriend(friendId) {
    try {
        // Send DELETE request to the API
        const response = await fetch(`/friends/api/friends-remove/${friendId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(), // Include CSRF token
            },
        });

        if (response.ok) {
            alert('Friend removed successfully!');
            // Optionally refresh the friend list or update the UI
            listFriends();
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        console.error('Error removing friend:', error);
        alert('An error occurred while removing the friend.');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Listener for sending friend requests
    document.querySelectorAll('.send-friend-request-btn').forEach(button => {
        button.addEventListener('click', () => {
            const username = button.dataset.username;
            sendFriendRequest(username);
        });
    });

    // Listener for listing friend requests
    const loadRequestsButton = document.getElementById('load-requests-btn');
    if (loadRequestsButton) {
        loadRequestsButton.addEventListener('click', listFriendRequests);
    }

    // Listener to all "Remove Friend" buttons.
    document.querySelectorAll('.remove-friend-btn').forEach(button => {
        button.addEventListener('click', () => {
            const friendId = button.dataset.friendid;
            removeFriend(friendId); // Call the remove friend function
        });
    });
});
