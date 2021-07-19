<script>
import { onMount } from 'svelte';

	import Emails from '../components/Email.svelte'

	let emails = [];

	async function updateNumOfBreaches(email) {
		let response = await fetch(`http://localhost:8000/hibp_fetch/no_detail/${email.email}`)

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}
		const data = await response.json()

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
		return update.json()
	}

	async function getEmails() {
		let response = await fetch('http://localhost:8000/emails');

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}
		emails = await response.json()

		emails.map(email => updateNumOfBreaches(email))
	}



	onMount(() => {
		getEmails()
	})
	
</script>

<main>
	<!-- <h1>Hello!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p> -->
	<Emails emails={emails}/>

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