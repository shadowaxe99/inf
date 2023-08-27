```javascript
// Utility functions for InfluenceAI frontend

// Function to format date for content calendar
export function formatDate(date) {
    let d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    return [year, month, day].join('-');
}

// Function to validate form inputs
export function validateForm(inputs) {
    for (let i = 0; i < inputs.length; i++) {
        if (inputs[i] === '') {
            return false;
        }
    }
    return true;
}

// Function to handle API errors
export function handleApiError(response) {
    if (!response.ok) {
        throw Error(response.statusText);
    }
    return response;
}

// Function to generate unique ID for DOM elements
export function generateId(prefix) {
    return prefix + '_' + Math.random().toString(36).substr(2, 9);
}

// Function to format currency for transactions
export function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(amount);
}

// Function to format phone numbers
export function formatPhoneNumber(phoneNumberString) {
    let cleaned = ('' + phoneNumberString).replace(/\D/g, '');
    let match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
    if (match) {
        return '(' + match[1] + ') ' + match[2] + '-' + match[3];
    }
    return null;
}
```