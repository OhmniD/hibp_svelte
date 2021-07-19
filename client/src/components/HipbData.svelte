<script>
import { onMount } from "svelte";


    export let email

    let hipbdata = []

    async function hibpQuery(email) {
		let response = await fetch(`http://localhost:8000/hibp_fetch/${email}`);

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		let data = await response.json()

        hipbdata = data;

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
