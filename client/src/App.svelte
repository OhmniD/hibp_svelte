<script>
import { onMount } from 'svelte';

	import Emails from './components/Email.svelte'
	import Form from './components/Form.svelte'

	let emails = [];

	async function updateNumOfBreaches(email) {
		let response = await fetch(`http://localhost:8000/hibp_fetch/no_detail/${email.email}`)

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		if (await response.json != undefined) {
			const data = await response.json()
		} else {
			return console.log("Thingy")
		}
		
		

		// if (data.length === 0) {
		// 	email.num_of_breaches = 0
		// }  else {
		// 	email.num_of_breaches = data.length
		// }

	
		// let update = await fetch(`http://localhost:8000/emails/${email.id}`, {
		// 	method: 'POST',
		// 	headers: {
		// 		'Content-Type': 'application/json'
		// 	},
		// 	body: JSON.stringify(email)
		// })
		// return update.json()
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
	<Form />
	<Emails emails={emails}/>

</main>

<style>
	@import url('https://fonts.googleapis.com/css2?family=PT+Sans&family=Roboto&display=swap');

	* {
		margin: 0;
		padding: 0;
	}
	
	main {
	background-color:#282c34;
	color: #f3f3f3;
	font-family:"Roboto";
	min-height: 100vh;
	}
	
</style>