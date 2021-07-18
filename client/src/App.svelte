<script>
import { onMount } from 'svelte';

	let emails = [];

	async function hibpQuery(email) {
		let response = await fetch(`http://localhost:8000/hibp_fetch/account-exists@hibp-integration-tests.com/${email}`);

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		let data = await response.json()
		let output = await data.map(data =>
		console.log(data)
		)
	}

	async function getEmails() {
		let response = await fetch('http://localhost:8000/emails');

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}
		emails = await response.json()
	}



	onMount(() => {
		getEmails()
	})
	
</script>

<main>
	<h1>Hello!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<div>
		{#each emails as email}
		<p>{email.email}</p>
		{:else}
		<p>Nothing to see here yet</p>
		{/each}
	</div>

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