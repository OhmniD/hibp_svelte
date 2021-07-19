<script>
import { onMount } from "svelte";
import Bottleneck from "bottleneck"


    export let email

    let hipbdata = []

    const limiter = new Bottleneck({
        maxConcurrent: 1,
        minTime: 333
    })

    async function hibpQuery(email) {
		let response = await limiter.schedule(() => fetch(`http://localhost:8000/hibp_fetch/${email.email}`));

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		let data = await response.json()

        hipbdata = data;

        if (data.length === 0) {
			email.num_of_breaches = 0
		}  else {
			email.num_of_breaches = data.length
		}

        let update = await fetch(`http://localhost:8000/emails/${email.id}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(email)
		})
		// return update.json()

	}

    onMount(() => { 
        hibpQuery(email)
    })

</script>

<ul>
    {#each hipbdata as breach}
    <li>
    <p>{breach.Name} - Breached {breach.BreachDate}</p>
    <!-- <p>{breach.Description}</p> -->

    <!-- <img src={breach.LogoPath}> -->
    </li>
    {/each}
</ul>
