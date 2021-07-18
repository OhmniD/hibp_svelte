<script>
import { onMount } from 'svelte';

	export let name;

	async function hibpQuery() {
		let response = await fetch('http://localhost:8000/hibp_fetch/account-exists@hibp-integration-tests.com');

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		let data = await response.json()
		let output = await data.map(data =>
		console.log(data)
		)
	}



	onMount(() => {
		hibpQuery()
	})
	
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>

</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>