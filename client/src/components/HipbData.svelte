<script>
import { getContext, onMount } from "svelte";
import Bottleneck from "bottleneck"
import BreachInfo from './BreachInfo.svelte'
import { fade } from 'svelte/transition'


    export let email

    let hibpdata = []

    const limiter = new Bottleneck({
        minTime: 333,
        maxConcurrent: 1
        
    })

    const { open } = getContext('simple-modal');

    const showBreachInfo = (breach) => {
        open(BreachInfo, { breach })
    }

    async function hibpQuery(email) {
		let response = await limiter.schedule(() => fetch(`http://localhost:8000/hibp_fetch/${email.email}`));

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		let data = await response.json()

        hibpdata = data;

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
	}

    onMount(() => { 
        hibpQuery(email)
    })

</script>

{#if hibpdata.length === 0 && email.num_of_breaches !== 0}
<div transition:fade class="loader"></div>
{:else}
<ul transition:fade>
    {#each hibpdata as breach}
    <li>
        <p class="breach" on:click={showBreachInfo(breach)}>{breach.Name} (Breached - {breach.BreachDate})</p>
    </li>
    {/each}
</ul>
{/if}

<style>
    .loader {
  border: 16px solid #f3f3f3; /* Light grey */
  border-top: 16px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
li {
    list-style-type: none;
}

.breach {
    transition: 0.15s ease-in-out;
}
.breach:hover {
    transform: scale(1.05);
    transition: 0.15s ease-in-out;
    background: linear-gradient(90deg,dodgerblue,#e52e71);
    cursor: pointer;
    text-shadow: none;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
}
</style>

