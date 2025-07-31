# BookNest User Registration: Asynchronous Background Email Task

## Task Overview
BookNest has seen a sharp increase in new user signups. The platform's user registration endpoint currently sends email confirmations directly in the request handler, causing API latency spikes during high traffic. This slows down registration for users and can degrade scalability. Your team needs to improve this endpoint so that confirmation emails are sent in the background, allowing the API to respond quickly while emails are delivered reliably.

## Guidance
- All code is in `main.py`, which contains the FastAPI app, registration route, and the outline for email sending functionality.
- The registration endpoint and model are present, but the email sending logic is synchronous and directly in the request/response flow.
- The email sending function is a stub (simulates delay), letting you focus on asynchronous/task handling, not integration with a real email provider.

## Objectives
- Refactor the user registration process so that sending the confirmation email happens in a background task, not in the main handler.
- Apply FastAPI best practices for using asynchronous routes and background task dependencies.
- Ensure the API responds quickly after registration, completing the email sending separately.
- Demonstrate basic async/await usage as appropriate, even if the provided stub is a simulated async operation.

## How to Verify
- When POSTing to `/register` with valid data, the route quickly returns a success response without waiting for the email logic.
- The simulated email send function runs asynchronously after the response (can log a message to console to confirm execution time/order).
- The server is responsive during registration requests, even if the email stub introduces an artificial delay.
- Registration with missing or invalid data returns a 422 error as expected (input validation is retained).
