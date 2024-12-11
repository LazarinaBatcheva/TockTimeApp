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

function getHeaders() {
    return {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken(),
    };
}

function handleError(error, defaultMessage = 'An error occurred.') {
    console.error(error);
    alert(defaultMessage);
}

/**
 * Sends a friend request to the specified user.
 * @param {string} receiverUsername - The username of the recipient.
 */
async function sendFriendRequest(receiverUsername) {
    try {
        const response = await fetch('/friends/api/friend-requests/', {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify({ receiver_username: receiverUsername }),
        });

        if (response.ok) {
            alert(`Friend request sent to ${receiverUsername}!`);
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        handleError(error, 'Error sending friend request.');
    }
}

function createRequestElement(request) {
    const div = document.createElement('div');
    div.className = 'friend-request';

    const text = document.createElement('p');
    text.textContent = `${request.sender_username} sent you a friend request.`;

    const acceptButton = document.createElement('button');
    acceptButton.textContent = 'Accept';
    acceptButton.className = 'btn btn-success';
    acceptButton.addEventListener('click', () => updateFriendRequest(request.id, 'accepted'));

    const rejectButton = document.createElement('button');
    rejectButton.textContent = 'Reject';
    rejectButton.className = 'btn btn-danger';
    rejectButton.addEventListener('click', () => updateFriendRequest(request.id, 'rejected'));

    div.append(text, acceptButton, rejectButton);
    return div;
}

async function listFriendRequests() {
    try {
        const response = await fetch('/friends/api/friend-requests/', {
            method: 'GET',
            headers: getHeaders(),
        });

        if (response.ok) {
            const requests = await response.json();
            const container = document.getElementById('friend-requests-container');
            const countElement = document.getElementById('requests-count');

            if (!container || !countElement) return;

            container.innerHTML = '';
            countElement.textContent = requests.length > 0
                ? `You have ${requests.length} friend request(s).`
                : 'You have no pending friend requests.';
            countElement.style.display = 'inline-block';

            requests.forEach(request => container.appendChild(createRequestElement(request)));
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        handleError(error, 'Error fetching friend requests.');
    }
}

async function updateFriendRequest(requestId, status) {
    try {
        const response = await fetch(`/friends/api/friend-requests/${requestId}/`, {
            method: 'PUT',
            headers: getHeaders(),
            body: JSON.stringify({ status }),
        });

        if (response.ok) {
            alert(`Friend request ${status} successfully!`);
            await listFriendRequests();
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        handleError(error, 'Error updating friend request.');
    }
}

async function removeFriend(friendId) {
    try {
        const response = await fetch(`/friends/api/friends-remove/${friendId}/`, {
            method: 'DELETE',
            headers: getHeaders(),
        });

        if (response.ok) {
            alert('Friend removed successfully!');
            await listFriendRequests();
        } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.detail}`);
        }
    } catch (error) {
        handleError(error, 'Error removing friend.');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.send-friend-request-btn').forEach(button => {
        button.addEventListener('click', () => sendFriendRequest(button.dataset.username));
    });

    const loadRequestsButton = document.getElementById('load-requests-btn');
    if (loadRequestsButton) {
        loadRequestsButton.addEventListener('click', listFriendRequests);
    }

    document.querySelectorAll('.remove-friend-btn').forEach(button => {
        button.addEventListener('click', () => removeFriend(button.dataset.friendid));
    });
});
