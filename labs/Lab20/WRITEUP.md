1. **The timeout trap.** When the client times out, does that mean the server failed? What's actually happening on the server side when the client gives up waiting?
    I belive the server is still trying to procces the request but the client gets impatient and gives a 404 error. this doesn't mean the server failed though, jsut that the cleint stop trying to reach out to it.



2. **Naming your intent.** What would happen if the idempotency key were a random UUID generated fresh on each retry, instead of a stable `f"{student}-lab{lab}"`? Would retries still prevent duplicate grading? Why or why not?
I think it would still prevent duplicate grading because the whole spirit behind idempotency is for the client and the server to remember, "oh hey I already did this". so I don't think it would stop preventing it.

3. **Sync vs. async.** The CoinGecko API from Lab 19 returned prices immediately (sync). The grading API in Task 4 returns a job ID and makes you poll (async). What's the deciding factor for when an API should use each approach?
I feel like it would be time and cost. if the immeditate is faster and less time consuming I would assume the API is going to lean that way but if on the backend it is way more expensive to do that maybe they go over to Async which could take a little bit more time but be cost effective.

4. **Hidden state.** The lecture says "the API hides state from you." Where in this lab did you experience hidden state? What was hidden, and what design decision made it visible?
Before we added the 202 and it was jsut telling us 200. it allowed us to see that the API still hadn't fully gotten it yet!