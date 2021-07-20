<script>
import { getContext, onMount } from "svelte";
import Bottleneck from "bottleneck"
import BreachInfo from './BreachInfo.svelte'


    export let email

    let hipbdata = []

    const limiter = new Bottleneck({
        maxConcurrent: 1,
        minTime: 333
    })

    const { open } = getContext('simple-modal');

    const showBreachInfo = (breach) => {
        open(BreachInfo, { message: breach.Description })
    }

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

        // Put in a get here to check if the number of breaches retrieved === number of breaches in database - only update if there has been a change/increase

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
        <p on:click={showBreachInfo(breach)}>{breach.Name} - Breached {breach.BreachDate}</p>
    </li>
    {/each}
</ul>
